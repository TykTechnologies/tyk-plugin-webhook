import json, requests

target_url = 'http://httpbin.org/post'

def trigger_webhook(payload):
    requests.post(target_url, json=payload)
