
==================
Leonardo Watermark
==================

Add watermark templatetag - https://pypi.org/project/django-watermark/.

.. contents::
    :local:

Installation
------------

.. code-block:: bash

    pip install leonardo-watermark

Usage
-----

{% load watermark %}
{{ image_url|watermark:"The Watermark,position=R,opacity=10,rotation=45" }}

Read More
---------

* https://github.com/django-leonardo/django-leonardo
* https://pypi.org/project/django-watermark/
