'''
Get color tone from image--see description in process/get_color_tone
'''
from process.get_color_tone import *

if __name__ == '__main__' :
    # Here defines the command-line options for the program
    import argparse
    import os
    # add the assets folder :
    try :
        os.mkdir('./assets')
    except :
        pass
    # add a parser to parse text argument
    parser = argparse.ArgumentParser(description='Obtain color tone image from text.')
    parser.add_argument('text', type=str, help='Text we use to find the color tone')
    text = vars(parser.parse_args())['text']
    clusters, img_paths = get_clusters_from_text(text, 8, 8)
    plot_clusters(text, clusters, img_paths)