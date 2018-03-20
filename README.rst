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

    # Django 1.10+
    MIDDLEWARE = [
        ...
        'admin_ip_restrictor.middleware.AdminIPRestrictorMiddleware'
    ]

    # Django 1.9
    MIDDLEWARE_CLASSES = [
        ...
        'admin_ip_restrictor.middleware.AdminIPRestrictorMiddleware'
    ]

Set these variables in your `settings.py` to control who has access to the admin (IPV4 and IPV6 can be mixed)::

    RESTRICT_ADMIN=True
    ALLOWED_ADMIN_IPS=['127.0.0.1', '::1']
    ALLOWED_ADMIN_IP_RANGES=['127.0.0.0/24', '::/1']


If using environment variables make sure that the variables receive the right type of value.
`django-admin-ip-restrictor` automatically converts the following formats::

    $ export RESTRICT_ADMIN='true'
    $ export ALLOWED_ADMIN_IPS='127.0.0.1,::1'
    $ export ALLOWED_ADMIN_IP_RANGES='127.0.0.0/24,::/1'


For `RESTRICT_ADMIN` also these values can be used: `True`, `1`, `false`, `False`, `0`

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
