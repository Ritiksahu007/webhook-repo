from datetime import datetime

def format_event(event):
    time_str = event['timestamp'].strftime('%d %B %Y - %I:%M %p UTC')
    if event['event_type'] == 'push':
        return f"{event['author']} pushed to {event['to_branch']} on {time_str}"
    elif event['event_type'] == 'pull_request':
        return f"{event['author']} submitted a pull request from {event['from_branch']} to {event['to_branch']} on {time_str}"
    elif event['event_type'] == 'merge':
        return f"{event['author']} merged branch {event['from_branch']} to {event['to_branch']} on {time_str}"
    else:
        return "Unknown event"