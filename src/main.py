import requests
import json
import ast
from datetime import datetime
from color import color_from_image

def token():
    with open('token.json', 'r') as f:
        token_json = json.load(f)
    
    return token_json['token']
        
def new_album():
    res = requests.get('https://rest-drf.herokuapp.com/api/artist/update')
    
    if res.status_code != 200:
        print ('Failed to get song data form rest-drf')
        sendError(res.text)
        print (res.text)

    return ast.literal_eval(res.text)
    
def send(msg):
    
    TOKEN = token()

    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer ' + TOKEN
    }

    res = requests.post('https://slack.com/api/chat.postMessage', 
        headers = headers, 
        data = json.dumps(msg)
    )
    
    status = json.loads(res.text)['ok']

    if status:
        print ('Succeeded to send slack message')
    else:
        print ('Failed to send slack message.')
        print (json.loads(res.text))
        

def sendError(content):
    msg = {
        'channel': 'U02EED66CE9',
        'attachments': [
            {
                'mrkdwn_in': ['text'],
                'color': '#ff0000',
                'title': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'text': content,
                'footer': 'FLO',
                'footer_icon': 'https://www.music-flo.com/favicon.ico'
            }
        ]
    }
    
    send(msg)
        
if __name__ == '__main__':
    
    print (datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' | project running...')

    for album in new_album():
        msg = {
            'channel': 'U02EED66CE9',
            'attachments': [
                {
                    'mrkdwn_in': ['text'],
                    'color': color_from_image(album['image']),
                    'title': album['artist'] + ' - ' + album['title'],
                    'thumb_url': album['image'],
                    'fields': album['tracks'],
                    'footer': 'FLO',
                    'footer_icon': 'https://www.music-flo.com/favicon.ico'
                }
            ]
        }

        send (msg)
