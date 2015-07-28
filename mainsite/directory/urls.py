from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^food/all/$', views.food_list),
	url(r'^food/(?P<pk>[0-9]+)/$', views.food_detail),
	url(r'^food/new', views.food_new),
	url(r'^food/edit/(?P<pk>[0-9]+)/$', views.food_edit),
	url(r'^food/delete/(?P<pk>[0-9]+)/$', views.food_delete),
	url(r'^component/delete/(?P<pk>[0-9]+)/$', views.component_delete),
	url(r'^company/all/$', views.company_list),
	url(r'^company/(?P<pk>[0-9]+)/$', views.company_detail),
	url(r'^company/new/$', views.company_new, name='company_new'),
	url(r'^company/edit/(?P<pk>[0-9]+)/$', views.company_edit),
	url(r'^company/delete/(?P<pk>[0-9]+)/$', views.company_delete),
	url(r'^component/new', views.component_new),
	url(r'^search/$', views.search),
	url(r'^sort/$', views.food_sort),
	url(r'^food/photo/new/$', views.food_photo_new),
	url(r'^food/photo/delete/(?P<pk>[0-9]+)/$', views.food_photo_delete),
	url(r'^company/photo/delete/(?P<pk>[0-9]+)/$', views.company_photo_delete),
	url(r'^company/photo/new/$', views.company_photo_new),
]