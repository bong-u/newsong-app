import requests
import json

BASE_URL = 'https://www.music-flo.com/api/meta/v1'
ARTIST = '/artist/80137177'

params = {
    'sortType' : 'RECENT',
    'roleType' : 'RELEASE',
    'page' : '1'
}

def getAlbum():
    with requests.session() as s:
        res = s.get (BASE_URL + ARTIST + '/album', params = params)

        data = json.loads(res.text)
    
        for item in data['data']['list']:
            print (item['title'])
            print (item['releaseYmd'])

        print (data['data']['lastPageYn'])
        print (data['data']['totalCount'])
        
getAlbum()