import json


def get_event_by_name(event_name, db):
    event_db = db.keys('*')
    required_event = None
    for event in event_db:
        event_details = json.loads(r.mget(event)[0])
        if event_name.lower() == event_details["name"].lower():
            required_event = event_details
            break
    return required_event


def get_sorted_sports_events(sport, order_by, db):
    event_db = db.keys('*')
    sorted_events = []

    for event in event_db:
        event_details = json.loads(db.mget(event)[0])
        if event_details["sport"]["name"].lower() == sport.lower():
            sport_event = create_event_details(event_details)
            sorted_events.append(sport_event)

    return sorted(sorted_events, key=lambda i: i[order_by])


def get_event_id(message):
    return f'{message["event"]["id"]}'


def get_event(message):
    return message["event"]


def create_event_details(event):
    return {
        "id": event["id"],
        "url": event["url"],
        "name": event["name"],
        "startTime": event["startTime"]
    }


def add_event_url(event):
    event["url"] = generate_event_url(event["id"])


def generate_event_url(event_id):
    return f'http://127.0.0.1/api/match/{event_id}'
