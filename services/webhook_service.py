import requests

def send_webhook_notification(url, data):
    """Sends notifications when proposals are updated."""
    headers = {"Content-Type": "application/json"}
    requests.post(url, json=data, headers=headers)
