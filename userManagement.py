import sqlite3 as sql
import json


def insertUser(username, password, DoB):
    con = sql.connect("databaseFiles/database.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO users (username,password,dateOfBirth) VALUES (?,?,?)",
        (username, password, DoB),
    )
    con.commit()
    con.close()


def retrieveUsers(username, password):
    con = sql.connect("databaseFiles/database.db")
    cur = con.cursor()
    cur.execute(
        f"SELECT * FROM users WHERE username == '{username}' AND password == '{password}'"
    )
    if cur.fetchone() == None:
        con.close()
        return False
    else:
        con.close()
        return True


def insertFeedback(feedback):
    con = sql.connect("databaseFiles/database.db")
    cur = con.cursor()
    cur.execute(f"INSERT INTO feedback (feedback) VALUES ('{feedback}')")
    con.commit()
    con.close()


def listFeedback():
    con = sql.connect("databaseFiles/database.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM feedback").fetchall()
    con.close()
    f = open("templates/partials/sucess_feedback.html", "w")
    for row in data:
        f.write("<p>\n")
        f.write(f"{row[1]}\n")
        f.write("</p>\n")
    f.close()
