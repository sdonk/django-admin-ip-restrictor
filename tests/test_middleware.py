from unittest import mock

import pytest
from django.core.urlresolvers import reverse_lazy
from django.test.client import Client


@pytest.mark.parametrize(
    'header, incoming_ip, expected',
    (
        ('HTTP_X_FORWARDED_FOR', '74.125.224.72', 200),
        ('X_FORWARDED_FOR', '74.125.224.72', 200),
        ('HTTP_CLIENT_IP', '74.125.224.72', 200),
        ('HTTP_X_REAL_IP', '74.125.224.72', 200),
        ('HTTP_X_FORWARDED', '74.125.224.72', 200),
        ('HTTP_X_CLUSTER_CLIENT_IP', '74.125.224.72', 200),
        ('HTTP_FORWARDED_FOR', '74.125.224.72', 200),
        ('HTTP_FORWARDED', '74.125.224.72', 200),
        ('HTTP_VIA', '74.125.224.72', 200),
        ('REMOTE_ADDR', '74.125.224.72', 200)
    ),
    ids=[
        'HTTP_X_FORWARDED_FOR allow',
        'X_FORWARDED_FOR allow',
        'HTTP_CLIENT_IP allow',
        'HTTP_X_REAL_IP allow',
        'HTTP_X_FORWARDED allow',
        'HTTP_X_CLUSTER_CLIENT_IP allow',
        'HTTP_FORWARDED_FOR allow',
        'HTTP_FORWARDED allow',
        'HTTP_VIA allow',
        'REMOTE_ADDR allow'
    ]
)
def test_admin_no_restriction(header, incoming_ip, expected, settings):
    settings.RESTRICT_ADMIN = False
    admin_url = reverse_lazy('admin:login')
    client = Client()
    response = client.get(admin_url, **{header: incoming_ip})
    assert response.status_code == expected


@pytest.mark.parametrize(
    'header, incoming_ip, expected',
    (
        ('HTTP_X_FORWARDED_FOR', '74.125.224.72', 200),
        ('X_FORWARDED_FOR', '74.125.224.72', 200),
        ('HTTP_CLIENT_IP', '74.125.224.72', 200),
        ('HTTP_X_REAL_IP', '74.125.224.72', 200),
        ('HTTP_X_FORWARDED', '74.125.224.72', 200),
        ('HTTP_X_CLUSTER_CLIENT_IP', '74.125.224.72', 200),
        ('HTTP_FORWARDED_FOR', '74.125.224.72', 200),
        ('HTTP_FORWARDED', '74.125.224.72', 200),
        ('HTTP_VIA', '74.125.224.72', 200),
        ('REMOTE_ADDR', '74.125.224.72', 200),
        ('HTTP_X_FORWARDED_FOR', '0:0:0:0:0:ffff:4a7d:e048', 200),
        ('X_FORWARDED_FOR', '0:0:0:0:0:ffff:4a7d:e048', 200),
        ('HTTP_CLIENT_IP', '0:0:0:0:0:ffff:4a7d:e048', 200),
        ('HTTP_X_REAL_IP', '0:0:0:0:0:ffff:4a7d:e048', 200),
        ('HTTP_X_FORWARDED', '0:0:0:0:0:ffff:4a7d:e048', 200),
        ('HTTP_X_CLUSTER_CLIENT_IP', '0:0:0:0:0:ffff:4a7d:e048', 200),
        ('HTTP_FORWARDED_FOR', '0:0:0:0:0:ffff:4a7d:e048', 200),
        ('HTTP_FORWARDED', '0:0:0:0:0:ffff:4a7d:e048', 200),
        ('HTTP_VIA', '0:0:0:0:0:ffff:4a7d:e048', 200),
        ('REMOTE_ADDR', '0:0:0:0:0:ffff:4a7d:e048', 200)
    ),
    ids=[
        'HTTP_X_FORWARDED_FOR allow',
        'X_FORWARDED_FOR allow',
        'HTTP_CLIENT_IP allow',
        'HTTP_X_REAL_IP allow',
        'HTTP_X_FORWARDED allow',
        'HTTP_X_CLUSTER_CLIENT_IP allow',
        'HTTP_FORWARDED_FOR allow',
        'HTTP_FORWARDED allow',
        'HTTP_VIA allow',
        'REMOTE_ADDR allow',
        'HTTP_X_FORWARDED_FOR ipv6 allow',
        'X_FORWARDED_FOR ipv6 allow',
        'HTTP_CLIENT_IP ipv6 allow',
        'HTTP_X_REAL_IP ipv6 allow',
        'HTTP_X_FORWARDED ipv6 allow',
        'HTTP_X_CLUSTER_CLIENT_IP ipv6 allow',
        'HTTP_FORWARDED_FOR ipv6 allow',
        'HTTP_FORWARDED ipv6 allow',
        'HTTP_VIA ipv6 allow',
        'REMOTE_ADDR ipv6 allow',
    ]
)
def test_admin_restricted_allowed_ips(header, incoming_ip, expected, settings):
    settings.RESTRICT_ADMIN = True
    settings.ALLOWED_ADMIN_IPS = ['74.125.224.72', '0:0:0:0:0:ffff:4a7d:e048']
    admin_url = reverse_lazy('admin:login')
    client = Client()
    response = client.get(admin_url, **{header: incoming_ip})
    assert response.status_code == expected


