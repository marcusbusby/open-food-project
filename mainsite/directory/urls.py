from django.conf.urls import url, patterns, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	url(r'^food/all/$', views.food_list),
	url(r'^food/(?P<pk>[0-9]+)/$', views.food_entry),
	url(r'^food/detail/(?P<string>[\w\-]+)/$', views.food_detail),
	url(r'^food/new', views.food_new),
	url(r'^food/edit/(?P<pk>[0-9]+)/$', views.food_edit),
	url(r'^food/delete/(?P<pk>[0-9]+)/$', views.food_delete),
	url(r'^component/delete/(?P<pk>[0-9]+)/$', views.component_delete),
	url(r'^company/all/$', views.company_list),
	url(r'^company/detail/(?P<string>[\w\-]+)/$', views.company_detail),
	url(r'^company/new/$', views.company_new, name='company_new'),
	url(r'^company/edit/(?P<pk>[0-9]+)/$', views.company_edit),
	url(r'^company/delete/(?P<pk>[0-9]+)/$', views.company_delete),
	url(r'^company/(?P<pk>[0-9]+)/$', views.company_entry),
	url(r'^component/new', views.component_new),
	url(r'^search/$', views.search),
	url(r'^sort/$', views.food_sort),
	url(r'^food/photo/new/$', views.food_photo_new),
	url(r'^food/photo/delete/(?P<pk>[0-9]+)/$', views.food_photo_delete),
	url(r'^company/photo/delete/(?P<pk>[0-9]+)/$', views.company_photo_delete),
	url(r'^company/photo/new/$', views.company_photo_new),
	url(r'^tag/(?P<pk>[0-9]+)/$', views.tag_entry),
	url(r'^tag/list/$', views.tag_list),
	url(r'^tag/new/$', views.tag_new),
	url(r'^api/companies/$', views.CompanyList.as_view(), name='company-list'),
	url(r'^api/company/(?P<pk>[0-9]+)/$', views.CompanyEntry.as_view()),
	url(r'^api/foods/$', views.FoodList.as_view(), name='food-list'),
	url(r'^api/food/(?P<pk>[0-9]+)/$', views.FoodEntry.as_view()),
	url(r'^api/foodmaps/$', views.FoodMapList.as_view(), name='foodmap-list'),
	url(r'^api/foodmap/(?P<pk>[0-9]+)/$', views.FoodMapEntry.as_view()),
	url(r'^api/users/$', views.UserList.as_view(), name='user-list'),
	url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserEntry.as_view()),
	url(r'^api/$', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]