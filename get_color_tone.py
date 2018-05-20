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
from knn_process import get_pixel_list
from knn_process import get_clusters
from plot_utils import get_bar
import matplotlib.pyplot as plt


def get_color_tone(text) :
    links = get_image_links(text)
    img_paths = download_images(links)
    pixel_list = get_pixel_list(img_paths)
    clusters = get_clusters(pixel_list, 6)
    bar = get_bar(clusters)
    plt.suptitle('Color tone of: %s' % text, fontsize = 16)
    bottom_ax = plt.subplot(212)
    bottom_ax.imshow(bar)
    bottom_ax = plt.subplot(221)
    bottom_ax.imshow(bar)
    bottom_ax.axis('off')
    bottom_ax = plt.subplot(222)
    bottom_ax.imshow(bar)
    bottom_ax.axis('off')
    plt.show()




if __name__ == '__main__' :
    # Try to get the color tone of the word "Snack"
    get_color_tone('Snack')
    get_color_tone('Groot')
    