@pytest.mark.parametrize(
    'header, incoming_ip, expected',
    (
        ('HTTP_X_FORWARDED_FOR', '74.125.224.72', 404),
        ('X_FORWARDED_FOR', '74.125.224.72', 404),
        ('HTTP_CLIENT_IP', '74.125.224.72', 404),
        ('HTTP_X_REAL_IP', '74.125.224.72', 404),
        ('HTTP_X_FORWARDED', '74.125.224.72', 404),
        ('HTTP_X_CLUSTER_CLIENT_IP', '74.125.224.72', 404),
        ('HTTP_FORWARDED_FOR', '74.125.224.72', 404),
        ('HTTP_FORWARDED', '74.125.224.72', 404),
        ('HTTP_VIA', '74.125.224.72', 404),
        ('REMOTE_ADDR', '74.125.224.72', 404),
        ('HTTP_X_FORWARDED_FOR', '0:0:0:0:0:ffff:4a7d:e048', 404),
        ('X_FORWARDED_FOR', '0:0:0:0:0:ffff:4a7d:e048', 404),
        ('HTTP_CLIENT_IP', '0:0:0:0:0:ffff:4a7d:e048', 404),
        ('HTTP_X_REAL_IP', '0:0:0:0:0:ffff:4a7d:e048', 404),
        ('HTTP_X_FORWARDED', '0:0:0:0:0:ffff:4a7d:e048', 404),
        ('HTTP_X_CLUSTER_CLIENT_IP', '0:0:0:0:0:ffff:4a7d:e048', 404),
        ('HTTP_FORWARDED_FOR', '0:0:0:0:0:ffff:4a7d:e048', 404),
        ('HTTP_FORWARDED', '0:0:0:0:0:ffff:4a7d:e048', 404),
        ('HTTP_VIA', '0:0:0:0:0:ffff:4a7d:e048', 404),
        ('REMOTE_ADDR', '0:0:0:0:0:ffff:4a7d:e048', 404)
    ),
    ids=[
        'HTTP_X_FORWARDED_FOR block',
        'X_FORWARDED_FOR block',
        'HTTP_CLIENT_IP block',
        'HTTP_X_REAL_IP block',
        'HTTP_X_FORWARDED block',
        'HTTP_X_CLUSTER_CLIENT_IP block',
        'HTTP_FORWARDED_FOR block',
        'HTTP_FORWARDED block',
        'HTTP_VIA block',
        'REMOTE_ADDR block',
        'HTTP_X_FORWARDED_FOR ipv6 block',
        'X_FORWARDED_FOR ipv6 block',
        'HTTP_CLIENT_IP ipv6 block',
        'HTTP_X_REAL_IP ipv6 block',
        'HTTP_X_FORWARDED ipv6 block',
        'HTTP_X_CLUSTER_CLIENT_IP ipv6 block',
        'HTTP_FORWARDED_FOR ipv6 block',
        'HTTP_FORWARDED ipv6 block',
        'HTTP_VIA ipv6 block',
        'REMOTE_ADDR ipv6 block'
    ]
)
def test_admin_restricted_blocked_ips(header, incoming_ip, expected, settings):
    settings.RESTRICT_ADMIN = True
    settings.ALLOWED_ADMIN_IPS = ['8.8.8.9', '0:0:0:0:0:ffff:4a7d:e04b']
    admin_url = reverse_lazy('admin:login')
    client = Client()
    response = client.get(admin_url, **{header: incoming_ip})
    assert response.status_code == expected


