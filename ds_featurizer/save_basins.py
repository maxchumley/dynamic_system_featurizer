"""
Save the basin results as image files.
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.ticker as ticker
from ds_featurizer import config

def save_basins(basin, im_num, feat, extents, labels, system):
    """
    Save the basin results as image files.
    Args:
        basin -- n x n array of features
        im_num -- List containing image number and parameter row number
        feat -- List containing folder name and feature title
        extents -- Horizontal and vertical image extents for the basins and image size
        labels -- list containing strings to label the x and y axes
        system -- String containing the system name
    """
    
    # Set the plot fonts
    rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
    rc('text', usetex=True)
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    
    # Unpack the plot size parameters
    x_start, x_end, y_start, y_end, n_pixels = extents
    
    # Plot the image
    fig = plt.figure(figsize=(6, 5), dpi=200)
    image = plt.imshow(basin, origin='lower', aspect='auto',extent=[x_start, x_end, y_start, y_end])
    cbar = plt.colorbar(image, format=ticker.FuncFormatter(fmt), ticks=np.linspace(np.min(basin), np.max(basin),5))
    cbar.ax.tick_params(labelsize=15)
    plt.title(fr"[{n_pixels}$\times${n_pixels}] - {feat[1]}", fontsize=30, pad=20)
    plt.xlabel(labels[0], fontsize=30)
    plt.ylabel(labels[1], fontsize=30)
    plt.xticks(np.linspace(x_start, x_end, 5), fontsize=20)
    plt.yticks(np.linspace(y_start, y_end, 5), fontsize=20)
    plt.tight_layout()
    
    # Save the image into the proper folder
    path = os.path.join(os.getcwd(),os.path.join('Basin_'+system, feat[0]))
    path = os.path.join(path, str(im_num[0]+1))
    plt.savefig(path)
    plt.close(fig)
    
def fmt(x, pos):
    a, b = '{:.2e}'.format(x).split('e')
    b = int(b)
    return r'${} \times 10^{{{}}}$'.format(a, b)
    

