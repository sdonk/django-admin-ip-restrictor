from django.conf.urls import include, url
from django.contrib import admin
from django.http.response import HttpResponse

def my_view(*args, **kwargs):
	return HttpResponse('Hello, world')

not_admin_urls = [
	url(r'', my_view, name='home'),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^not-admin/', include((not_admin_urls, 'not-admin')))
]
