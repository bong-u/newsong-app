import requests
import json

def getToken():
    with open('TOKEN.json') as f:
        token_json = json.load(f)
        
    return token_json['token']

def send(msg):
    
    msg['channel'] = '#new-song'
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

