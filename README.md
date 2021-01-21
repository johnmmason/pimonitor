# pimonitor
A simple service for collecting, storing, and sharing sensor data.

### Project Overview

Convenience and peace-of-mind are often cited as primary reasons for bringing IOT sensors into the home.  In the past few years, the consumer market has been flooded with a variety of internet-connected home gadgets which aim to make it *as easy as possible* to turn your home into a "smart home".  However, many electronics and computer hobbyists find these products lacking in key areas.  For example,

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

### Setup and Installation

This section coming soon.

### Features Coming Soon

* Upload current client code (coming extremely soon)
* Finish server setup instructions
* Split server code into modules to allow for easy modification and customization
* Add data monitoring functionality to allow for alerts when sensor values cross a predefined threshold
* Add email reporting functionality to share sensor data at a predefined interval
* Add support for multiple sensors on one client device
* Add native support for additional types of sensors
