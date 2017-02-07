==============================================
Django Bootstrap Static Files |latest-version|
==============================================

|bootstrap| |jquery| |fontawesome|

Bootstrap and optional Font Awesome static files ready for the picking.

Also ships the latest jQuery compatible with Bootstrap, for optional inclusion.

.. |latest-version| image:: https://img.shields.io/pypi/v/django-bootstrap-static.svg
   :alt: Latest version on PyPI
   :target: https://pypi.python.org/pypi/django-bootstrap-static
.. |bootstrap| image:: https://img.shields.io/badge/Bootstrap-v3.3.7-563d7c.svg
   :alt: Bootstrap 3.3.7
   :target: http://getbootstrap.com/
.. |jquery| image:: https://img.shields.io/badge/jQuery-v3.1.1-0769ad.svg
   :alt: jQuery 3.1.1
   :target: http://jquery.com/
.. |fontawesome| image:: https://img.shields.io/badge/Font_Awesome-v4.7.0-1c9a71.svg
   :alt: Font Awesome 4.7.0
   :target: http://fontawesome.io/

Install
=======

.. code-block:: bash

    pip install django-bootstrap-static

Configuration
=============

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
============

Occasionally, I forget to update this package with new bootstrap updates.
Please feel free to submit a PR.

Sources and Procedures
----------------------

Bootstrap: (all files from dist package)
    `Bootstrap website / Getting started`_ -> drop into ``bootstrap/static/bootstrap/``
jQuery: (compressed, uncompressed, map)
    `jQuery website / Download`_ -> rename and mix into ``bootstrap/static/bootstrap/js/``

    Pick the latest version denoted as a dependency in ``bower.json`` (see `Plugin dependencies`_).
Font Awesome: (``css/``, ``fonts/`` only)
    `Font Awesome website`_ ("No thanks, just download") -> drop into ``fontawesome/static/fontawesome/``

.. _Bootstrap website / Getting started: http://getbootstrap.com/getting-started/
.. _jQuery website / Download: http://jquery.com/download/
.. _Plugin dependencies: https://getbootstrap.com/javascript/
.. _Font Awesome website: http://fontawesome.io/

Releases
========

To keep with the Bootstrap release schedule we will keep version numbers of
this app in sync with the bootstrap Major.Minor.Revision changes (`semver`_).
The additional version number will be added at the end to denote a new change
within this package itself.

``django-bootstrap-static==3.3.1.1`` == Bootstrap ``3.3.1`` with an additional
package change.

.. _semver: http://semver.org/
