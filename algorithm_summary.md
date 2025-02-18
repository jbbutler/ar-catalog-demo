# How ARs are Detected

In [Wille (2021)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020JD033788), Antarctic ARs are detected on a pixelwise basis, where a pixel is considered part of an AR if the poleward integrated vapor transport (as derived from MERRA-2) is higher than the 98th percentile of that pixel location's vIVT data across all years for that particular month. The equation for poleward integrated vaport transport is shown below.

:::{equation}
:align: center

vIVT = -\frac{1}{g}\int_{sfc}^{top} qvdp

:::
