# test
This Flask-based app receives GitHub webhook events from `action-repo`.

## Features
- Flask server to receive webhook payloads
- MongoDB to store event data
- Frontend polls every 15 seconds to show latest activity

## Technologies Used
- Python + Flask
- MongoDB
- HTML/CSS + JS for UI


This Flask app receives GitHub webhook events from `action-repo` and stores them in MongoDB. A simple UI polls every 15 seconds to show repo activity like Push, Pull Requests, and Merge (optional).