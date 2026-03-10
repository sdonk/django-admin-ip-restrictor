from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import include, path


def my_view(*args, **kwargs):
    return HttpResponse("Hello, world")


not_admin_urls = [
    path("", my_view, name="home"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("not-admin/", include((not_admin_urls, "not-admin"))),
]
