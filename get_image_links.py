'''
Defines a function that recieves a text and uses Google Image search API
to get the links of thumbnails. This function return a list of links to the
thumbnails.
'''

import requests

def read_key(keyfilename='google-api-key.txt') :
    '''
    Read the Google API key from keyfilename.
    '''
    key = open(keyfilename).read()
    return key

def get_image_links(key, image_num=6) :
    '''
    Get a list of thumbnail links using the google API
    key.
    '''
    param = {}
