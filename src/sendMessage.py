import requests
import json
import os
from datetime import datetime

JSON_PATH = os.path.abspath('flo-reminder/json')

def getToken():
    with open(JSON_PATH + '/TOKEN.json', 'r') as f:
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
    
    # print (res.text)
    print (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), end=' | ')
    print ('Sending status :', end=' ')
    print (json.loads(res.text)['ok'])

