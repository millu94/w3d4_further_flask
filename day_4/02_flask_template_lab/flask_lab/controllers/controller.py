from flask import render_template, request
from app import app
from models.event import Event
from models.events_example import events

@app.route("/")
def index():
    return render_template('index.html', title="Home", events=events)