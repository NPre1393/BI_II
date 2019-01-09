import pandas as pd
import numpy as np
from sklearn.manifold import TSNE, LocallyLinearEmbedding, Isomap, MDS, SpectralEmbedding

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
matplotlib.style.use('ggplot')

def plot_data(df, y, type, components=2):

    """
    Plotting components with different dimensionality reduction techniques
    """
    if type == "TSNE":
        # performs TSNE on both transformed data frames with 50 variables
        X_embedded = TSNE(n_components=components, perplexity=40, n_iter=500).fit_transform(df)
    elif type == "LLE":
        X_embedded = LocallyLinearEmbedding(n_components=components, n_neighbors=5, n_jobs=-1).fit_transform(df)
    elif type == "ISO":
        X_embedded = Isomap(n_components=components, n_neighbors=5, n_jobs=-1, neighbors_algorithm='kd_tree').fit_transform(df)
    elif type == "MDS":
        X_embedded = MDS(n_components=components, n_jobs=-1).fit_transform(df)
    elif type == "SPECT":
        X_embedded = SpectralEmbedding(n_components=components, n_jobs=-1, n_neighbors=5, affinity="nearest_neighbors").fit_transform(df)

    # get unique values for colormap
    unique = np.unique(y)
    colors = [plt.cm.jet(i/float(len(unique)-1)) for i in range(len(unique))]

    fig = plt.figure()   
    if components == 3:
    # scatter plot every class
        ax = fig.add_subplot(111, projection='3d')
        for i, u in enumerate(unique):
            xi = [X_embedded[:,0][j] for j  in range(len(X_embedded[:,0])) if y[j] == u]
            yi = [X_embedded[:,1][j] for j  in range(len(X_embedded[:,0])) if y[j] == u]
            zi = [X_embedded[:,2][j] for j  in range(len(X_embedded[:,0])) if y[j] == u]
            #plt.scatter(xi, yi, c=colors[i], label=str(u))
            ax.scatter(xi, yi, zi, c=colors[i], label=str(u))
    elif components == 2:
        for i, u in enumerate(unique):
            xi = [X_embedded[:,0][j] for j  in range(len(X_embedded[:,0])) if y[j] == u]
            yi = [X_embedded[:,1][j] for j  in range(len(X_embedded[:,0])) if y[j] == u]

            plt.scatter(xi, yi, c=colors[i], label=str(u))
    else: 
        raise ValueError('components not 2 or 3')

    plt.legend(loc='upper right')
    plt.gca().set_title('{0} with {1} components'.format(type, components))
    plt.show()