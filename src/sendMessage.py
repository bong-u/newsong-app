import requests
import json

JSON_PATH = '../json/'

def getToken():
    with open(JSON_PATH + 'TOKEN.json', 'r') as f:
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
    print ('Sending status :', end=' ')
    print (json.loads(res.text)['ok'])

