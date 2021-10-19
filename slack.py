import requests
import json

def getToken():
    with open('TOKEN.json') as f:
        token_json = json.load(f)
        
    return token_json['token']

def sendMessage(): 
    
    SLACK_TOKEN = 'xoxb-2486712878006-2629452021185-LXQ4mYi8YCpO7VlUCHmZXTYH'
    CHANNEL_ID = 'C02J4R8E6AX'
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': 'Bearer ' + SLACK_TOKEN
    }
    
    payload = {
        'channel': '#new-song',
        'text': 'test'
    }
    
    res = requests.post('https://slack.com/api/chat.postMessage', 
        headers = headers, 
        data = json.dumps(payload)
    )
    
    print (res.text)

token = getToken()
print (token)
sendMessage()
