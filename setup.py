from setuptools import setup, find_packages

version = '4.0.0'

setup(name='django-bootstrap-static',
      version=version,
      description="A collection of Bootstrap static files.",
      long_description=open("README.rst", "r").read(),
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
      author='Peter Bittner',
      author_email='django@bittner.it',
      url='http://github.com/bittner/django-bootstrap-static',
      license='MIT',
      packages=find_packages(),
      install_requires=[],
      include_package_data=True,
      zip_safe=False,
      )
