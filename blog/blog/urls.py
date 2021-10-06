"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
    """


from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from blog.views import register_view
from posts.views import index
from shop.views import products_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", index, name="index_view"),
    path("register/", register_view, name="register_view"),
    path("api/", include("api.urls", namespace="api")),
    path("", products_view, name="products_view"),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
