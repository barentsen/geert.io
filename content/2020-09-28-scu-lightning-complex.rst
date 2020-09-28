Wildfires From Space: Part II — The SCU Lightning Complex near San Jose
#######################################################################
:date: 2020-09-28 07:00
:author: Geert
:category: wildfires 
:slug: wildfires-from-space-scu-lightning-complex-2020

The `SCU Lightning Complex <https://www.fire.ca.gov/incidents/2020/8/18/scu-lightning-complex/>`_
east of San Jose is one of several significant wild fires
which affected the US West Coast in recent weeks.
The fire started on August 16, 2020, and burned nearly 400,000 acres over a period of several weeks.

To visualize the impact of the fire, I mosaicked two recent true-color images
taken from space by `ESA's Sentinel-2 satellite <https://sentinel.esa.int/web/sentinel/missions/sentinel-2>`_.
You can download high-resolution versions of these images
`here <|filename|/images/scu-lightning-complex-before-2020jun03.jpg>`__
and `here <|filename|/images/scu-lightning-complex-after-2020sep06.jpg>`__.


.. raw:: html

    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">This is the Bay Area east of San Jose in California, seen from space before &amp; after the recent <a href="https://twitter.com/hashtag/wildfires?src=hash&amp;ref_src=twsrc%5Etfw">#wildfires</a>.<br><br>Unprecedented fires have turned 300,000 football fields of nature into a giant brown scar. The images are 70 miles wide!<br><br>⬇️ Jun 3, 2020 vs Sep 6, 2020 ↘️ <a href="https://t.co/mFODtGrZOA">pic.twitter.com/mFODtGrZOA</a></p>&mdash; Geert Barentsen (@GeertHub) <a href="https://twitter.com/GeertHub/status/1310723653198163968?ref_src=twsrc%5Etfw">September 28, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


Image details
-------------

Both images were taken by ESA's Copernicus Sentinel-2 satellite and turned into cloud-free mosaics using Google's fabulous `Earth Engine <https://earthengine.google.com/>`_ platform.
You can recreate the image for September 6th using the following Earth Engine script:

.. code-block:: javascript
  :linenos:

  var mosaic = ee.ImageCollection('COPERNICUS/S2_SR')
      .filterBounds(geometry)
      .filterDate('2020-09-05', '2020-09-07')
      .sort('CLOUDY_PIXEL_PERCENTAGE', false)
      .mosaic()
      .clip(geometry);

  var params = {bands: ['TCI_R', 'TCI_G', 'TCI_B'],
                min: 0.0,
                max: [250, 250, 250],
                gamma: [1.45, 1.45, 1.45]
  };

  Map.addLayer(mosaic, params, 'mosaic');
