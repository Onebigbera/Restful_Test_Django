# -*-coding:utf-8 -*-
# File :urls.py
# Author:George
# Date : 2019/1/15
# motto: Someone always give up while someone always try!
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from book import views
router = DefaultRouter()
# 当使用 viewsets来写视图函数时，二级路由在这里
router.register(r'books', views.BookViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]