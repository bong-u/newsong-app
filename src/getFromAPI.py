import requests
import json
import os

BASE_URL = 'https://www.music-flo.com/api/meta/v1'
JSON_PATH = os.path.join(os.getcwd(), 'json')

params = {
    'sortType' : 'RECENT',
    'roleType' : 'RELEASE',
    'page' : '1',
    'size' : '3'
}

def UpdateArtists(recent):
    artists = {}
    
    with open(JSON_PATH + '/ARTISTS.json', 'r') as f:
        artists = json.load(f)
        
    for artist in artists:
        if artist['name'] == recent['name']:
            artist['recent'] = recent['recent']
            
    with open(JSON_PATH + '/ARTISTS.json', 'w', encoding = 'utf8') as f:
        json.dump(artists, f, indent=4, ensure_ascii=False)
        
    return artists

def getAlbums(artist):
    
    results = []
    recent = {}
    
    res = requests.get (BASE_URL + artist['url'] + '/album', params = params)

    albums = json.loads(res.text)
    
    for n, item in enumerate(albums['data']['list']):
        result = {}
        
        if n == 0:
            recent = {
                'name' : artist['name'],
                'recent' : item['id']
            }
        
        if artist['recent'] == item['id']: break;
        
        result['artist'] = artist['name']
        result['title'] = item['title']
        result['releaseYmd'] = item['releaseYmd']
        result['img'] = item['imgList'][4]['url']
        result['tracks'] = getTracks (str(item['id']), artist['name'])
        
        results.append (result)
        
    UpdateArtists (recent)
    
    return results

def getTracks(album, artistName):
    
    result = []
    
    res = requests.get (BASE_URL + '/album/' + album + '/track')
    
    tracks = json.loads (res.text)
    
    for n, item in enumerate(tracks['data']['list']):
        artists = []
        
        for artist in item['artistList']:
            artists.append (artist['name'])
        
        value = '{0}. {1} - {2}'.format (str(n+1), item['name'], ', '.join(artists))
        
        result.append ({'value' : value})
    
    return result
    