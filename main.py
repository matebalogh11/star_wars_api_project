from flask import Flask, render_template, redirect, url_for, session, request, flash
from os import urandom
import logic

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        usrn = request.form["username"]
        pw = request.form["password"]
        if logic.check_credentials(usrn, pw):
            if logic.check_username(usrn):
                logic.save_credentials(usrn, pw)
                session["username"] = request.form["username"]
                return redirect(url_for("index"))
            flash("This username is already in use!", "error")
            return redirect(url_for("registration"))
        flash("Your password must be at least 5 characters long!", "error")
        return redirect(url_for("registration"))
    return render_template("registration.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usrn = request.form["username"]
        pw = request.form["password"]
        if logic.check_login(usrn, pw):
            session["username"] = request.form.get("username")
            return redirect(url_for("index"))
        flash("Invalid credentials", "error")
        return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


def main():
    app.secret_key = urandom(13)
    app.run(debug=True)


if __name__ == "__main__":
    main()
