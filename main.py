from flask import Flask, redirect, url_for, render_template, request
import coronaWebScrape

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        country = request.form["nm"]
        return redirect(url_for("country", ctr=country))
    else:
        return render_template("index.html")
    
@app.route("/<ctr>")
def country(ctr):
    ctr = coronaWebScrape.scrape(ctr)
    if ctr == None:
        return redirect(url_for("home"))
    else:
        return f"""<h2>{ctr}</h2><p><a href="{{url_for(app.home)}}">Return Home</a></p>"""

if __name__ == "__main__":
    app.run()