# Script containing functions to display the catalog.
#
# Jimmy Butler, September 2024


import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def construct_thumbnail(storm):
    '''
    Function that takes in a single AR's binary DataArray mask, and returns a thumbnail
    of what the AR looked like at the point of its greatest pixel-wise extent.
    Helper function for 'display_catalog' below.
    '''

    rep_time = storm.sel(time=storm.sum(dim=['lat', 'lon']).idxmax())
    fig, ax = plt.subplots(1)
    ax.imshow(rep_time.to_numpy());
    ax.invert_yaxis()
    ax.axis('off');
    fig.set_size_inches((0.5,0.5))
    plt.close()

    # using strategy from this StackExchange, which stores the thumbnails in an in-memory buffer,
    # and converts to base64 in the HTML
    # https://stackoverflow.com/questions/47038538/insert-matplotlib-images-into-a-pandas-dataframe
    bytes_file = BytesIO()
    fig.savefig(bytes_file, format='png', pad_inches=0, bbox_inches='tight')
    bytes_file.seek(0)
    figdata_png = base64.b64encode(bytes_file.getvalue()).decode()
    image_html = '<img src="data:image/png;base64,{}" />'.format(figdata_png)

    return image_html


def display_catalog(catalog_df, nrows=None):
    '''
    Function that takes in the catalog dataframe, and displays a desired number of rows of the catalog.

    Inputs:
        catalog_df (pandas.DataFrame): a DataFrame with a column of xArray binary DataArrays labelled 'data_array'
        nrows (int): the number of rows, from the top of the catalog, that you wish to print

    Outputs:
        The catalog, but styled so that it can be printed/read in a Jupyter notebook
    '''
    if nrows:
        return catalog_df.head(nrows).style.format({'data_array': lambda x: construct_thumbnail(x)})
    else:
        return catalog_df.style.format({'data_array': construct_thumbnail})