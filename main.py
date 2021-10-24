from src.sendMessage import send
from src.getFromAPI import getAlbums
import json
import os

JSON_PATH = os.path.join(os.getcwd(), 'json')

def getArtists():
    with open(JSON_PATH + '/ARTISTS.json', 'r') as f:
        artists = json.load(f)
        
    return artists

if __name__ == '__main__':
    artists = getArtists();
    
    for artist in artists:
        results = getAlbums(artist)
        
        for result in results:
            msg = {
                'channel': '',
                'attachments': [
                    {
                        'mrkdwn_in': ['text'],
                        'color': '#3f3fff',
                        'title': result['artist'] + ' - ' + result['title'],
                        'thumb_url': result['img'],
                        "fields": result['tracks'],
                        'footer': 'FLO',
                        'footer_icon': 'https://www.music-flo.com/favicon.ico'
                    }
                ]
            }
            send(msg)