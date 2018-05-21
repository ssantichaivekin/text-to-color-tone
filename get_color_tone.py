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
from knn_process import read_image
from knn_process import get_pixel_list
from knn_process import get_clusters
from plot_utils import get_bar
import matplotlib.pyplot as plt


def get_color_tone(text) :
    # Download images from text and get the image paths
    # img_paths are where the images are stored on the client.
    links = get_image_links(text)
    img_paths = download_images(links)

    # Read and process the images using Scikit's KNN.
    pixel_list = get_pixel_list(img_paths)
    # Get the KNN clusters. We are finding 5 clusters in the example.
    clusters = get_clusters(pixel_list, 5)

    # Plotting :
    color_tone_bar = get_bar(clusters)
    # Set the plot name
    plt.suptitle('Color tone of: %s' % text, fontsize = 16)

    # Plot color tone
    bottom_ax = plt.subplot(212)
    bottom_ax.imshow(color_tone_bar)

    # Example Picture 1
    ex_img0 = read_image(img_paths[0])
    upleft_ax = plt.subplot(221)
    upleft_ax.imshow(ex_img0)
    upleft_ax.axis('off')

    # Example Picture 2
    ex_img1 = read_image(img_paths[1])
    upright_ax = plt.subplot(222)
    upright_ax.imshow(ex_img1)
    upright_ax.axis('off')

    # Show the results on the screen
    plt.show()


if __name__ == '__main__' :
    # Try to get the color tone of the word "Snack" and "Groot"
    get_color_tone('Snack')
    get_color_tone('Groot')
    
