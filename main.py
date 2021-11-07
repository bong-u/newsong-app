from src.sendMessage import send
from src.getFromAPI import getAlbums
from src.getDomColor import getColor
import json
from src.path import ARTIST_PATH

def getArtists():
    with open(ARTIST_PATH, 'r') as f:
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
                        'color': getColor (result['img']),
                        'title': result['artist'] + ' - ' + result['title'],
                        'thumb_url': result['img'],
                        "fields": result['tracks'],
                        'footer': 'FLO',
                        'footer_icon': 'https://www.music-flo.com/favicon.ico'
                    }
                ]
            }
            
            send(msg)
