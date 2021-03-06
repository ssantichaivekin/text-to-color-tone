'''
This where the program should be run.
The program uses the Google API to get thumbnails
and obtain from the thumbnails color tone using
scikit's KNN algorithm.

The program also support command line arguments
using the argparse library.

Author: Santi Santichaivekin
'''

# The import statement is essentially the index of this app.

# Use Google API to find the image links
from downloader.get_image_links import get_image_links
# Use request to download images
from downloader.download_images import download_images
# Use opencv(cv2) to read images into np.ndarray image format
from process.knn_process import read_image
# Use opencv(cv2) to read images into np.ndarray single list format
from process.knn_process import get_pixel_list
# From the single list format, use Scikit's KNN to compute clusters
from process.knn_process import get_clusters_from_pixel_list
# From clusters, create a bar, which can be then converted to a plot
from process.plot_utils import get_bar

def get_clusters_from_text(text, num_links, num_clusters) :
    # Download images from text and get the image paths
    # img_paths are where the images are stored on the client.
    links = get_image_links(text, num_links)

    img_paths = download_images(links, text)

    # Read and process the images using Scikit's KNN.
    pixel_list = get_pixel_list(img_paths)
    # Get the KNN clusters. We are finding  clusters in the example.
    clusters = get_clusters_from_pixel_list(pixel_list, num_clusters)
    return clusters, img_paths

def plot_clusters(title, clusters, img_paths=None, show_on_screen=True, targetname=None) :
    import matplotlib.pyplot as plt

    # Plotting :
    color_tone_bar = get_bar(clusters)
    # Set the plot name
    plt.suptitle('Color tone of: %s' % title, fontsize = 16)

    # Plot color tone
    bottom_ax = plt.subplot(212)
    bottom_ax.imshow(color_tone_bar)

    if img_paths :
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
    if show_on_screen :
        plt.show()
    else :
        plt.savefig(targetname)


if __name__ == '__main__' :
    # Here defines the command-line options for the program
    import argparse
    parser = argparse.ArgumentParser(description='Obtain color tone image from text.')
    parser.add_argument('text', type=str, help='Text we use to find the color tone')
    text = vars(parser.parse_args())['text']
    clusters, img_paths = get_clusters_from_text(text, 8, 8)
    plot_clusters(text, clusters, img_paths)

    # for debug
    # import os
    # plot_clusters(clusters, img_paths, False, os.path.expanduser('~/Desktop/tree.png'))

    