@pytest.mark.parametrize(
    'header, incoming_ip, expected',
    (
        ('HTTP_X_FORWARDED_FOR', '74.125.224.72', 200),
        ('X_FORWARDED_FOR', '74.125.224.72', 200),
        ('HTTP_CLIENT_IP', '74.125.224.72', 200),
        ('HTTP_X_REAL_IP', '74.125.224.72', 200),
        ('HTTP_X_FORWARDED', '74.125.224.72', 200),
        ('HTTP_X_CLUSTER_CLIENT_IP', '74.125.224.72', 200),
        ('HTTP_FORWARDED_FOR', '74.125.224.72', 200),
        ('HTTP_FORWARDED', '74.125.224.72', 200),
        ('HTTP_VIA', '74.125.224.72', 200),
        ('REMOTE_ADDR', '74.125.224.72', 200),
        ('HTTP_X_FORWARDED_FOR', '0:0:0:0:0:ffff:4a7d:e048', 200),
        ('X_FORWARDED_FOR', '0:0:0:0:0:ffff:4a7d:e048', 200),
        ('HTTP_CLIENT_IP', '0:0:0:0:0:ffff:4a7d:e048', 200),
        ('HTTP_X_REAL_IP', '0:0:0:0:0:ffff:4a7d:e048', 200),
        ('HTTP_X_FORWARDED', '0:0:0:0:0:ffff:4a7d:e048', 200),
        ('HTTP_X_CLUSTER_CLIENT_IP', '0:0:0:0:0:ffff:4a7d:e048', 200),
        ('HTTP_FORWARDED_FOR', '0:0:0:0:0:ffff:4a7d:e048', 200),
        ('HTTP_FORWARDED', '0:0:0:0:0:ffff:4a7d:e048', 200),
        ('HTTP_VIA', '0:0:0:0:0:ffff:4a7d:e048', 200),
        ('REMOTE_ADDR', '0:0:0:0:0:ffff:4a7d:e048', 200)
    ),
    ids=[
        'HTTP_X_FORWARDED_FOR allow',
        'X_FORWARDED_FOR allow',
        'HTTP_CLIENT_IP allow',
        'HTTP_X_REAL_IP allow',
        'HTTP_X_FORWARDED allow',
        'HTTP_X_CLUSTER_CLIENT_IP allow',
        'HTTP_FORWARDED_FOR allow',
        'HTTP_FORWARDED allow',
        'HTTP_VIA allow',
        'REMOTE_ADDR allow',
        'HTTP_X_FORWARDED_FOR ipv6 allow',
        'X_FORWARDED_FOR ipv6 allow',
        'HTTP_CLIENT_IP ipv6 allow',
        'HTTP_X_REAL_IP ipv6 allow',
        'HTTP_X_FORWARDED ipv6 allow',
        'HTTP_X_CLUSTER_CLIENT_IP ipv6 allow',
        'HTTP_FORWARDED_FOR ipv6 allow',
        'HTTP_FORWARDED ipv6 allow',
        'HTTP_VIA ipv6 allow',
        'REMOTE_ADDR ipv6 allow',
    ]
)
def test_admin_restricted_allowed_ip_ranges(header, incoming_ip, expected,
                                            settings):
    settings.RESTRICT_ADMIN = True
    settings.ALLOWED_ADMIN_IP_RANGES = [
        '74.125.224.72/32',
        '0:0:0:0:0:ffff:4a7d:e048/128'
    ]
    admin_url = reverse_lazy('admin:login')
    client = Client()
    response = client.get(admin_url, **{header: incoming_ip})
    assert response.status_code == expected


