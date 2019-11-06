"""
Packaging setup for Django-Bootstrap-Static
"""
from setuptools import setup, find_packages

import bootstrap as package

setup(
    name='django-bootstrap-static',
    version=package.__version__,
    license=package.__license__,
    author=package.__author__,
    author_email=package.__email__,
    description=package.__doc__.strip(),
    long_description=open("README.rst", "r").read(),
    long_description_content_type='text/x-rst',
    url=package.__url__,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    keywords=[
        'django',
        'staticfiles',
        'bootstrap',
        'jquery',
        'fontawesome',
    ],
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
)
