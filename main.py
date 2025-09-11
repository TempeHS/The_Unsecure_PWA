from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import user_management as dbHandler
import os
import sqlite3

# Code snippet for logging a message
# app.logger.critical("message")

app = Flask(__name__)


# Initialize required files and directories
def init_app():
    """Initialize required files and directories for the application."""
    # Create database directory if it doesn't exist
    os.makedirs("database_files", exist_ok=True)

    # Initialize database if it doesn't exist
    db_path = "database_files/database.db"
    if not os.path.exists(db_path):
        con = sqlite3.connect(db_path)
        cur = con.cursor()

        # Create users table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            dateOfBirth TEXT NOT NULL
        )"""
        )

        # Create feedback table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            feedback TEXT NOT NULL
        )"""
        )

        con.commit()
        con.close()
        print("Database initialized successfully")

    # Initialize visitor log if it doesn't exist
    if not os.path.exists("visitor_log.txt"):
        with open("visitor_log.txt", "w") as f:
            f.write("0")
        print("Visitor log initialized")

    # Create templates/partials directory if it doesn't exist
    os.makedirs("templates/partials", exist_ok=True)

    # Initialize feedback HTML file if it doesn't exist
    if not os.path.exists("templates/partials/success_feedback.html"):
        with open("templates/partials/success_feedback.html", "w") as f:
            f.write("")
        print("Feedback HTML file initialized")


# Initialize the app
init_app()


@app.route("/health")
def health_check():
    """Health check endpoint for monitoring."""
    return {"status": "healthy", "message": "App is running"}, 200


@app.route("/success.html", methods=["POST", "GET", "PUT", "PATCH", "DELETE"])
def addFeedback():
    if request.method == "GET" and request.args.get("url"):
        url = request.args.get("url", "")
        return redirect(url, code=302)
    if request.method == "POST":
        feedback = request.form["feedback"]
        dbHandler.insertFeedback(feedback)
        dbHandler.listFeedback()
        return render_template("/success.html", state=True, value="Back")
    else:
        dbHandler.listFeedback()
        return render_template("/success.html", state=True, value="Back")


@app.route("/signup.html", methods=["POST", "GET", "PUT", "PATCH", "DELETE"])
def signup():
    if request.method == "GET" and request.args.get("url"):
        url = request.args.get("url", "")
        return redirect(url, code=302)
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        DoB = request.form["dob"]
        dbHandler.insertUser(username, password, DoB)
        return render_template("/index.html")
    else:
        return render_template("/signup.html")


@app.route("/index.html", methods=["POST", "GET", "PUT", "PATCH", "DELETE"])
@app.route("/", methods=["POST", "GET"])
def home():
    # Simple Dynamic menu
    if request.method == "GET" and request.args.get("url"):
        url = request.args.get("url", "")
        return redirect(url, code=302)
    # Pass message to front end
    elif request.method == "GET":
        msg = request.args.get("msg", "")
        return render_template("/index.html", msg=msg)
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        isLoggedIn = dbHandler.retrieveUsers(username, password)
        if isLoggedIn:
            dbHandler.listFeedback()
            return render_template("/success.html", value=username, state=isLoggedIn)
        else:
            return render_template("/index.html")
    else:
        return render_template("/index.html")


if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    app.run(debug=False, host="0.0.0.0", port=10000)
