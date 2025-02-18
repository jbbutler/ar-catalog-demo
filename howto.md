# How to use the catalog

To follow along with this tutorial, you can either clone [this repository](https://github.com/jbbutler/AR-Catalog-Tutorial) and follow the provided instructions to run the `catalog_tutorial.ipynb` notebook, or directly access a cloud-hosted Jupyter notebook via [this binder link](https://mybinder.org/v2/gh/jbbutler/AR-Catalog-Tutorial/HEAD?labpath=catalog_tutorial.ipynb). Note that the `environment.yml` file found in the repository is crucial to loading up these hdf5 files; otherwise you may run into package conflicts.

First, we'll load up the packages we need to access the catalog in this tutorial.

```{code} python
import pandas as pd
import xarray as xr
import numpy as np
import os
from pathlib import Path
import xarray as xr
import matplotlib.pyplot as plt
from catalog_display import display_catalog
```
The catalog files are organized by year, from 1980 until 2022. Each year's file is an .hdf5 file, that, once loaded, consists of a `pandas.DataFrame`. Let's load up the storms from 2022, and take a look at the output. The following code block produces the image in [](#storm_df_example).

```{code} python
storms = pd.read_hdf('2022_storm_df.h5')
# first 10 storms of 2022
display_catalog(storms, 10)
```
:::{figure} .images/storm_df_example.png
:label: storm_df_example
:::

Each row of the DataFrame consists of an individual storm from that year, with a binary-valued `xarray.DataArray` mask containing the AR pixels associated with that storm in the `data_array` column, and an indicator of whether or not that storm made landfall over the AIS at any point in the `is_landfalling` column. Note, the `display_catalog` function is a custom function that behaves like `DataFrame.head()`, which shows the first $n$ many rows of the DataFrame, where in the `data_array` column we specifically show thumbnails of the footprint of the storm at the time of its greatest spatial extent.

Let's pick a storm and look at a slice of its `xarray.DataArray` at a particular time, as shown in [](#example_slice)

```{code} python
storms.data_array.iloc[37].isel(time=20).plot.imshow();
```
:::{figure} .images/example_slice.png
:label: example_slice
:::

Now you know how to load up the data and begin playing around and using it! Feel free to check out the repository mentioned above for more interactive examples of use cases of this catalog and its format.
