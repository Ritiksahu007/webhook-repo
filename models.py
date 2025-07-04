from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")  
db = client['webhook_db']
collection = db['events']

def save_event(event_type, data):
    if event_type == 'push':
        author = data['pusher']['name']
        to_branch = data['ref'].split('/')[-1]
        event = {
            "event_type": "push",
            "author": author,
            "from_branch": None,
            "to_branch": to_branch,
            "timestamp": datetime.utcnow()
        }
    elif event_type == 'pull_request':
        pr = data['pull_request']
        event = {
            "event_type": "pull_request",
            "author": pr['user']['login'],
            "from_branch": pr['head']['ref'],
            "to_branch": pr['base']['ref'],
            "timestamp": datetime.utcnow()
        }
    elif event_type == 'merge':  
        event = {
            "event_type": "merge",
            "author": data['sender']['login'],
            "from_branch": data['pull_request']['head']['ref'],
            "to_branch": data['pull_request']['base']['ref'],
            "timestamp": datetime.utcnow()
        }
    else:
        return  # Ignore other types

    collection.insert_one(event)

def get_recent_events(limit=10):
    return list(collection.find().sort("timestamp", -1).limit(limit))