'''
From the thumbnails we obtain one list of pixels using
opencv2 color and numpy concatenation. Then we use the
KNN (K-nearest-neighbors) algorithm the find the colors
(that is, the color tone) that best represent all thumbnails.
'''

from numpy import concatenate
import cv2

def get_pixel_list(img_paths) :
    '''
    Read the images in image path and return one flatten list
    of pixels in those images.
    '''
    pixel_lists = []
    for img_path in img_paths :
        # Process the image using opencv's cv2 library
        image = cv2.imread(img_path, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # The image is now in np.ndarray form.
        # We then reshape it so that it is a flat list of
        # pixels.
        image_pixels = image.reshape((image.shape[0] * image.shape[1], 3))
        pixel_lists += [image_pixels]
    # Now we have a list of pixel lists. We that flatten those
    # lists into one list.
    pixel_list = concatenate(pixel_lists)
    return pixel_list
    