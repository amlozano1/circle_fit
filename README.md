circle_fit
==========

Small python library to fit a circle given a list of data points. 
Useful if you don't have access to numpy/scipy and just need something quick.
Based on Algorithm 1 From http://www.spaceroots.org/documents/circle/circle-fitting.pdf
Finding the circle that best fits a set of points by L. Maisonobe

Examples
```
from circle_fit import fit_center, fit_radius, fit_circle

points = [ (30,68), (50,-6), (110, -20), (35, 15), (45, 97)]
center = fit_center(points)
radius = fit_radius(points)

center2, radius2 = fit_circle(points)
```