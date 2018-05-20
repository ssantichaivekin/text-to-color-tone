'''
Define a function to download the images and return cv2 images.
These images can further be used by scikit KNN algorithm for further processing.
'''

import requests

def download_images(image_links, file_prefix='temp') :
    '''
    Download the thumbnail images to asset folder.
    Return the names of the file downloaded.
    '''
    imgnames = []
    for i, link in zip(range(len(image_links)), image_links) :
        r = requests.get(link)
        imgname = './assets/%s-%d.jpg' % (file_prefix, i)
        with open(imgname, 'wb') as f:
            f.write(r.content)
        imgnames += [imgname]
    return imgnames

if __name__ == '__main__' :
    # Driver function: Try to download 6 images for Groot.
    from get_image_links import get_image_links
    links = get_image_links('Groot')
    img_names = download_images(links)