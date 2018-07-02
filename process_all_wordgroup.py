'''
Get all word from the count_1w.txt
Process all of them using dictionary.get_pixel_list.py => gen_process
Get the matplotlib data (csv, hist) of the processed group and store them
in a seperate folder (just like what we did with other things) and then
write a function to take them from the folder and visualize them.
'''

def process_all_wordgroup(all_wordgroups, wordlist, targetpath) :
    '''
    Process all wordgroups specified in all_wordgroups.
    Save the csv, hist, and processed image to targetpath.
    '''

    # calls dictionary.get_pixel_list => gen_process
    # to get the generator of the list we will use

    # calls process.knn_process => get_clusters_from_pixel_list
    # to get a knn-cluster

    # calls process.plot_utils => centroid histogram
    # to get a hist from the cluster

    # calls write_info
    # calls process.get_color_tone => plot_clusters(clusters, img_paths, False, targetname) :

    

if __name__ == '__main__' :
    # get all_wordgroups and wordlist

    # open/write the assets/wordgroup folder

    # call process_all_wordgroup to save the process