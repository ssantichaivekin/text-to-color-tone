'''
From the thumbnails we obtain one list of pixels using
opencv2 color and numpy concatenation. Then we use the
KNN (K-nearest-neighbors) algorithm the find the colors
(that is, the color tone) that best represent all thumbnails.
'''

from numpy import concatenate
from sklearn.cluster import KMeans
import cv2

def read_image(img_path) :
    tempimage = cv2.imread(img_path, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(tempimage, cv2.COLOR_BGR2RGB)
    return image

def get_pixel_list(img_paths) :
    '''
    Read the images in image path and return one flatten list
    of pixels in those images.
    '''
    pixel_lists = []
    for img_path in img_paths :
        # Process the image using opencv's cv2 library
        image = read_image(img_path)
        # The image is now in np.ndarray form.
        # We then reshape it so that it is a flat list of
        # pixels.
        image_pixels = image.reshape((image.shape[0] * image.shape[1], 3))
        pixel_lists += [image_pixels]
    # Now we have a list of pixel lists. We that flatten those
    # lists into one list.
    pixel_list = concatenate(pixel_lists)
    return pixel_list

def get_clusters(pixel_list, num_clusters=5) :
    '''
    Get the KNN clusters from the pixel list.
    '''
    clusters = KMeans(n_clusters=num_clusters)
    clusters.fit(pixel_list)
    return clusters

def console_display_clusters(clusters) :
    '''
    Display the float/int values of the clusters.
    '''
    centers = clusters.cluster_centers_
    for i, center in zip(range(len(center)), center) :
        print("Center #",i, " == ", center)
        # note that the center's values are floats, not ints!
        center_integers = [int(p) for p in center]
        print("   and as ints:", center_integers)
    