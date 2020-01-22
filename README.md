# Events platform

This platform provides access to the data of the latest sports events. It allows for the addition and modification of sports events.

## Getting started
These instructions will get a copy of the project up and running on your local machine.

## Pre-requisites


1. _Redis_ is installed on your local machine. To install Redis follow these instructions:
```
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make
```

For more details see <https://redis.io/topics/quickstart>

2. _redis-py_  Python package is installed.
```
pip install redis-py
```
For more details see <https://pypi.org/project/redis/>


3. _tornado_ Python package is installed.
```
pip install redis.py
```
For more details see <https://pypi.org/project/tornado/3.2.1/>


## Steps to run the app:

1. Run the redis server on localhost:
```
redis-server
```

2. Run the Python app:
```
python app/app.py
```

This will run on localhost and port 8080 by default.

## Accessing the API
The following endpoints are exposed:

http://<server:port>/api/match/

##Request types:
The following request types have been implemented:

GET | POST | PUT

##Example requests:
GET request with _resource id_:

```
"curl -v http://localhost:8080/api/match/1"
```

Get request with _name_ parameter:
```
curl -v "http://localhost:8080/api/match/?name=Fleetwood%20vs%20Day%20vs%20Rose"
```

Get request with _sport_ and _ordering_ parameters:

```
curl -v "http://localhost:8080/api/match/?sport=hurling&ordering=startTime"
```

Sample new event message:
```
{
  "id": 8661032861909884001,
  "message_type": "NewEvent",
  "event": {
    "id": 1,
    "name": "Cork vs Galway",
    "startTime": "2020-04-19 15:35:00",
    "sport": {
      "id": 221,
      "name": "Hurling"
    },
    "markets": [
      {
        "id": 385086549360973400,
        "name": "Winner",
        "selections": [
          {
            "id": 8243901714083343000,
            "name": "Cork",
            "odds": 1.01
          },
          {
            "id": 5737666888266680000,
            "name": "Galway",
            "odds": 1.01
          }
        ]
      }
    ]
  }
}
```

POST request to create a new event:
```
curl --header "Content-Type: application/json" -d "{\"id\":8661032861909884001,\"message_type\":\"NewEvent\",\"event\":{\"id\":13,\"name\":\"Cork vs Galway\",\"startTime\":\"2020-04-19 15:35:00\",\"sport\":{\"id\":221,\"name\":\"Hurling\"},\"markets\":[{\"id\":385086549360973400,\"name\":\"Winner\",\"selections\":[{\"id\":8243901714083343000,\"name\":\"Cork\",\"odds\":1.01},{\"id\":5737666888266680000,\"name\":\"Galway\",\"odds\":1.01}]}]}}" http://localhost:8080/api/match/
```

Sample update odds message:
```
{
  "id": 8661032861909884001,
  "message_type": "UpdateOdds",
  "event": {
    "id": 1,
    "name": "Cork vs Galway",
    "startTime": "2020-04-19 15:35:00",
    "sport": {
      "id": 221,
      "name": "Hurling"
    },
    "markets": [
      {
        "id": 385086549360973400,
        "name": "Winner",
        "selections": [
          {
            "id": 8243901714083343000,
            "name": "Cork",
            "odds": 1.04
          },
          {
            "id": 5737666888266680000,
            "name": "Galway",
            "odds": 1.31
          }
        ]
      }
    ]
  }
}
```

PUT request to update odds:

```
curl -X PUT --header "Content-Type: application/json" -d "{\"id\":8661032861909884001,\"message_type\":\"UpdateOdds\",\"event\":{\"id\":13,\"name\":\"Cork vs Galway\",\"startTime\":\"2020-04-19 15:35:00\",\"sport\":{\"id\":221,\"name\":\"Hurling\"},\"markets\":[{\"id\":385086549360973400,\"name\":\"Winner\",\"selections\":[{\"id\":8243901714083343000,\"name\":\"Cork\",\"odds\":1.04},{\"id\":5737666888266680000,\"name\":\"Galway\",\"odds\":1.31}]}]}}" http://localhost:8080/api/match/
```

##Running Unittests

```
pip install mock
python test/test_event_utils.py
```
