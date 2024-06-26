==============================================
Django Bootstrap Static Files |latest-version|
==============================================

|bootstrap| |jquery| |fontawesome| |pipeline|

Bootstrap and optional Font Awesome static files ready for the picking.

Also ships the latest jQuery compatible with Bootstrap, for optional inclusion.

.. |latest-version| image:: https://img.shields.io/pypi/v/django-bootstrap-static.svg
   :alt: Latest version on PyPI
   :target: https://pypi.python.org/pypi/django-bootstrap-static
.. |bootstrap| image:: https://img.shields.io/badge/Bootstrap-v5.3.3-563d7c.svg
   :alt: Bootstrap 5.3.3
   :target: https://getbootstrap.com/
.. |jquery| image:: https://img.shields.io/badge/jQuery-v3.7.1-0769ad.svg
   :alt: jQuery 3.7.1
   :target: https://jquery.com/
.. |fontawesome| image:: https://img.shields.io/badge/Font_Awesome-v6.5.2-1c9a71.svg
   :alt: Font Awesome 6.5.2
   :target: https://fontawesome.com/icons?m=free
.. |pipeline| image:: https://github.com/bittner/django-bootstrap-static/actions/workflows/pipeline.yml/badge.svg
   :alt: Build status
   :target: https://github.com/bittner/django-bootstrap-static/actions/workflows/pipeline.yml

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
        <script defer src="{% static 'fontawesome/js/all.min.js' %}"></script>
    </head>
    <body>
        ...
        <script src="{% static 'bootstrap/js/jquery.min.js' %}"></script>
        <script src="{% static 'bootstrap/js/bootstrap.bundle.min.js' %}"></script>
    </body>

Note that in the above code sample we use SVG powered Font Awesome, as
recommended by their docs.  You can use Font Awesome the classic way by
replacing the ``<script ...>`` tag in the ``<head>`` section above by:

.. code-block:: django

    <link rel="stylesheet" href="{% static 'fontawesome/css/all.min.css' %}">

If you don't use Bootstrap features that require ``Popper.js`` (e.g. dropdowns,
popovers, tooltips) you can include ``bootstrap.min.js`` instead of the bundle
to save a few kilobytes of bandwidth.

More details on integration may be available from each of the two projects:

- https://getbootstrap.com/docs/5.3/getting-started/introduction/
- https://fontawesome.com/get-started (`Upgrading from Version 4 of Font Awesome`_)

.. _Upgrading from Version 4 of Font Awesome:
    https://fontawesome.com/get-started/web-fonts-with-css#upgrading

Contribution
============

Occasionally, I forget to update this package with new bootstrap updates.
Please feel free to submit a PR.

Sources and Procedures
----------------------

Bootstrap: (all files from dist package)
    `Bootstrap website / Download`_ ➜ drop into ``bootstrap/static/bootstrap/``
jQuery: (compressed, uncompressed, map)
    `jQuery website / Download`_ ➜ rename and mix into ``bootstrap/static/bootstrap/js/``

    Pick the latest version denoted as a dependency in ``bower.json`` (see `Dependencies`_).
Font Awesome: (content of the ``on-server/`` folder only)
    `Font Awesome website / Download Free`_ ➜ drop into ``fontawesome/static/fontawesome/``

Tests
-----

Tests are great! And necessary. Please, add more. More is better!
We use `Tox`_.

.. code-block:: console

    pip install tox

Run all the linting and tests locally using Tox like this:

.. code-block:: console

    tox

.. code-block:: console

    tox list
    tox -e package
    tox -e py310,clean
    tox -e format -- tests

Releases
========

To stay aligned with the Bootstrap release schedule we will keep version
numbers of this app in sync with the bootstrap Major.Minor.Revision changes
(`semver`_).  The additional version number will be added at the end to denote
a new change within this package itself, e.g.

``django-bootstrap-static==3.3.1.1`` == Bootstrap ``3.3.1`` with an additional
package change.

.. _Bootstrap website / Download: https://getbootstrap.com/
.. _jQuery website / Download: https://jquery.com/download/
.. _Dependencies: https://getbootstrap.com/docs/5.0/getting-started/javascript/
.. _Font Awesome website / Download Free: https://fontawesome.com/
.. _Tox: https://tox.wiki/
.. _semver: https://semver.org/
