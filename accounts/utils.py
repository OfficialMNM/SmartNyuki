import requests
import json, os

def send_push_notification(token, title, body):
    server_key = 'BPNsumvdyu5y1tjNslXq5iGDBC6AI_6DRN8EiZVn7UOFLxpp_npNfqNIMEReBIvmdmFBl2EnMJANLsU_LIELOsc'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'key={server_key}',
    }
    payload = {
        'notification': {
            'title': title,
            'body': body,
        },
        'to': token,
    }
    response = requests.post('https://fcm.googleapis.com/fcm/send', headers=headers, data=json.dumps(payload))
    print('Notification sent:', response.json())

def absAppPath(*args):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(BASE_DIR, *args)