from flask import Flask, render_template, redirect, url_for, session, request, flash, jsonify, send_from_directory
from os import urandom
import logic

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    """Validate the submitted form then save the credentials in the database."""
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
    """Check the credentials in the db then initialise a session."""
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
    """Kill the session when the user logs out."""
    session.pop("username", None)
    return redirect(url_for("index"))


@app.route("/votes", methods=["POST"])
def votes():
    """Save the ajax request in the db if the user votes."""
    data = request.get_json(silent=True)
    success = '{"stage": "success"}'
    username = session["username"]
    logic.save_votes(data, username)
    return success


@app.route("/votestat")
def votestat():
    """Return vote stats from db."""
    stats = jsonify(logic.fetch_statistics())
    return stats


@app.route("/images/<path:filename>")
def send_gritter_files(filename):
    """Serve the requested dir/files to gritter."""
    return send_from_directory("images", filename)

if __name__ == "__main__":
    app.secret_key = urandom(13)
    app.run()
