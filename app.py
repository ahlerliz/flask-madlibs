from flask import Flask, render_template, request
from flask.templating import render_template_string
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

#populate the list of (verb/adjective/nouns)
#loop over the list and fill in html element with each one
# grab the data from user reponses, post route?
# 
prompts = silly_story.prompts

@app.get("/questions")
def get_questions():
    """Dynamically populates the questions.html with the prompts from a story instance """
    return render_template("questions.html", prompts=prompts)


@app.get("/story")
def make_story():
    """Retrieves user inputed prompt answers from questions.html form and generates a story with the answers"""
    answers = request.args
    story = silly_story.generate(answers)
    return render_template("story.html", story = story)
    #Question: why would you use render_template_string