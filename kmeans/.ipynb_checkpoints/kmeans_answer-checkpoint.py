import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
import random
from sklearn import preprocessing

def calc_dist(dat, centroids):
    dist_mat = []
    val_mat = []
    for row in dat:
        lst = []
        for idx, centroid in enumerate(centroids):
            lst.append([idx, np.linalg.norm(row - centroid)])

        arr = np.array(lst)
        min_bucket = np.argmin(arr[:,1])
        min_val = np.min(arr[:,1])
        dist_mat.append(min_bucket)
        val_mat.append(min_val)
    return np.array(dist_mat), np.array(val_mat)

def init_kmeans(dat, k):

    rand_centroids = random.sample(range(len(dat)), k)

    iris_centroids = dat[rand_centroids]
    centroids_mean = iris_centroids

    dist, values = calc_dist(dat, centroids_mean)

    return dist

def new_centroids(dat,dist_mat, k):
    centroids = []
    for i in range(k):
        mask = dat[dist_mat == i]
        mean = np.mean(mask, axis = 0)
        centroids.append(mean)
    dist, values = calc_dist(dat, centroids)

    return dist

def num_iters(num, dat, k):
    for i in range(num):
        if i == 0:
            new_dist, values = init_kmeans(iris_dat, k)
            # return init_dist
        # elif i == 1:
        #     new_dist = new_centroids(iris_dat, new_dist, 10)
        else:
            new_dist, values = new_centroids(iris_dat, new_dist, k)
            # centroids = new_centroids(iris_dat, new_dist, 10)[1]
    return new_dist, values

def sse(val_mat, dat, k):
    dist = num_iters(100, dat, k)
    return np.sum(dist**2)


if __name__ == '__main__':

    #load in iris
    iris = datasets.load_iris()

    #get data only:
    iris_dat = iris.data

    # random.seed(42)
    for n in range(1000):
        dist = num_iters(n, iris_dat, 3)
        print(dist)

    # for n in range(10):


    #random sample:
    # plt.scatter(iris_dat[:, 0], iris_dat[:, 1])
    # plt.scatter(centroids[:, 0], centroids[:, 1], c='r', s=100)
