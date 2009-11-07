try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

version = '0.1.2'
try:
    long_description = open('README.rst').read()
except IOError:
    long_description = """\
galerts
=======

galerts is a Python client for managing `Google Alerts
<http://www.google.com/alerts>`_. Currently it resorts to scraping html from
Google's web interface since there is as of yet no public API. If they ever
decide to publish one, galerts will promptly switch over to using it.

Using galerts should be pretty straightforward. Check out the README and the
module itself for documentation.

Please find `galerts on github <http://github.com/jab/galerts>`_ if you would
like to collaborate!
"""

setup(
    name='galerts',
    version=version,
    author='Josh Bronson',
    author_email='jabronson@gmail.com',
    description="Python libary for managing Google Alerts",
    long_description=long_description,
    keywords='google, alerts, google alerts, news',
    url='http://github.com/jab/galerts',
    license='MIT',
    py_modules=['galerts'],
    zip_safe=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        ],
    install_requires=[
        "BeautifulSoup",
        ],
    )
