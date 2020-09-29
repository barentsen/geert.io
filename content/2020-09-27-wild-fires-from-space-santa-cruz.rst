Wildfires From Space: Part I — The CZU Lightning Complex in the Santa Cruz Mountains
####################################################################################
:date: 2020-09-26 07:00
:author: Geert
:category: wildfires 
:slug: wildfires-from-space-santa-cruz-mountains-2020

The `CZU Lightning Complex <https://www.fire.ca.gov/incidents/2020/8/16/czu-lightning-complex-including-warnella-fire/>`_
in the Santa Cruz Mountains is one of several significant wild fires
which affected the US West Coast in recent weeks.
The fire started on August 16, 2020, and burned more than 80,000 acres over a period of several weeks.

To visualize the impact of the fire, I mosaicked two recent true-color images
taken from space by `ESA's Sentinel-2 satellite <https://sentinel.esa.int/web/sentinel/missions/sentinel-2>`_.
You can download high-resolution versions of these images
`here <|filename|/images/santa-cruz-mountains-2020jun03.png>`__
and `here <|filename|/images/santa-cruz-mountains-2020sep06.png>`__.


.. raw:: html

    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">These are the Santa Cruz Mountains near Silicon Valley, seen from space before &amp; after the recent <a href="https://twitter.com/hashtag/CaliforniaFires?src=hash&amp;ref_src=twsrc%5Etfw">#CaliforniaFires</a>.<br><br>Can you see the giant brown scar?<br><br>⬇️ June 3, 2020 vs Sept 6, 2020 ↘️ <a href="https://t.co/Y8nu6S9Jcn">pic.twitter.com/Y8nu6S9Jcn</a></p>&mdash; Geert Barentsen (@GeertHub) <a href="https://twitter.com/GeertHub/status/1309878200533618688?ref_src=twsrc%5Etfw">September 26, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


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
