from flask import Flask
from flask import render_template
from flask import request
import userManagement as dbHandler

app = Flask(__name__)


@app.route("/sucess.html", methods=["POST", "GET", "PUT", "PATCH", "DELETE"])
def addFeedback():
    if request.method == "POST":
        feedback = request.form["feedback"]
        dbHandler.insertFeedback(feedback)
        dbHandler.listFeedback()
        return render_template("/sucess.html", state=True, value="Back")
    else:
        dbHandler.listFeedback()
        return render_template("/sucess.html", state=True, value="Back")


@app.route("/signup.html", methods=["POST", "GET", "PUT", "PATCH", "DELETE"])
def signup():
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
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        isLoggedIn = dbHandler.retrieveUsers(username, password)
        if isLoggedIn:
            dbHandler.listFeedback()
            return render_template("/sucess.html", value=username, state=isLoggedIn)
        else:
            return render_template("/index.html")
    else:
        return render_template("/index.html")


if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    app.run(debug=True, host="0.0.0.0", port=5000)
