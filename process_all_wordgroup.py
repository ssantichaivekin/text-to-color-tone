'''
Get all word from the count_1w.txt
Process all of them using dictionary.get_pixel_list.py => gen_process
Get the matplotlib data (csv, hist) of the processed group and store them
in a seperate folder (just like what we did with other things) and then
write a function to take them from the folder and visualize them.
'''

import os

from dictionary.get_pixel_list import gen_process
from process.knn_process import get_clusters_from_pixel_list
from process.plot_utils import centroid_histogram
from writer.write_word import write_info
from process.get_color_tone import plot_clusters

def process_all_wordgroup(all_wordgroups, wordlist, targetpath) :
    '''
    Process all wordgroups specified in all_wordgroups.
    Save the csv, hist, and processed image to targetpath.
    '''

    for wordgroup in all_wordgroups :
        # calls dictionary.get_pixel_list => gen_process
        # to get the generator of the list we will use
        groupname, pixellist = gen_process(wordgroup, wordlist)
        print(groupname)
        # calls process.knn_process => get_clusters_from_pixel_list
        # to get a knn-cluster
        if len(pixellist) == 0 :
            continue
        clusters = get_clusters_from_pixel_list(pixellist)
        # calls process.plot_utils => centroid histogram
        # to get a hist from the cluster
        hist = centroid_histogram(clusters)
        # calls writer.write_info
        write_info(groupname, clusters.cluster_centers_, hist, targetpath)
        # calls process.get_color_tone => plot_clusters(title, clusters, img_paths, False, targetname) :
        targetname = targetpath + groupname + '.png'
        plot_clusters(groupname, clusters, None, False, targetname)


    

if __name__ == '__main__' :
    # get all_wordgroups and wordlist
    from dictionary.word_group_generator import all_groups
    # open/write the assets/wordgroup folder
    loc = os.path.abspath(__file__)
    # just strip everything but leave /
    os.chdir(loc.strip('process_all_wordgroup.py'))
    os.makedirs('./assets/wordgroup/', exist_ok=True)
    # call process_all_wordgroup to save the process
    from writer.segment_word import get_all_words

    wordlist = get_all_words()
    targetpath = './assets/wordgroup/'

    process_all_wordgroup(all_groups, wordlist, targetpath)

    print('success')