import requests
import json

BASE_URL = 'https://www.music-flo.com/api/meta/v1'


params = {
    'sortType' : 'RECENT',
    'roleType' : 'ALL',
    'page' : '1'
}

def getAlbum(artist):
    
    result = {}
    
    while (True):
        res = requests.get (BASE_URL + artist['url'] + '/album', params = params)

        albums = json.loads(res.text)
    
        for item in albums['data']['list']:
            result['artist'] = artist['name']
            result['title'] = item['title']
            result['releaseYmd'] = item['releaseYmd']
            result['img'] = item['imgList'][5]['url']
            break;


        if (albums['data']['lastPageYn'] == 'Y'):
            break;
    
    return result