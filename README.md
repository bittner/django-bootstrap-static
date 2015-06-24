Django Bootstrap Static Files
=============================

Bootstrap and optional Font Awesome static files ready for the picking.

Install
-------

pip install django-bootstrap-static==3.3.5

Contribution
------------

Occasionally, I forget to update this package with new bootstrap updates.  Please feel free to submit a PR.

Configuration
-------------

To pickup bootstrap static files, simply include 'bootstrap' in your INSTALLED_APPS.  You can also get Fontawesome support by adding 'fontawesome' to your installed apps.

Please refer to each project for integration/install guides.

- http://getbootstrap.com
- http://fortawesome.github.io/Font-Awesome/

Releases
--------

To keep with the bootstrap release schedule we will keep version numbers of this app in sync with the bootstrap Major.Minor.Revision changes.  The additional
version number will be added at the end to denote a new change within this package itself.

django-bootstrap-static==3.3.1.1 == bootstrap 3.3.1 with an additional package change.
