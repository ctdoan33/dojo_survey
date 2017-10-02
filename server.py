from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route("/")
def survey():
    return render_template("index.html")
@app.route("/result", methods=["POST"])
def result():
    name = request.form["name"]
    if len(name)<1:
        flash("Name field cannot be blank")
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]
    if len(comment)>120:
        flash("Comment cannot be more than 120 characters")
    return render_template("result.html", name=name, location=location, language=language, comment=comment)
app.run(debug=True)