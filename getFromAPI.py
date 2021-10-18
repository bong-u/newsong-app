#!-*- coding: utf-8 -*-

import requests
import json

BASE_URL = 'https://www.music-flo.com/api/meta/v1'

ARTIST = {
    'name' : u'백예린 (Yerin Baek)',
    'url' : '/artist/80137177'
}

params = {
    'sortType' : 'RECENT',
    'roleType' : 'ALL',
    'page' : '1'
}

def getAlbum(artist):
    
    while (True):
        res = requests.get (BASE_URL + artist['url'] + '/album', params = params)

        data = json.loads(res.text)
    
        for item in data['data']['list']:
            print (item['title'].encode('utf-8'))
            print (item['releaseYmd'])
            print (item['imgList'][5]['url'])
            break;


        if (data['data']['lastPageYn'] == 'Y'):
            break;
    
    print (artist['name'].encode('utf-8'))
    print ('백예린');

print (u'안뇽')
getAlbum(ARTIST)