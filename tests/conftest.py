import os

import django
import pytest
from django.test.client import Client


def pytest_configure(config):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')
    django.setup()


@pytest.fixture
def incoming_ip():
    return '127.0.0.1'


@pytest.fixture
def client_from_ip(incoming_ip):
    return Client(REMOTE_ADDR=incoming_ip)


@pytest.fixture
def client_ip_header(incoming_ip):
    return Client(HTTP_X_FORWARDED_FOR=incoming_ip)

