"""Tests for Django templates."""

from django.template import Context, Template

readme_template = """
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
"""

classic_template = """
    {% load static %}
    <link rel="stylesheet" href="{% static 'fontawesome/css/all.min.css' %}">
"""


def test_readme_template():
    """Importing the package should work as described in the README."""
    bootstrap_min_css = "bootstrap/css/bootstrap.min.css"
    bootstrap_min_js = "bootstrap/js/bootstrap.bundle.min.js"
    fontawesome_min_js = "fontawesome/js/all.min.js"
    jquery_min_js = "bootstrap/js/jquery.min.js"

    c = Context()
    t = Template(readme_template)
    html = t.render(c)

    assert f'<link rel="stylesheet" href="/static/{bootstrap_min_css}">' in html
    assert f'<script defer src="/static/{fontawesome_min_js}"></script>' in html
    assert f'<script src="/static/{jquery_min_js}"></script>' in html
    assert f'<script src="/static/{bootstrap_min_js}"></script>' in html


def test_classic_fontawesome():
    """Non-JS powered, classic Font Awesome."""
    fontawesome_min_css = "fontawesome/css/all.min.css"

    c = Context()
    t = Template(classic_template)
    html = t.render(c)

    assert f'<link rel="stylesheet" href="/static/{fontawesome_min_css}">' in html
