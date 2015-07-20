"""mainsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('directory.urls')),
    url(r'^accounts/login/$', 'mainsite.views.login', name = 'login'),
    url(r'^accounts/auth/$', 'mainsite.views.auth_view'),
    url(r'^accounts/logout/$', 'mainsite.views.logout'),
    url(r'^accounts/loggedin/$', 'mainsite.views.loggedin'),
    url(r'^accounts/invalid/$', 'mainsite.views.invalid_login'),
    url(r'^accounts/register/$', 'mainsite.views.register_user'),
    url(r'^accounts/register_success/$', 'mainsite.views.register_success'),
    url(r'', include('userprofile.urls')),

]
