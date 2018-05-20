'''
A file from Python tutorial
  OpenCV and Python K-Means Color Clustering
  Adrian Rosebrock
  May 26, 2014 

Also used in CS35 class.
link: https://www.pyimagesearch.com/2014/05/26/opencv-python-k-means-color-clustering/
'''

import numpy as np
import cv2
import matplotlib.pyplot as plt

def centroid_histogram(clt):
	# grab the number of different clusters and create a histogram
	# based on the number of pixels assigned to each cluster
	numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
	(hist, _) = np.histogram(clt.labels_, bins = numLabels)

	# normalize the histogram, such that it sums to one
	hist = hist.astype("float")
	hist /= hist.sum()

	# return the histogram
	return hist

def plot_colors(hist, centroids):
	# initialize the bar chart representing the relative frequency
	# of each of the colors
	bar = np.zeros((50, 300, 3), dtype = "uint8")
	startX = 0

	# loop over the percentage of each cluster and the color of
	# each cluster
	for (percent, color) in zip(hist, centroids):
		# plot the relative percentage of each cluster
		endX = startX + (percent * 300)
		cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
			color.astype("uint8").tolist(), -1)
		startX = endX
	
	# return the bar chart
	return bar

'''
The following part is written by me, adpated from the tutorial.
'''

def get_bar(clusters) :
	'''
	Use matplotlib to plot the scikit-knn clusters.
	'''
	hist = centroid_histogram(clusters)
	bar = plot_colors(hist, clusters.cluster_centers_)
	return bar
