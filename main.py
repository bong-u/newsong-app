from sendMessage import send
from getFromAPI import getAlbums
import json

def getArtists():
    with open('ARTISTS.json', 'r') as f:
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
                        'author_name': result['artist'],
                        'title': result['title'],
                        'thumb_url': result['img'],
                        "fields": result['tracks'],
                        'footer': 'FLO',
                        'footer_icon': 'https://www.music-flo.com/favicon.ico'
                    }
                ]
            }
            send(msg)