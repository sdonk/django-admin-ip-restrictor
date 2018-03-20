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
        self.restrict_admin = getattr(
            settings,
            'RESTRICT_ADMIN',
            False
        )
        allowed_admin_ips = getattr(
            settings,
            'ALLOWED_ADMIN_IPS',
            []
        )
        self.allowed_admin_ips = self.parse_envars(
            allowed_admin_ips
        )
        allowed_admin_ip_ranges = getattr(
            settings,
            'ALLOWED_ADMIN_IP_RANGES',
            []
        )
        self.allowed_admin_ip_ranges = self.parse_envars(
            allowed_admin_ip_ranges
        )

    def __call__(self, request):
        response = self.process_request(request)

        if not response and self.get_response:
            response = self.get_response(request)

        return response

    @staticmethod
    def parse_envars(value):
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
        if client_ip is None:
            raise Exception('IP not found')
        else:
            if is_routable:
                return client_ip
            else:
                raise Exception('IP is private')

    def process_request(self, request):
        ip = self.get_ip(request)
        is_admin_app = resolve(request.path).app_name == 'admin'
        conditions = (is_admin_app, self.restrict_admin, self.is_blocked(ip))

        if all(conditions):
            raise Http404()

        return None

