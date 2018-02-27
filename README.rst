Django Admin IP Restrictor
==========================

.. image:: https://circleci.com/gh/sdonk/django-admin-ip-restrictor/tree/master.svg?style=shield
    :target: https://circleci.com/gh/sdonk/django-admin-ip-restrictor/tree/master

.. image:: https://codecov.io/gh/sdonk/django-admin-ip-restrictor/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/sdonk/django-admin-ip-restrictor

.. image:: https://img.shields.io/pypi/v/django-admin-ip-restrictor.svg
    :target: https://pypi.python.org/pypi/django-admin-ip-restrictor

.. image:: https://img.shields.io/pypi/pyversions/django-admin-ip-restrictor.svg
    :target: https://pypi.python.org/pypi/django-admin-ip-restrictor

.. image:: https://img.shields.io/pypi/l/django-admin-ip-restrictor.svg
    :target: https://pypi.python.org/pypi/django-admin-ip-restrictor

A Django middleware to restrict the access to the Django admin based on incoming IPs

Requirements
------------

* Python >= 3.4
* Django >= 1.9
* django-ipware==1.1.6

Usage
-----

First install the package::

    $ pip install django-admin-ip-restrictor

Then add the middleware to your settings::

    # Django 1.9
    MIDDLEWARE_CLASSES = [
        ...
        'admin_ip_restrictor.middleware.AdminIPRestrictorMiddleware'
    ]

    # Django 1.10+
    MIDDLEWARE = [
        ...
        'admin_ip_restrictor.middleware.AdminIPRestrictorMiddleware'
    ]

Use these settings to control who has access to the admin::

    RESTRICT_ADMIN=True
    ALLOWED_ADMIN_IPS=[]
    ALLOWED_ADMIN_IP_RANGES=[]

Run tests
---------

Install `tox` and `pyenv`::

    $ pip install tox pyenv


Install Python versions in `pyenv`::

    $ pyenv install 3.4.4
    $ pyenv install 3.5.3
    $ pyenv install 3.6.2

Specify the Python versions you want to test with::

    $ pyenv local 3.4.4 3.5.3 3.6.2

Run tests::

    $ tox


Contribute
----------

Fork the project and submit a PR!
