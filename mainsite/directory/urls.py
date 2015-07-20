from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home),
	url(r'^food/all/$', views.food_list),
	url(r'^food/(?P<pk>[0-9]+)/$', views.food_detail),
	url(r'^food/new', views.food_new),
	url(r'^food/edit/(?P<pk>[0-9]+)/$', views.food_edit),
	url(r'^company/all/$', views.company_list),
	url(r'^company/(?P<pk>[0-9]+)/$', views.company_detail),
	url(r'^company/new/$', views.company_new, name='company_new'),
	url(r'^company/edit/(?P<pk>[0-9]+)/$', views.company_edit),
	url(r'^component/new', views.component_new),
]