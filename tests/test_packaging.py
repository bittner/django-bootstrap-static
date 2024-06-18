"""Functional tests for installed package."""

from importlib import import_module, resources

import pytest


def test_imports():
    """Importing the package should work as described in the README."""

    bootstrap = import_module("bootstrap")
    fontawesome = import_module("fontawesome")

    assert bootstrap.__version__ == "5.3.3"
    assert fontawesome.__version__ == "6.5.2"


@pytest.mark.parametrize(
    ("package", "files"),
    [
        (
            "bootstrap.static.bootstrap.css",
            [
                "bootstrap.css",
                "bootstrap.css.map",
                "bootstrap.min.css",
                "bootstrap.min.css.map",
            ],
        ),
        (
            "bootstrap.static.bootstrap.js",
            [
                "bootstrap.js",
                "bootstrap.js.map",
                "bootstrap.min.js",
                "bootstrap.min.js.map",
                "jquery.js",
                "jquery.min.js",
                "jquery.min.map",
            ],
        ),
        (
            "fontawesome.static.fontawesome.css",
            [
                "all.css",
                "all.min.css",
                "fontawesome.css",
                "fontawesome.min.css",
            ],
        ),
    ],
)
def test_staticfiles(package, files):
    """Once installed, the package must contain static resources."""

    for filename in files:
        resource_path = resources.files(package) / filename
        assert resource_path.is_file(), f"{filename} not found in {package}"
