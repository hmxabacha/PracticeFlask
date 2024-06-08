from flask import Flask, request, render_template,redirect
import sqlite3

app=Flask(__name__)

db=sqlite3.connect("bacha.db")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register",methods=["POST"])
def register():
    name=request.form.get("name")
    password=request.form.get("password")
    confirm=request.form.get("confirmPassword")
    if not name or not password or not confirm or password != confirm:
        return "Something Is Missing OR Password Un-match!!"
    db=sqlite3.connect("bacha.db")
    db.execute("INSERT INTO login(name,password) VALUES(?,?)",(name,password))
    db.commit()
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    db=sqlite3.connect("bacha.db")
    registrants=db.execute("SELECT * FROM login")
    return render_template("registrants.html",registrants=registrants)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/certificates")
def certificates():
    return render_template("certificates.html")