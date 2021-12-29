from django.urls import re_path,path
from . import views

app_name = 'Users'
urlpatterns = [
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^logout/$', views.logout, name='logout'),
    re_path(r'^profile/(?P<pk>\d+)/$',views.profile, name='profile'),
    re_path(r'^profile/update/(?P<pk>\d+)/$',views.profile_update, name='profile_update'),
    re_path(r'^profile/paschange/(?P<pk>\d+)/$',views.paschange, name='pas_change'),
]