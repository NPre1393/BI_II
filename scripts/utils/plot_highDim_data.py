import pandas as pd
import numpy as np
from sklearn.manifold import TSNE, LocallyLinearEmbedding, Isomap, MDS, SpectralEmbedding

import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

def plot_data(df, y, type):

    """
    Plotting components with different dimensionality reduction techniques
    """
    if type == "TSNE":
        # performs TSNE on both transformed data frames with 50 variables
        X_embedded = TSNE(n_components=2, perplexity=40, n_iter=500).fit_transform(df)
    elif type == "LLE":
        X_embedded = LocallyLinearEmbedding(n_components=2, n_neighbors=5, n_jobs=-1).fit_transform(df)
    elif type == "ISO":
        X_embedded = Isomap(n_components=2, n_neighbors=5, n_jobs=-1, neighbors_algorithm='kd_tree').fit_transform(df)
    elif type == "MDS":
        X_embedded = MDS(n_components=2, n_jobs=-1).fit_transform(df)
    elif type == "SPECT":
        X_embedded = SpectralEmbedding(n_components=2, n_jobs=-1, n_neighbors=5, affinity="nearest_neighbors").fit_transform(df)

    
    # get unique values for colormap
    unique = np.unique(y)
    colors = [plt.cm.jet(i/float(len(unique)-1)) for i in range(len(unique))]

    plt.figure(1)   

    # scatter plot every class (Walk, Tram etc.)
    for i, u in enumerate(unique):
        xi = [X_embedded[:,0][j] for j  in range(len(X_embedded[:,0])) if y[j] == u]
        yi = [X_embedded[:,1][j] for j  in range(len(X_embedded[:,0])) if y[j] == u]
        plt.scatter(xi, yi, c=colors[i], label=str(u))
    plt.legend(loc='upper right')
    plt.gca().set_title('{0} with two components'.format(type))
    plt.show()