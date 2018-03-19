import pytest
from django.core.urlresolvers import reverse_lazy
from django.test.client import Client


@pytest.mark.parametrize(
    'header, incoming_ip, expected',
    (
        ('HTTP_X_FORWARDED_FOR', '127.0.0.1', 200),
        ('X_FORWARDED_FOR', '127.0.0.1', 200),
        ('HTTP_CLIENT_IP', '127.0.0.1', 200),
        ('HTTP_X_REAL_IP', '127.0.0.1', 200),
        ('HTTP_X_FORWARDED', '127.0.0.1', 200),
        ('HTTP_X_CLUSTER_CLIENT_IP', '127.0.0.1', 200),
        ('HTTP_FORWARDED_FOR', '127.0.0.1', 200),
        ('HTTP_FORWARDED', '127.0.0.1', 200),
        ('HTTP_VIA', '127.0.0.1', 200),
        ('REMOTE_ADDR', '127.0.0.1', 200)
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
    client = Client(*{header: incoming_ip})
    response = client.get(admin_url)
    assert response.status_code == expected


@pytest.mark.parametrize(
    'header, incoming_ip, expected',
    (
        ('HTTP_X_FORWARDED_FOR', '127.0.0.1', 200),
        ('X_FORWARDED_FOR', '127.0.0.1', 200),
        ('HTTP_CLIENT_IP', '127.0.0.1', 200),
        ('HTTP_X_REAL_IP', '127.0.0.1', 200),
        ('HTTP_X_FORWARDED', '127.0.0.1', 200),
        ('HTTP_X_CLUSTER_CLIENT_IP', '127.0.0.1', 200),
        ('HTTP_FORWARDED_FOR', '127.0.0.1', 200),
        ('HTTP_FORWARDED', '127.0.0.1', 200),
        ('HTTP_VIA', '127.0.0.1', 200),
        ('REMOTE_ADDR', '127.0.0.1', 200),
        ('HTTP_X_FORWARDED_FOR', '::1', 200),
        ('X_FORWARDED_FOR', '::1', 200),
        ('HTTP_CLIENT_IP', '::1', 200),
        ('HTTP_X_REAL_IP', '::1', 200),
        ('HTTP_X_FORWARDED', '::1', 200),
        ('HTTP_X_CLUSTER_CLIENT_IP', '::1', 200),
        ('HTTP_FORWARDED_FOR', '::1', 200),
        ('HTTP_FORWARDED', '::1', 200),
        ('HTTP_VIA', '::1', 200),
        ('REMOTE_ADDR', '::1', 200)
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
    settings.ALLOWED_ADMIN_IPS = ['127.0.0.1', '::1']
    admin_url = reverse_lazy('admin:login')
    client = Client(*{header: incoming_ip})
    response = client.get(admin_url)
    assert response.status_code == expected


@pytest.mark.parametrize(
    'header, incoming_ip, expected',
    (
        ('HTTP_X_FORWARDED_FOR', '127.0.0.1', 404),
        ('X_FORWARDED_FOR', '127.0.0.1', 404),
        ('HTTP_CLIENT_IP', '127.0.0.1', 404),
        ('HTTP_X_REAL_IP', '127.0.0.1', 404),
        ('HTTP_X_FORWARDED', '127.0.0.1', 404),
        ('HTTP_X_CLUSTER_CLIENT_IP', '127.0.0.1', 404),
        ('HTTP_FORWARDED_FOR', '127.0.0.1', 404),
        ('HTTP_FORWARDED', '127.0.0.1', 404),
        ('HTTP_VIA', '127.0.0.1', 404),
        ('REMOTE_ADDR', '127.0.0.1', 404),
        ('HTTP_X_FORWARDED_FOR', '::1', 404),
        ('X_FORWARDED_FOR', '::1', 404),
        ('HTTP_CLIENT_IP', '::1', 404),
        ('HTTP_X_REAL_IP', '::1', 404),
        ('HTTP_X_FORWARDED', '::1', 404),
        ('HTTP_X_CLUSTER_CLIENT_IP', '::1', 404),
        ('HTTP_FORWARDED_FOR', '::1', 404),
        ('HTTP_FORWARDED', '::1', 404),
        ('HTTP_VIA', '::1', 404),
        ('REMOTE_ADDR', '::1', 404)
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
    settings.ALLOWED_ADMIN_IPS = '127.0.0.2,::2'
    admin_url = reverse_lazy('admin:login')
    client = Client(*{header: incoming_ip})
    response = client.get(admin_url)
    assert response.status_code == expected


@pytest.mark.parametrize(
    'header, incoming_ip, expected',
    (
        ('HTTP_X_FORWARDED_FOR', '127.0.0.1', 200),
        ('X_FORWARDED_FOR', '127.0.0.1', 200),
        ('HTTP_CLIENT_IP', '127.0.0.1', 200),
        ('HTTP_X_REAL_IP', '127.0.0.1', 200),
        ('HTTP_X_FORWARDED', '127.0.0.1', 200),
        ('HTTP_X_CLUSTER_CLIENT_IP', '127.0.0.1', 200),
        ('HTTP_FORWARDED_FOR', '127.0.0.1', 200),
        ('HTTP_FORWARDED', '127.0.0.1', 200),
        ('HTTP_VIA', '127.0.0.1', 200),
        ('REMOTE_ADDR', '127.0.0.1', 200),
        ('HTTP_X_FORWARDED_FOR', '::1', 200),
        ('X_FORWARDED_FOR', '::1', 200),
        ('HTTP_CLIENT_IP', '::1', 200),
        ('HTTP_X_REAL_IP', '::1', 200),
        ('HTTP_X_FORWARDED', '::1', 200),
        ('HTTP_X_CLUSTER_CLIENT_IP', '::1', 200),
        ('HTTP_FORWARDED_FOR', '::1', 200),
        ('HTTP_FORWARDED', '::1', 200),
        ('HTTP_VIA', '::1', 200),
        ('REMOTE_ADDR', '::1', 200)
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
    settings.ALLOWED_ADMIN_IP_RANGES = ['127.0.0.0/24', '::/1']
    admin_url = reverse_lazy('admin:login')
    client = Client(*{header: incoming_ip})
    response = client.get(admin_url)
    assert response.status_code == expected


@pytest.mark.parametrize(
    'header, incoming_ip, expected',
    (
        ('HTTP_X_FORWARDED_FOR', '127.0.0.1', 404),
        ('X_FORWARDED_FOR', '127.0.0.1', 404),
        ('HTTP_CLIENT_IP', '127.0.0.1', 404),
        ('HTTP_X_REAL_IP', '127.0.0.1', 404),
        ('HTTP_X_FORWARDED', '127.0.0.1', 404),
        ('HTTP_X_CLUSTER_CLIENT_IP', '127.0.0.1', 404),
        ('HTTP_FORWARDED_FOR', '127.0.0.1', 404),
        ('HTTP_FORWARDED', '127.0.0.1', 404),
        ('HTTP_VIA', '127.0.0.1', 404),
        ('REMOTE_ADDR', '127.0.0.1', 404),
        ('HTTP_X_FORWARDED_FOR', '::1', 404),
        ('X_FORWARDED_FOR', '::1', 404),
        ('HTTP_CLIENT_IP', '::1', 404),
        ('HTTP_X_REAL_IP', '::1', 404),
        ('HTTP_X_FORWARDED', '::1', 404),
        ('HTTP_X_CLUSTER_CLIENT_IP', '::1', 404),
        ('HTTP_FORWARDED_FOR', '::1', 404),
        ('HTTP_FORWARDED', '::1', 404),
        ('HTTP_VIA', '::1', 404),
        ('REMOTE_ADDR', '::1', 404)
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
    settings.ALLOWED_ADMIN_IPS = ['192.168.0.0/24', '2000::']
    admin_url = reverse_lazy('admin:login')
    client = Client(*{header: incoming_ip})
    response = client.get(admin_url)
    assert response.status_code == expected
