"""
This script provides a Rest API allowing for the access
and modification of event data.
"""

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json
import redis

import event_utils as utils

r = redis.Redis()


class EventHandler(RequestHandler):

    def send_response(self, data, status=200):
        """Construct and send a JSON response with appropriate status code."""
        self.set_status(status)
        self.write(json.dumps(data))

    def get(self, id=None):
        if id:
            if r.exists(id):
                result = r.mget(id)
                self.write(json.loads(result[0]))
            else:
                self.set_status(404)
                self.write("ID not found")

        elif self.get_argument("name", None):
            match_name = self.get_argument("name").lower()
            event = utils.get_event_by_name(match_name, r)
            if event:
                event_details = utils.create_event_details(event)
                self.send_response([event_details])
            else:
                self.send_response("Event Name not found", 404)

        elif self.get_argument("sport", None) and self.get_argument("ordering", None):
            sport = self.get_argument("sport")
            order_by = self.get_argument("ordering")
            sorted_events = utils.get_sorted_sports_events(sport, order_by, r)
            if sorted_events:
                self.send_response(sorted_events)
            else:
                self.send_response("Could not sort events", 400)

    def post(self, _):
        if self.request.body:
            message = json.loads(self.request.body)
            event = utils.get_event(message)
            event_id = utils.get_event_id(message)
            if not r.exists(event_id):
                utils.add_event_url(event)
                r.mset({event_id: json.dumps(event)})
                self.send_response(event)
            else:
                self.send_response("Event ID already exists", 400)

    def put(self, _):
        message = json.loads(self.request.body)
        event_id = utils.get_event_id(message)
        if r.exists(event_id):
            event = utils.get_event(message)
            utils.add_event_url(event)
            r.mset({event_id: json.dumps(event)})
            self.send_response(event)
        else:
            self.send_response("Event ID can not be found", 404)


def make_app():
    return Application([
        (r"/api/match/([0-9]+)?", EventHandler),
    ], debug=True)


def run_server():
    app = make_app()
    app.listen(8080)
    IOLoop.current().start()


if __name__ == '__main__':
    run_server()
