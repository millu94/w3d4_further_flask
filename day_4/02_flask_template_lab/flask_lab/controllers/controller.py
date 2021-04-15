from flask import render_template, request
from app import app
from models.events_example import events, create_event
from models.event import Event


@app.route("/")
def index():
    return render_template('index.html', title="Home", events=events)

@app.route('/', methods=['POST'])
def add_event():
    date = request.form['date']
    name_of_event = request.form['name_of_event']
    number_of_guests = request.form['number_of_guests']
    room_location = request.form['room_location']
    description = request.form['description']
    new_event = Event(date, name_of_event, number_of_guests, room_location, description, False)
    create_event(new_event)
    return render_template('index.html', title="Home", events=events)
    