Mapping the Milky Way's dust
#############################
:date: 2014-06-03 08:00
:author: Geert
:category: astronomy
:slug: iphas-3d-extinction-map

In recent months, my colleagues and I have been working very hard
on compiling a massive catalogue
which details the position and brightness of roughly 200 million stars
located in the northern part of the Milky Way.
The catalogue is based on a huge set of images 
which we collected as part of the `IPHAS survey`_
using the `Isaac Newton Telescope`_ in La Palma.
The data set contains 1.6 TB of compressed FITS images!


Although the paper which describes the new catalogue
is still under peer-review,
our first major result already `appeared on the arXiv today`_.
Using a probabilistic graphical model,
Stuart Sale (Oxford) and collaborators used the catalogue
to estimate the distance and extinction
towards 38 million stars.
The result of this effort is a 3D map of extinction (i.e. interstellar dust)
across the Northern Galactic Plane:

.. figure:: |filename|/images/2014-iphas-extinction-map.gif
   :alt: 3D extinction map.
   :target: |filename|/images/2014-iphas-extinction-map.gif

   A 3D extinction map of the Northern Galactic Plane based on IPHAS data. (Animation: S. Sale)

The new IPHAS catalogue is particularly well suited for this task,
because it provides narrow-band H-alpha photometry
for stars down to ~20th magnitude.
When this data is combined with the IPHAS broad-band magnitudes (Sloan r/i),
it yields a good proxy for the intrinsic brightness and colour of each star
(which in turn is key to obtaining distance and extinction estimates).
In effect, H-alpha photometry is the cheapest-imaginable
method to carry out a spectroscopic survey.

To learn more about the project, visit the fancy new website
for the `IPHAS survey`_ which I created recently.

.. _Isaac Newton Telescope: http://www.ing.iac.es/Astronomy/telescopes/int/
.. _IPHAS survey: http://www.iphas.org
.. _appeared on the arXiv today: http://arxiv.org/abs/1406.0009