from models.event import *

event1 = Event("10/07/2021", "Metallica", 1000, "Belhouston", "Heavy Metal")

event2 = Event("06/08/2021", "Chic", 500, "Kelvingrove Band Stand", "Disco")

events = [event1, event2]

def create_event(event):
    events.append(event)

def list_all_events(self):
    pass