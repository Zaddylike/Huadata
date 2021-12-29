from django.urls import path,re_path
from . import views

app_name = 'pic_upload'

urlpatterns = [

    path('',views.PicList.as_view(), name='pic_list'),

    re_path(r'^pic/upload/$',views.PicUpload.as_view(),name='pic_upload'),

    re_path(r'^pic/(?P<pk>\d+)/$',views.PicDetail.as_view(),name='pic_detail'),

]