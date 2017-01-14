Footprint of the IPHAS Galactic Plane survey
############################################
:date: 2012-10-22 11:01
:author: Geert
:category: astronomy
:tags: IPHAS
:slug: iphas-footprint

As part of my post-doc at the University of Hertfordshire, I'm helping
to calibrate, release and exploit data obtained by the \ `INT
Photometric H-Alpha Survey`_ (IPHAS). This is a 1800
deg\ :sup:`2` optical survey of the Northern Galactic Plane, carried out
in the narrow-band Hα and broad-band Sloan r'/i' filters. I'll be
talking more about the survey in future posts, but as a warm-up I
produced this plot of the survey's 15270 telescope pointings:

.. figure:: |filename|/images/iphas_footprint.png
   :alt: Footprint of the IPHAS survey.
   :target: |filename|/images/iphas_footprint.png

   Footprint of the IPHAS survey.

Let me explain this footprint briefly. The survey uses the `Wide-Field
Camera`_ (WFC) at the 2.5-meter `Isaac Newton Telescope`_ (INT) in La
Palma. This camera consists of four thinned 2048 × 4096 pixel CCDs
arranged in an L shape like this:

.. figure:: |filename|/images/iphas_field1.png
   :alt: Footprint of a single IPHAS (WFC) exposure.
   :target: |filename|/images/iphas_field1.png

   Footprint of a single IPHAS (WFC) exposure.

The four CCDs provide a combined field of view of 0.3 deg\ :sup:`2`,
hence the minimum number of pointings required to cover the 1800
deg\ :sup:`2` survey area is 6000. However, the survey was designed to
provide a 5% overlap between adjacent fields to enable data quality and
calibration checks. As a result, the footprint contains a total of 7635
fields which partially overlap.

Furthermore, each field was paired with a so-called *offset field* at 5
arcmin West and South, to cover the narrow gaps between the CCD chips.
This explains the final number of 7635 x 2 = 15 270 pointings. When
their footprints are plotted using 30% opacity, a complicated sky
coverage pattern emerges. Whilst the majority of the sky is covered
twice, there are overlap areas which are covered three or four times
(dark patches) and narrow bands between CCD chips which are covered 
only once (brighter strips):

.. figure:: |filename|/images/iphas_local1.png
   :alt: IPHAS footprints.
   :target: |filename|/images/iphas_local1.png

   IPHAS footprints plotted with 30% opacity. The darkest overlap areas are covered four times, while the the narrow bands between CCD chips are exposed only once.

A tricky question which results from this coverage pattern is: \ **how
should the final source catalogue be generated?** Some objects are
observed four times, sometimes many years apart, whilst others are only
observed once. Should multiple exposures of a single object be averaged,
or should only the best exposure be adopted in the source catalogue?
Such tricky decisions have to be made for all surveys because
*telescopes don't make catalogues* (see `Hogg & Lang 2010`_.)

An obvious solution is to release both a catalogue of individual
detections on one hand, and a catalogue of averaged source properties on
the other hand (there has already been a fair bit of thinking and
discussion in this direction within the IPHAS team!)

Such catalogue releases should preferably be supplemented by scriptable
access to the calibrated pixel data, through image cut-outs, to enable
users to re-measure properties or fit models to the *actual pixel data*.
Is there a standard VO protocol for this? There is the `Simple Image
Access protocol`_, but is not quite designed for cut-outs!

How do you think surveys with a complicated sky coverage pattern should
generate their catalogues and make data available?

.. _INT Photometric H-Alpha Survey: http://www.iphas.org
.. _Wide-Field Camera: http://www.ing.iac.es/Astronomy/instruments/wfc/
.. _Isaac Newton Telescope: http://www.ing.iac.es/Astronomy/telescopes/int/
.. _Hogg & Lang 2010: http://arxiv.org/abs/1008.0738
.. _Simple Image Access protocol: http://www.ivoa.net/Documents/SIA/
