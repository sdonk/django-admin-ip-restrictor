Django Admin IP Restrictor
==========================

.. image:: https://travis-ci.org/sdonk/django-admin-ip-restrictor.svg?branch=master
    :target: https://travis-ci.org/sdonk/django-admin-ip-restrictor

.. image:: https://codecov.io/gh/uktrade/django-admin-ip-restrictor/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/uktrade/django-admin-ip-restrictor

.. image:: https://img.shields.io/pypi/v/django-admin-ip-restrictor.svg
    :target: https://pypi.python.org/pypi/django-admin-ip-restrictor

.. image:: https://img.shields.io/pypi/pyversions/django-admin-ip-restrictor.svg
    :target: https://pypi.python.org/pypi/django-admin-ip-restrictor

.. image:: https://img.shields.io/pypi/l/django-admin-ip-restrictor.svg
    :target: https://pypi.python.org/pypi/django-admin-ip-restrictor

A Django middleware to restrict the access to the Django admin based on incoming IPs

Requirements
------------

* Python >= 3.5
* Django >= 1.11,<4
* django-ipware=>2,<4

Note that Django 3 has dropped support for Python 3.5

Usage
-----

First install the package::

    $ pip install django-admin-ip-restrictor

Then add the middleware to your settings::

    MIDDLEWARE = [
        ...
        'admin_ip_restrictor.middleware.AdminIPRestrictorMiddleware'
    ]

Set these variables in your `settings.py` to control who has access to the admin (IPV4 and IPV6 can be mixed)::

    RESTRICT_ADMIN=True
    ALLOWED_ADMIN_IPS=['127.0.0.1', '::1']
    ALLOWED_ADMIN_IP_RANGES=['127.0.0.0/24', '::/1']
    RESTRICTED_APP_NAMES=['admin']
    TRUST_PRIVATE_IP=True

Use `RESTRICTED_APP_NAMES` to restrict the access to more apps. Admin app is always included.

If using environment variables make sure that the variables receive the right type of value.
`django-admin-ip-restrictor` automatically converts the following formats::

    $ export RESTRICT_ADMIN='true'
    $ export ALLOWED_ADMIN_IPS='127.0.0.1,::1'
    $ export ALLOWED_ADMIN_IP_RANGES='127.0.0.0/24,::/1'
    $ export RESTRICTED_APP_NAMES='wagtail_admin,foo'


For `RESTRICT_ADMIN` also these values can be used: `True`, `1`, `false`, `False`, `0`

Use `TRUST_PRIVATE_IP` to skip checking IP addresses from a trusted private network.

Changelog
---------
Full changelog at https://github.com/sdonk/django-admin-ip-restrictor/blob/master/CHANGELOG.rst

Run tests
---------

Install `tox`::

    $ pip install tox


Install `pyenv`, use https://github.com/pyenv/pyenv#installation as reference.

Install Python versions in `pyenv`::

    $ pyenv install 3.5.10
    $ pyenv install 3.6.12
    $ pyenv install 3.7.9
    $ pyenv install 3.8.6

Specify the Python versions you want to test with::

    $ pyenv local 3.5.10 3.6.12 3.7.9 3.8.6

Run tests::

    $ tox

Contribute
----------

Fork the project and submit a PR!
