# Events platform

This platform provides access to data of the latest sports events. It allow for the addition and modification of sports events.

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


3. tornado Python package is installed.
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

## Accessing the API
The following endpoints are exposed.:
../api/match/

##Running the Unittests
blah
