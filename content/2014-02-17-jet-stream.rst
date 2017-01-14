Annual variations in the jet stream (video)
###########################################
:date: 2014-02-17 10:00
:author: Geert
:category: climate
:slug: variations-in-the-jet-stream

The weather has been unusual in the past two months:
extremely wet and windy in the UK
whilst very cold and snowy in the United States.
Such large-scale weather patterns are naturally linked
to variations in the global atmospheric circulation.
It is hence no surprise that there is much talk in the media
about the so-called *jet stream*,
which refers to the very strong winds
which circle our planet at an altitude of about 10 km.

To get a better idea of what the jet stream looks like and how it varies,
I hacked together a tiny Python module called `jetstream.py`_ to visualise
the average position and strength of the jet stream in different months
based on global circulation models. 
The result looks like this:

.. raw:: html

    <iframe width="640" height="360" src="http://www.youtube.com/embed/OGbDihkcvEE?feature=player_embedded" frameborder="0" allowfullscreen></iframe>

The data shown originates from the `ECMWF ERA re-analysis model`_,
which does not offer data for January or February 2014 yet
(hence the video focuses on December).
I cannot offer an interesting interpretation about this animation
at present, I was just curious to look at the data.

If you spot something interesting in this video, please leave a comment below.


.. _jetstream.py: https://www.github.com/barentsen/jetstream.py
.. _ECMWF ERA re-analysis model: http://www.ecmwf.int/research/era/do/get/era-interim