@pytest.mark.parametrize(
    'header, incoming_ip, expected',
    (
        ('HTTP_X_FORWARDED_FOR', '74.125.224.72', 404),
        ('X_FORWARDED_FOR', '74.125.224.72', 404),
        ('HTTP_CLIENT_IP', '74.125.224.72', 404),
        ('HTTP_X_REAL_IP', '74.125.224.72', 404),
        ('HTTP_X_FORWARDED', '74.125.224.72', 404),
        ('HTTP_X_CLUSTER_CLIENT_IP', '74.125.224.72', 404),
        ('HTTP_FORWARDED_FOR', '74.125.224.72', 404),
        ('HTTP_FORWARDED', '74.125.224.72', 404),
        ('HTTP_VIA', '74.125.224.72', 404),
        ('REMOTE_ADDR', '74.125.224.72', 404),
        ('HTTP_X_FORWARDED_FOR', '0:0:0:0:0:ffff:4a7d:e048', 404),
        ('X_FORWARDED_FOR', '0:0:0:0:0:ffff:4a7d:e048', 404),
        ('HTTP_CLIENT_IP', '0:0:0:0:0:ffff:4a7d:e048', 404),
        ('HTTP_X_REAL_IP', '0:0:0:0:0:ffff:4a7d:e048', 404),
        ('HTTP_X_FORWARDED', '0:0:0:0:0:ffff:4a7d:e048', 404),
        ('HTTP_X_CLUSTER_CLIENT_IP', '0:0:0:0:0:ffff:4a7d:e048', 404),
        ('HTTP_FORWARDED_FOR', '0:0:0:0:0:ffff:4a7d:e048', 404),
        ('HTTP_FORWARDED', '0:0:0:0:0:ffff:4a7d:e048', 404),
        ('HTTP_VIA', '0:0:0:0:0:ffff:4a7d:e048', 404),
        ('REMOTE_ADDR', '0:0:0:0:0:ffff:4a7d:e048', 404)
    ),
    ids=[
        'HTTP_X_FORWARDED_FOR block',
        'X_FORWARDED_FOR block',
        'HTTP_CLIENT_IP block',
        'HTTP_X_REAL_IP block',
        'HTTP_X_FORWARDED block',
        'HTTP_X_CLUSTER_CLIENT_IP block',
        'HTTP_FORWARDED_FOR block',
        'HTTP_FORWARDED block',
        'HTTP_VIA block',
        'REMOTE_ADDR block',
        'HTTP_X_FORWARDED_FOR ipv6 block',
        'X_FORWARDED_FOR ipv6 block',
        'HTTP_CLIENT_IP ipv6 block',
        'HTTP_X_REAL_IP ipv6 block',
        'HTTP_X_FORWARDED ipv6 block',
        'HTTP_X_CLUSTER_CLIENT_IP ipv6 block',
        'HTTP_FORWARDED_FOR ipv6 block',
        'HTTP_FORWARDED ipv6 block',
        'HTTP_VIA ipv6 block',
        'REMOTE_ADDR ipv6 block',
    ]
)
def test_admin_restricted_blocked_ip_ranges(header, incoming_ip, expected,
                                            settings):
    settings.RESTRICT_ADMIN = True
    settings.ALLOWED_ADMIN_IPS = ['192.168.0.0/24', '0:0:0:0:0:ffff:4a7d:e04b']
    admin_url = reverse_lazy('admin:login')
    client = Client()
    response = client.get(admin_url, **{header: incoming_ip})
    assert response.status_code == expected


@mock.patch('admin_ip_restrictor.middleware.get_client_ip')
def test_client_ip_not_found(mocked_get_client_ip):
    mocked_get_client_ip.return_value = None, None

    admin_url = reverse_lazy('admin:login')
    client = Client()
    with pytest.raises(Exception) as e:
        client.get(admin_url)
    assert 'IP not found' in str(e.value)


@pytest.mark.parametrize(
    'header, incoming_ip',
    (
        ('HTTP_X_FORWARDED_FOR', '127.0.0.1'),
        ('HTTP_X_FORWARDED_FOR', 'fc00:'),
    ),
    ids=[
        'Private IPV4',
        'Private IPV6'
    ]
)
def test_client_ip_private(header, incoming_ip):

    admin_url = reverse_lazy('admin:login')
    client = Client()
    with pytest.raises(Exception) as e:
        client.get(admin_url, **{header: incoming_ip})
    assert 'IP is private' in str(e.value)


@pytest.mark.parametrize(
    'envar, expected',
    (
        ('127.0.0.1', ['127.0.0.1']),
        ('127.0.0.1,127.0.0.2', ['127.0.0.1', '127.0.0.2']),
    ),
    ids=[
        'single entry string',
        'comma separated multiple entry string',
    ]
)
def test_list_envars_parsing(envar, expected):
    from admin_ip_restrictor.middleware import AdminIPRestrictorMiddleware
    assert AdminIPRestrictorMiddleware.parse_list_envars(envar) == expected


@pytest.mark.parametrize(
    'envar, expected',
    (
        ('True', True),
        ('true', True),
        ('1', True),
        (1, True),
        ('bla', False),
        ('foo', False),
        ('0', False),
        (0, False)
    ),
    ids=[
        'True',
        'true',
        '1',
        '1 number',
        'false',
        'False',
        '0',
        '0 number'
    ]
)
def test_bool_envars_parsing(envar, expected):
    from admin_ip_restrictor.middleware import AdminIPRestrictorMiddleware
    assert AdminIPRestrictorMiddleware.parse_bool_envars(envar) == expected
