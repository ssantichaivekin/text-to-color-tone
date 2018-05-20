'''
Defines a function that recieves a text and uses Google Image search API
to get the links of thumbnails. This function return a list of links to the
thumbnails.
'''

import requests
from bs4 import BeautifulSoup

def read_key(keyfilename='google-api-key.txt') :
    '''
    Read the Google API key from keyfilename.
    '''
    key = open(keyfilename).read()
    return key

def read_search_engine_id(keyfilename='google-engine-name.txt') :
    '''
    Read the custom search engine.
    '''
    key = open(keyfilename).read()
    return key

def get_image_links(query, image_num=6) :
    '''
    Get a list of thumbnail links using the google API
    key.
    '''
    key = read_key()
    engine_id = read_search_engine_id()
    s_type = 'photo'
    params = {
        # search query; the text to find color tone
        'q'         : query, 
        # Google API search engine ID
        'cx'        : engine_id,
        # Image size : small, medium, large, etc
        'imgSize'   : 'medium',
        # Image type : clipart, face, lineart, news, and photo.
        'imgType'   : 'photo',
        # Search type -- we are searching images
        'searchType': 'image',
        # 6 seems to be enough for finding color tone.
        'num'       : 6,
        # This is my Google API key.
        'key'       : key
        }
    link = 'https://www.googleapis.com/customsearch/v1'
    r = requests.get(link, params)
    thumbnail_links = []
    for search_item in r.json()['items'] :
        thumbnail_link = search_item['image']['thumbnailLink']
        # print(thumbnail_link)
        thumbnail_links += [thumbnail_link]
    return thumbnail_links
