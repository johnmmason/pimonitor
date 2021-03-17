-- schema.sql

\c pimonitor;

CREATE TABLE home_data(
    id SERIAL,
    location VARCHAR(30),
    timestamp TIMESTAMP,
    temperature REAL,
    humidity real
);

CREATE TABLE api_keys (
    id SERIAL,
    hash VARCHAR(64) UNIQUE,
    app VARCHAR(10)
);
