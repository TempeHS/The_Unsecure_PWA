from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import user_management as dbHandler
import os
import sqlite3
import logging
import sys

# Configure comprehensive logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)

app = Flask(__name__)

# Enable Flask logging
app.logger.setLevel(logging.DEBUG)
app.logger.info("Flask application starting up...")

# Code snippet for logging a message
# app.logger.critical("message")


# Initialize required files and directories
def init_app():
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


# Initialize the app
init_app()


@app.route("/health")
def health_check():
    """Health check endpoint for monitoring."""
    app.logger.info("Health check endpoint accessed")
    try:
        # Test database connection
        import sqlite3

        con = sqlite3.connect("database_files/database.db")
        con.close()
        app.logger.info("Health check: Database connection successful")
        return {
            "status": "healthy",
            "message": "App is running",
            "database": "connected",
        }, 200
    except Exception as e:
        app.logger.error(f"Health check failed: {str(e)}")
        return {"status": "unhealthy", "message": f"Database error: {str(e)}"}, 500


@app.route("/success.html", methods=["POST", "GET", "PUT", "PATCH", "DELETE"])
def addFeedback():
    app.logger.info(f"addFeedback endpoint accessed with method: {request.method}")
    try:
        if request.method == "GET" and request.args.get("url"):
            url = request.args.get("url", "")
            app.logger.info(f"Redirecting to URL: {url}")
            return redirect(url, code=302)
        if request.method == "POST":
            feedback = request.form["feedback"]
            app.logger.info(f"Processing feedback submission")
            dbHandler.insertFeedback(feedback)
            dbHandler.listFeedback()
            return render_template("/success.html", state=True, value="Back")
        else:
            app.logger.info("Displaying feedback list")
            dbHandler.listFeedback()
            return render_template("/success.html", state=True, value="Back")
    except Exception as e:
        app.logger.error(f"Error in addFeedback: {str(e)}")
        return (
            render_template("/success.html", state=False, value="Error occurred"),
            500,
        )


@app.route("/signup.html", methods=["POST", "GET", "PUT", "PATCH", "DELETE"])
def signup():
    app.logger.info(f"signup endpoint accessed with method: {request.method}")
    try:
        if request.method == "GET" and request.args.get("url"):
            url = request.args.get("url", "")
            app.logger.info(f"Redirecting to URL: {url}")
            return redirect(url, code=302)
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            DoB = request.form["dob"]
            app.logger.info(f"Processing user signup for username: {username}")
            dbHandler.insertUser(username, password, DoB)
            return render_template("/index.html")
        else:
            app.logger.info("Displaying signup form")
            return render_template("/signup.html")
    except Exception as e:
        app.logger.error(f"Error in signup: {str(e)}")
        return render_template("/signup.html"), 500


@app.route("/index.html", methods=["POST", "GET", "PUT", "PATCH", "DELETE"])
@app.route("/", methods=["POST", "GET"])
def home():
    app.logger.info(f"home endpoint accessed with method: {request.method}")
    try:
        # Simple Dynamic menu
        if request.method == "GET" and request.args.get("url"):
            url = request.args.get("url", "")
            app.logger.info(f"Redirecting to URL: {url}")
            return redirect(url, code=302)
        # Pass message to front end
        elif request.method == "GET":
            msg = request.args.get("msg", "")
            app.logger.info(f"Displaying home page with message: {msg}")
            return render_template("/index.html", msg=msg)
        elif request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            app.logger.info(f"Processing login for username: {username}")
            isLoggedIn = dbHandler.retrieveUsers(username, password)
            if isLoggedIn:
                app.logger.info(f"Login successful for user: {username}")
                dbHandler.listFeedback()
                return render_template(
                    "/success.html", value=username, state=isLoggedIn
                )
            else:
                app.logger.warning(f"Login failed for user: {username}")
                return render_template("/index.html")
        else:
            app.logger.info("Displaying default home page")
            return render_template("/index.html")
    except Exception as e:
        app.logger.error(f"Error in home: {str(e)}")
        return render_template("/index.html"), 500


if __name__ == "__main__":
    app.logger.info("Starting Flask application in main...")
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    app.run(debug=False, host="0.0.0.0", port=10000)
