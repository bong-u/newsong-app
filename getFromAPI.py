import requests
import json

BASE_URL = 'https://www.music-flo.com/api/meta/v1'


params = {
    'sortType' : 'RECENT',
    'roleType' : 'ALL',
    'page' : '1'
}

def getAlbums(artist):
    
    result = {}
    
    while (True):
        res = requests.get (BASE_URL + artist['url'] + '/album', params = params)

        albums = json.loads(res.text)
    
        for item in albums['data']['list']:
            result['artist'] = artist['name']
            result['title'] = item['title']
            result['releaseYmd'] = item['releaseYmd']
            result['img'] = item['imgList'][5]['url']
            result['tracks'] = getTracks(str(item['id']))
            break;


        if (albums['data']['lastPageYn'] == 'Y'):
            break;
    
    return result

def getTracks(album):
    
    result = []
    
    res = requests.get (BASE_URL + '/album/' + album + '/track')
    
    tracks = json.loads(res.text)
    
    for n, item in enumerate(tracks['data']['list']):
        result.append ({'value' : str(n+1) + '. ' + item['name']})
    
    return result
    