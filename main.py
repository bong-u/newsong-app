from sendMessage import send
from getFromAPI import getAlbums

if __name__ == '__main__':
    artists = [
        {
            'name' : '백예린 (Yerin Baek)',
            'url' : '/artist/80137177'
        }
    ]
    
    for artist in artists:
        result = getAlbums(artist)
    
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