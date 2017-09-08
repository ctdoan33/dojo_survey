from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def survey():
    return render_template("index.html")
@app.route("/result", methods=["POST"])
def results():
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]
    return render_template("result.html", subname=name, sublocation=location, sublanguage=language, subcomment=comment)
app.run(debug=True)