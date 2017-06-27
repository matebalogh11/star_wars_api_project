from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main.html")


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
