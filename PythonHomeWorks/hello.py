from cgitb import html
import imp
from unittest import result
from flask import Flask, render_template, request
from vowelsearch import search4letters

app = Flask(__name__)

@app.route("/")
def hello_python() ->str:
    return "Hello World"

@app.route("/search4", methods=['POST'])
def do_search()->str:
    phrase = request.form["phrase"]
    letters = request.form["letters"]
    title = "Here are your results"
    results = str(search4letters(phrase, letters))
    return render_template(
        "results.html",
        the_title = title ,
        the_phrase = phrase,
        the_letters = letters,
        the_results = results
    )

@app.route("/entry")
def entry_page()->"html":
    return render_template(
        "entry.html",
        the_title = "Welcome to the search4letters website"
    )
app.run()