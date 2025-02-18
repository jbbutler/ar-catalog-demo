# Butler (2025?) AR Catalog
An (unpublished) catalog of atmospheric river events in Antarctica by James Butler, Michelle Maclennan, and Fernando Perez. This is a catalog of individual storm events tracked through space and time, constructed by spatiotemporally clustering AR pixels in the [Wille (2021)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020JD033788) Eulerian catalog.

## Algorithm Characteristics
- **Type:** Condition and Track
- **Geometry Requirement:** Same as [Wille (2021)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020JD033788). Spatial neighborhood size of 500km for searching for candidate AR pixels for a particular event at a particular time. Defined as AR landfall if tracked AR object's pixels intersect the Antarctic Ice Sheet at any point in its lifetime.
- **Threshold Requirement:** 98th percentile of monthly, pixelwise vIVT
- **Temporal Requirement:** Time slice and stitching. Time window of 18 hours to search for candidate AR pixels for a particular storm event.
- **Region:** Antarctic ($39^{\circ}$- $86^{\circ}$ S)
- **DIO/Reference:** *TBD*
