from flask import render_template, request
from app import app
from models.event import Event
from models.events_example import events

@app.route("/")
def index():
    return render_template('index.html', title="Home", events=events)

@app.route('/', methods=['POST'])
def add_task():
    date = request.form['date']
    name_of_event = request.form['name_of_event']
    number_of_guests = request.form['number_of_guests']
    room_location = request.form['room_location']
    description = request.form['description']
    new_event = Event(date, name_of_event, number_of_guests, room_location, description)
    print(request.form)
    create_event(new_event)
    return render_template('index.html', title="Home", events=events)
    