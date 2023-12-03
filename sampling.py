import numpy as np
import graphlearning as gl

# Sample N points from the image array at random
def sample(im_array, N=5000, normalize=True):
    u = im_array.nonzero()
    if normalize:
        im_normal = (u[0] / im_array.shape[0], u[1] / im_array.shape[1])
    else:
        im_normal = (u[0], u[1])
    im_nonzero = np.array(list(map(list, zip(*im_normal)))) # nonzero points in the area
    y = im_nonzero[np.random.choice(im_nonzero.shape[0], N, replace=False), :]
    return y

# Compute Graph Fourier Transform
def GFT(im_points, k=25, r=1000):
    # im_points is sampled points from image, k is number of neighbors, r is number of eigenvalues
    W = gl.weightmatrix.knn(im_points, k)
    G = gl.graph(W)
    print("Graph is connected: ", G.isconnected())
    return G.eigen_decomp(k=r, normalization='normalized', method="lowrank")

def CLGFT(im_points, k=25, r=1000, alpha=1.0):
    W = gl.weightmatrix.knn(im_points, k)
    G = gl.graph(W)
    D = G.degree_matrix(p=-alpha)
    W = D * G.weight_matrix * D
    G_coifman = gl.graph(W)
    print("Graph is connected: ", G_coifman.isconnected())
    return G_coifman.eigen_decomp(k=r, normalization='randomwalk', method="lowrank")


