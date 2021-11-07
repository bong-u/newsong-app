import requests
import json
from datetime import datetime
from src.path import TOKEN_PATH

def getToken():
    with open(TOKEN_PATH, 'r') as f:
        token_json = json.load(f)
        
    return token_json['token']

def send(msg):
    
    msg['channel'] = 'U02EED66CE9'
    TOKEN = getToken()
    
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer ' + TOKEN
    }
    
    res = requests.post('https://slack.com/api/chat.postMessage', 
        headers = headers, 
        data = json.dumps(msg)
    )
    
    status = json.loads(res.text)['ok']

    print (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), end=' | ')
    print ('Sending status :', end=' ')
    print (status)

    if not status:
        print (json.loads(res.text))

