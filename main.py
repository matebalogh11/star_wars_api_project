from flask import Flask, render_template, redirect, url_for, session, request
from werkzeug import security
from os import urandom
import logic

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        if logic.check_credentials(request.form["username"], request.form["password"]):
            logic.save_credentials()
            session["username"] = request.form["username"]
            return redirect(url_for("index"))
    return render_template("registration.html")


@app.route("/login")
def login():
    if request.method == "POST":
        session["username"] = request.form.get("username")
        return redirect(url_for("index"))
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
