# johnmmason / pimonitor

![image](https://raw.githubusercontent.com/johnmmason/pimonitor/master/media/splash.png)

piMonitor is a simple application for recording, storing, and sharing sensor data.

## Project Overview

Consumer grade IOT sensors offer convenience and peace-of mind, but lack features important to tech hobbyists such as

* Sensor flexibility,
* customization,
* data security,
* and affordability.

This project attempts to address these issues by creating a software framework for inexpensive, homemade Raspberry-Pi based sensor modules and an accompanying self-hosted data logging server.

This project is still early in its development, so its functionality is rather limited.  Currently, the system supports a DHT22 temperature sensor but could be easily modified for other similar sensors.  Please see below for a list of planned additions to the code.

### Project Components

This project consists of two main components, the server and client(s).  **This repository contains only the server code.  Corresponding client code can be found in [johnmmason/pimonitor-sensor](https://github.com/johnmmason/pimonitor-sensor)**

#### The Server

The server can either be hosted locally or on a cloud instance such as AWS.

The server consists of a Flask-based WSGI application which accepts JSON data (later referred to as "the api") from the sensors and stores the data in a PostgreSQL database.

#### The Client

The client code was developed to run on a Raspberry Pi, and has been tested on both the Raspberry Pi 4 and Raspberry Pi Zero.

The client script reads data from attached sensors (currently supported, a DHT22 temperature and humidity sensor), compiles data into a JSON string, and then sends it to the API via a HTTP POST request.

## Setup and Installation

### Database Setup

You will need the following
* PostgreSQL with a database for this project (this can, but does not have to be, the default database)
* A user with adequate permissions to perform CRUD operations on the project database (this can, but does not have to, be the default user)
* Appropriate configuration to allow remote connections to your database

Open a SQL prompt using a method of your choice and create a table for this project:
```sql
CREATE TABLE home_data(
    id SERIAL,
    location VARCHAR(30),
    timestamp TIMESTAMP,
    temperature REAL,
    humidity real
)
```

### Server Setup

First, update your system and install required dependencies:
```bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install python3-dev python3-pip python3-venv -y
```

Clone this repository:
```bash
git clone https://github.com/johnmmason/pimonitor.git
```

Navigate to the project directory:
```bash
cd pimonitor
pwd
```

Create a Python virtual environment and install Python packages:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create `sample_config.ini` and configure database settings:
```bash
cp sample_config.ini config.ini
emacs config.ini
```

Set environment variables for Flask:
```bash
export FLASK_APP=pimonitor
export FLASK_ENV=development
```

Run the app using the built-in Flask development server:
```bash
flask run --host=0.0.0.0
```

Now, configure a production WSGI server to serve the application.  piMonitor has been tested with Gunicorn.

### Features Coming Soon
* Split server code into modules to allow for easy modification and customization
* Add data monitoring functionality to allow for alerts when sensor values cross a predefined threshold
* Add email reporting functionality to share sensor data at a predefined interval
* Add support for multiple sensors on one client device
* Add native support for additional types of sensors
