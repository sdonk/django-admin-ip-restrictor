import ipaddress

from django.conf import settings
from django.http import Http404
from ipware.ip2 import get_client_ip

try:
    from django.urls import resolve
except ImportError:  # pragma: no cover
    from django.core.urlresolvers import resolve


class AdminIPRestrictorMiddleware(object):

    def __init__(self, get_response=None):
        self.get_response = get_response
        restrict_admin = getattr(
            settings,
            'RESTRICT_ADMIN',
            False
        )
        self.restrict_admin = self.parse_bool_envars(
            restrict_admin
        )
        allowed_admin_ips = getattr(
            settings,
            'ALLOWED_ADMIN_IPS',
            []
        )
        self.allowed_admin_ips = self.parse_list_envars(
            allowed_admin_ips
        )
        allowed_admin_ip_ranges = getattr(
            settings,
            'ALLOWED_ADMIN_IP_RANGES',
            []
        )
        self.allowed_admin_ip_ranges = self.parse_list_envars(
            allowed_admin_ip_ranges
        )

    def __call__(self, request):
        response = self.process_request(request)

        if not response and self.get_response:
            response = self.get_response(request)

        return response

    @staticmethod
    def parse_bool_envars(value):
        if value in ('true', 'True', '1', 1):
            return True
        return False

    @staticmethod
    def parse_list_envars(value):
        if type(value) == list:
            return value
        else:
            return value.split(',')

    def is_blocked(self, ip):
        """Determine if an IP address should be considered blocked."""
        blocked = True

        if ip in self.allowed_admin_ips:
            blocked = False

        for allowed_range in self.allowed_admin_ip_ranges:
            if ipaddress.ip_address(ip) in ipaddress.ip_network(allowed_range):
                blocked = False

        return blocked

    def get_ip(self, request):
        client_ip, is_routable = get_client_ip(request)
        assert client_ip, 'IP not found'
        assert is_routable, 'IP is private'
        return client_ip

    def process_request(self, request):
        if self.restrict_admin:
            ip = self.get_ip(request)
            is_admin_app = resolve(request.path).app_name == 'admin'
            conditions = (is_admin_app, self.is_blocked(ip))

            if all(conditions):
                raise Http404()

        return None
