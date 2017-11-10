Django Admin IP Restrictor
==========================

.. image:: https://circleci.com/gh/sdonk/django-admin-ip-restrictor/tree/master.svg?style=shield
    :target: https://circleci.com/gh/sdonk/django-admin-ip-restrictor/tree/master

.. image:: https://codecov.io/gh/sdonk/django-admin-ip-restrictor/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/sdonk/django-admin-ip-restrictor

.. image:: https://img.shields.io/pypi/v/django-admin-ip-restrictor.svg
    :target: https://pypi.python.org/pypi/django-admin-ip-restrictor

.. image:: https://img.shields.io/pypi/l/django-admin-ip-restrictor.svg

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
    ALLOWED_ADMIN_IP_RANGES[]


Contribute
----------

Fork the project and submit a PR!
