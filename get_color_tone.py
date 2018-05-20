'''
This where the program should be run.
The program uses the Google API to get thumbnails
and obtain from the thumbnails color tone using
scikit's KNN algorithm.

Author: Santi Santichaivekin
Ideas: Christie Chan's MS project
'''

from get_image_links import get_image_links
from download_images import download_images

def get_color_tone(text) :
    links = get_image_links(text)
    img_names = download_images(links)
