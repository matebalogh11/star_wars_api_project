from flask import Flask, render_template, redirect, url_for, session, request, flash, jsonify, send_from_directory
from flask_sslify import SSLify
from os import urandom, path
import logic

app = Flask(__name__)
sslify = SSLify(app)
app.secret_key = urandom(13)


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
                session["username"] = usrn
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
            session["username"] = usrn
            return redirect(url_for("index"))
        flash("Invalid credentials", "error")
        return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


@app.route("/votes", methods=["POST"])
def votes():
    data = request.get_json(silent=True)
    success = '{"stage": "success"}'
    username = session["username"]
    logic.save_votes(data, username)
    return success


@app.route("/votestat")
def votestat():
    stats = jsonify(logic.fetch_statistics())
    return stats


@app.route("/images/<path:filename>")
def send_gritter_files(filename):
    return send_from_directory("images", filename)

if __name__ == "__main__":
    app.run()
