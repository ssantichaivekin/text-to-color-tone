'''
Defines a function that recieves a text and uses Google Image search API
to get the links of thumbnails. This function return a list of links to the
thumbnails.
'''

import requests
import json
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
    print('Loading image:', query)
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
        # This is my Google API key.
        'key'       : key
        }
    link = 'https://www.googleapis.com/customsearch/v1'
    r = requests.get(link, params)
    thumbnail_links = []
    json_data = r.json()
    with open('assets/jsons/%s-google-query.json' % query, 'w') as f:
        json.dump(json_data, f)
    for search_item in json_data['items'] :
        thumbnail_link = search_item['image']['thumbnailLink']
        # print(thumbnail_link)
        thumbnail_links += [thumbnail_link]
    thumbnail_links = thumbnail_links[:image_num]
    return thumbnail_links

if __name__ == '__main__' :
    # This test case prints links for thumbnails of "Dogs" and "Independence Day".
    print('Dogs:')
    print(*get_image_links('Dogs'), sep='\n')
    print('Independence Day:')
    print(*get_image_links('Independence Day'), sep='\n')
