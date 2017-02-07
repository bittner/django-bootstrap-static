Django Bootstrap Static Files
=============================

|bootstrap| |jquery| |fontawesome|

Bootstrap and optional Font Awesome static files ready for the picking.

Also ships the latest jQuery compatible with Bootstrap, for optional inclusion.

.. |bootstrap| image:: https://img.shields.io/badge/Bootstrap-v3.3.7-563d7c.svg
   :alt: Bootstrap
   :target: http://getbootstrap.com/getting-started/
.. |jquery| image:: https://img.shields.io/badge/jQuery-v3.1.1-0769ad.svg
   :alt: jQuery
   :target: http://getbootstrap.com/getting-started/
.. |fontawesome| image:: https://img.shields.io/badge/FontAwesome-v4.7.0-1c9a71.svg
   :alt: Font Awesome
   :target: http://fontawesome.io/get-started/

Install
-------

.. code-block:: bash

    pip install django-bootstrap-static

Configuration
-------------

To pickup Bootstrap static files, simply include ``'bootstrap'``, and optionally
``'fontawesome'``, in your ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = [
        # ...
        'bootstrap',
        'fontawesome',
    ]

Then you can include CSS and JavaScript as usual static resources, e.g. using
``{% static '...' %}`` in your base template as follows:

.. code-block:: django

    {% load static %}
    <head>
        <link rel="stylesheet" href="{% static 'bootstrap/css/bootstrap.min.css' %}">
        <link rel="stylesheet" href="{% static 'fontawesome/css/font-awesome.min.css' %}">
    </head>
    <body>
        ...
        <script src="{% static 'bootstrap/js/jquery.min.js' %}"></script>
        <script src="{% static 'bootstrap/js/bootstrap.min.js' %}"></script>
    </body>

More details on integration may be available from each of the two projects:

- http://getbootstrap.com/getting-started/
- http://fontawesome.io/get-started/

Contribution
------------

Occasionally, I forget to update this package with new bootstrap updates.
Please feel free to submit a PR.

Sources and Procedures
^^^^^^^^^^^^^^^^^^^^^^

Bootstrap: (all files from dist package)
    `Bootstrap website / Getting started`_ -> drop into ``bootstrap/static/``
jQuery: (compressed, uncompressed, map)
    `jQuery website / Download`_ -> rename and mix into ``bootstrap/static/js/``
Font Awesome: (``css/``, ``fonts/`` only)
    `Font Awesome website`_ ("No thanks, just download") -> drop into ``fontawesome/static/``

.. _Bootstrap website / Getting started: https://getbootstrap.com/getting-started/
.. _jQuery website / Download: http://jquery.com/download/
.. _Font Awesome website: http://fontawesome.io/

Releases
--------

To keep with the Bootstrap release schedule we will keep version numbers of
this app in sync with the bootstrap Major.Minor.Revision changes (`semver`_).
The additional version number will be added at the end to denote a new change
within this package itself.

``django-bootstrap-static==3.3.1.1`` == Bootstrap ``3.3.1`` with an additional
package change.

.. _semver: http://semver.org/
