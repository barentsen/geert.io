Wildfires From Space: Part III — The Bobcat Fire near Los Angeles
#################################################################
:date: 2020-10-15 07:00
:author: Geert
:category: wildfires 
:slug: wildfires-from-space-bobcat-fire-2020

The `Bobcat Fire <https://www.fire.ca.gov/incidents/2020/9/6/bobcat-fire/>`_
just north of Los Angeles one of the numerous wild fires
which affected the US West Coast in recent weeks.
The fire started on September 6th, 2020, and burned more than 110,000 acres.

To visualize the impact of the fire, I mosaicked two recent true-color images
taken from space by `ESA's Sentinel-2 satellite <https://sentinel.esa.int/web/sentinel/missions/sentinel-2>`_.
You can download high-resolution versions of these images
`here <|filename|/images/los-angeles-from-space-2020aug31.jpg>`__
and `here <|filename|/images/los-angeles-from-space-2020sep30.jpg>`__.

.. raw:: html

    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">This is Los Angeles, seen from space before &amp; after the start of the <a href="https://twitter.com/hashtag/BobcatFire?src=hash&amp;ref_src=twsrc%5Etfw">#BobcatFire</a>. 🔥<br><br>Can you spot the giant brown fire scar in the hills north of the city?<br><br>⬇️ Aug 31 vs Sep 30 ↘️ <a href="https://t.co/JsiLkEe4B5">pic.twitter.com/JsiLkEe4B5</a></p>&mdash; Geert Barentsen (@GeertHub) <a href="https://twitter.com/GeertHub/status/1316766471180046338?ref_src=twsrc%5Etfw">October 15, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


Image details
-------------

Both images were taken by ESA's Copernicus Sentinel-2 satellite and turned into cloud-free mosaics using Google's `Earth Engine <https://earthengine.google.com/>`_ platform.
You can recreate the second image using the following Earth Engine script:

.. code-block:: javascript
  :linenos:

  var mosaic = ee.ImageCollection('COPERNICUS/S2_SR')
      .filterBounds(geometry)
      .filterDate('2020-09-30', '2020-10-01')
      .sort('CLOUDY_PIXEL_PERCENTAGE', false)
      .mosaic()
      .clip(geometry);

  var params = {bands: ['TCI_R', 'TCI_G', 'TCI_B'],
                min: 0.0,
                max: [250, 250, 250],
                gamma: [1.45, 1.45, 1.45]
  };

  Map.addLayer(mosaic, params, 'mosaic');
