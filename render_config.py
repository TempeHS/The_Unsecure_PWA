"""
Render.com specific configuration and setup module.
This module contains all customizations needed for deploying to render.com,
keeping the main.py file clean and easily mergeable with the main branch.
"""

import os
import sqlite3
import logging
import sys
from functools import wraps
from flask import Blueprint, request


def setup_logging(app):
    """Configure comprehensive logging for the Flask application."""
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        stream=sys.stdout,
    )

    # Enable Flask logging
    app.logger.setLevel(logging.DEBUG)
    app.logger.info("Flask application starting up...")


def init_app(app):
    """Initialize required files and directories for the application."""
    try:
        app.logger.info("Starting application initialization...")

        # Create database directory if it doesn't exist
        app.logger.info("Creating database directory...")
        os.makedirs("database_files", exist_ok=True)
        app.logger.info("Database directory created/verified")

        # Initialize database if it doesn't exist
        db_path = "database_files/database.db"
        if not os.path.exists(db_path):
            app.logger.info("Database file not found, creating new database...")
            con = sqlite3.connect(db_path)
            cur = con.cursor()

            # Create users table
            app.logger.info("Creating users table...")
            cur.execute(
                """CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                dateOfBirth TEXT NOT NULL
            )"""
            )

            # Create feedback table
            app.logger.info("Creating feedback table...")
            cur.execute(
                """CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                feedback TEXT NOT NULL
            )"""
            )

            con.commit()
            con.close()
            app.logger.info("Database initialized successfully")
        else:
            app.logger.info("Database file already exists")

        # Initialize visitor log if it doesn't exist
        if not os.path.exists("visitor_log.txt"):
            app.logger.info("Creating visitor log file...")
            with open("visitor_log.txt", "w") as f:
                f.write("0")
            app.logger.info("Visitor log initialized")
        else:
            app.logger.info("Visitor log file already exists")

        # Create templates/partials directory if it doesn't exist
        app.logger.info("Creating templates/partials directory...")
        os.makedirs("templates/partials", exist_ok=True)

        # Initialize feedback HTML file if it doesn't exist
        if not os.path.exists("templates/partials/success_feedback.html"):
            app.logger.info("Creating feedback HTML file...")
            with open("templates/partials/success_feedback.html", "w") as f:
                f.write("")
            app.logger.info("Feedback HTML file initialized")
        else:
            app.logger.info("Feedback HTML file already exists")

        app.logger.info("Application initialization completed successfully!")

    except Exception as e:
        app.logger.error(f"Error during application initialization: {str(e)}")
        app.logger.error(f"Exception type: {type(e).__name__}")
        import traceback

        app.logger.error(f"Traceback: {traceback.format_exc()}")
        raise


def with_error_handling(app):
    """Decorator to add consistent error handling and logging to route functions."""

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            app.logger.info(
                f"{f.__name__} endpoint accessed with method: {request.method}"
            )
            try:
                return f(*args, **kwargs)
            except Exception as e:
                app.logger.error(f"Error in {f.__name__}: {str(e)}")
                # Return appropriate error response based on the route
                return f"An error occurred in {f.__name__}", 500

        return decorated_function

    return decorator


# Create a blueprint for render-specific routes
render_bp = Blueprint("render", __name__)


@render_bp.route("/health")
def health_check():
    """Health check endpoint for monitoring."""
    from flask import current_app

    current_app.logger.info("Health check endpoint accessed")
    try:
        # Test database connection
        con = sqlite3.connect("database_files/database.db")
        con.close()
        current_app.logger.info("Health check: Database connection successful")
        return {
            "status": "healthy",
            "message": "App is running",
            "database": "connected",
        }, 200
    except Exception as e:
        current_app.logger.error(f"Health check failed: {str(e)}")
        return {"status": "unhealthy", "message": f"Database error: {str(e)}"}, 500


def create_enhanced_route(app, original_func):
    """Create an enhanced version of a route function with logging and error handling."""

    @wraps(original_func)
    def enhanced_function(*args, **kwargs):
        app.logger.info(
            f"{original_func.__name__} endpoint accessed with method: {request.method}"
        )
        try:
            return original_func(*args, **kwargs)
        except Exception as e:
            app.logger.error(f"Error in {original_func.__name__}: {str(e)}")
            # Return appropriate error response based on the route
            from flask import render_template

            if "signup" in original_func.__name__:
                return render_template("/signup.html"), 500
            elif (
                "success" in original_func.__name__
                or "feedback" in original_func.__name__
            ):
                return (
                    render_template(
                        "/success.html", state=False, value="Error occurred"
                    ),
                    500,
                )
            else:
                return render_template("/index.html"), 500

    return enhanced_function


def configure_app_for_render(app):
    """Configure the Flask app with render.com specific settings."""
    # Setup logging first
    setup_logging(app)

    # Initialize the app (create directories, database, etc.)
    init_app(app)

    # Register render-specific routes
    app.register_blueprint(render_bp)

    # Configure Flask settings for render.com
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

    # Add enhanced logging and error handling to existing routes
    enhance_routes_with_logging(app)

    app.logger.info("Render.com configuration completed")


def enhance_routes_with_logging(app):
    """Add logging and error handling to existing Flask routes."""
    # Store original route functions
    original_endpoints = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint in app.view_functions:
            original_endpoints[rule.endpoint] = app.view_functions[rule.endpoint]

    # Enhance each route with logging and error handling
    for endpoint, func in original_endpoints.items():
        if endpoint not in [
            "static",
            "render.health_check",
        ]:  # Skip static files and our health check
            app.view_functions[endpoint] = create_enhanced_route(app, func)


def get_render_run_config():
    """Get the Flask run configuration for render.com deployment."""
    return {"debug": False, "host": "0.0.0.0", "port": 10000}
