from flask import Flask, request, jsonify, render_template
from models import save_event, get_recent_events
from utils import format_event

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    event_type = request.headers.get('X-GitHub-Event')
    data = request.json

    if not data:
        return 'No payload received', 400

    try:
        save_event(event_type, data)
        return 'Webhook received', 200
    except Exception as e:
        return str(e), 500

@app.route('/events', methods=['GET'])
def get_events():
    events = get_recent_events()
    formatted = [format_event(e) for e in events]
    return jsonify(formatted)

if __name__ == '__main__':
    app.run(debug=True)