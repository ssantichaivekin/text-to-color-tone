'''
Defines a function that a file that contains the color tone
of the information of a given word.
'''

from process.get_color_tone import get_clusters_from_text
# Note that the centroid histogram function just creates an
# np.array with values corresponding to the % of the appearance
# of that color
from process.plot_utils import centroid_histogram

import numpy as np

def write_info(name, centers, hist, folderpath) :
    filename = folderpath + text + '-centers.csv'
    np.savetxt(filename, centers, delimiter=',')
    filename = folderpath + text + '-hist.csv'
    np.savetxt(filename, hist, delimiter=',')

def save_info(text, folderpath='./assets/info/') :
    '''
    Print the detailed color tone information of the
    text to two seperate files in assets/info.
    '''
    # Get the centers of the cluster
    # This uses 8 top images and produces 8 clusters
    clusters, _ = get_clusters_from_text(text, 8, 8)
    centers = clusters.cluster_centers_
    hist = centroid_histogram(clusters)

    write_info(text, centers, hist, folderpath)

def bulk_save_info(textlist, folderpath='./assets/info/') :
    '''
    Run save info for each text in textlist.
    '''
    for text in textlist :
        save_info(text, folderpath)


if __name__ == '__main__' :
    save_info('hello')


