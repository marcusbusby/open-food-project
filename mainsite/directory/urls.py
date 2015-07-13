from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^food/all/$', views.food_list),
	url(r'^food/(?P<pk>[0-9]+)/$', views.food_detail),
	url(r'^company/all/$', views.company_list),
	url(r'^company/(?P<pk>[0-9]+)/$', views.company_detail)
]