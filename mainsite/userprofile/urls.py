from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r'^accounts/profile/$', 'userprofile.views.user_profile'),
	url(r'^accounts/login/$', 'userprofile.views.login', name = 'login'),
    url(r'^accounts/auth/$', 'userprofile.views.auth_view'),
    url(r'^accounts/logout/$', 'userprofile.views.logout'),
    url(r'^accounts/loggedin/$', 'userprofile.views.loggedin'),
    url(r'^accounts/invalid/$', 'userprofile.views.invalid_login'),
    url(r'^accounts/register/$', 'userprofile.views.register_user'),
    url(r'^accounts/register_success/$', 'userprofile.views.register_success'),
)