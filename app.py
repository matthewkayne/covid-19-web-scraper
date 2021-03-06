"""Flask Site"""

from flask import Flask, redirect, url_for, render_template, request
import corona_web_scrape

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    """home"""
    if request.method == "POST":
        country_input = request.form["nm"]
        return redirect(url_for("country", ctr=country_input))
    return render_template("index.html")


@app.route("/<ctr>")
def country(ctr):
    """country"""
    ctr = corona_web_scrape.scrape(ctr)
    if ctr is None:
        return redirect(url_for("home"))
    return render_template("result.html", country=ctr, home_url=url_for("home"))


if __name__ == "__main__":
    app.run()
