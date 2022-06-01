import requests
import json
import ast
from datetime import datetime
from color import color_from_image
import re

class App:
    __SLACK_TOKEN = ''
    __ID_API = ''
    __PW_API = ''
    __API_TOKEN = ''
    
    __updateList = []
    
    def __init__(self):
        self.__get_secret()

        artists = self.__get_artists()
        new_albums = []

        for artist in artists:
            new_albums += self.__get_recent_album (artist)

        for album in new_albums:
            message = {
                'channel': 'C02U2K2LX5Z',
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

            self.__send (message)
        
        
        self.__login_to_api()
        self.__update_api_db()
        
    
    def __get_secret(self):
        with open('token.json', 'r') as f:
            data_json = json.load(f)

        self.__SLACK_TOKEN = data_json['token']
        self.__ID_API = data_json['id']
        self.__PW_API = data_json['pw']

    def __get_artists(self):
        res = requests.get('https://rest-newsong.herokuapp.com/item')

        if res.status_code != 200:
            print ('Failed to get song data form rest-drf')
            self.__sendError(res.text)
            print (res.text)

        return ast.literal_eval(res.text)

    def __get_recent_album (self, artist):
        result = []
        needUpdate = False

        res = requests.get('https://www.music-flo.com/api/meta/v1/artist/'+ str(artist['id']) + '/album?sortType=RECENT&size=3&roleType=RELEASE')

        albums = json.loads(res.text)

        for album in albums['data']['list']:
            if artist['recent'] == album['id']:
                break
            
            needUpdate = True

            result.append({
                'artist' : re.sub(r'\([^)]*\)', '', artist['name']),
                'title' : album['title'],
                'releaseYmd' : album['releaseYmd'],
                'image' : album['imgList'][4]['url'],
                'tracks' : self.__get_tracks(str(album['id']), artist['name'])
            })
        
        if needUpdate:
            artist['recent'] = albums['data']['list'][0]['id']
            self.__updateList.append(artist)

        return result


    def __get_tracks(self, albumId, musicianName):
        albumId = str(albumId)

        result = []

        res = requests.get ('https://www.music-flo.com/api/meta/v1/album/' + albumId + '/track')

        tracks = json.loads (res.text)

        for n, item in enumerate(tracks['data']['list']):

            artists = []

            for musician in item['artistList']:
                artists.append (re.sub(r'\([^)]*\)', '', musician['name']))

            track = '{0} - {1} - {2}'.format (str(n+1), item['name'], ', '.join(artists))

            result.append ({'value' : track})

        return result

    def __send (self, message):
        
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': 'Bearer ' + self.__SLACK_TOKEN
        }

        res = requests.post('https://slack.com/api/chat.postMessage', 
            headers = headers, 
            data = json.dumps(message)
        )

        status = json.loads(res.text)['ok']

        if status:
            print ('Message sending success.')
        else:
            print ('Failed to send message.')
            print (json.loads(res.text))


    def __sendError(self, content):
        msg = {
            'channel': 'C02U2K2LX5Z',
            'attachments': [
                {
                    'mrkdwn_in': ['text'],
                    'color': '#ff0000',
                    'title': '[ERROR] '+datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'text': content,
                    'footer': 'FLO',
                    'footer_icon': 'https://www.music-flo.com/favicon.ico'
                }
            ]
        }

        self.__send(msg)
    
    def __login_to_api(self):
        res = requests.post('https://rest-newsong.herokuapp.com/login',
            data = {
                'username' : self.__ID_API,
                'password' : self.__PW_API
            }
        )
        
        self.__API_TOKEN = json.loads(res.text)['access_token']
        
    def __update_api_db(self):
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': 'Bearer ' + self.__API_TOKEN
        }
        
        for item in self.__updateList:
            print (item['name'] + ' updated')
            res = requests.put('https://rest-newsong.herokuapp.com/item',
                headers = headers,
                data = json.dumps (item)
            )
            
        
if __name__ == '__main__':
    
    print (datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' | project running...')
    
    app = App()
