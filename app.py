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
    return render_template("questions.html", prompts=prompts)