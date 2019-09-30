# -*-coding:utf-8 -*-
# File :urls.py
# Author:George
# Date : 2019/1/15
# motto: Someone always give up while someone always try!
"""
    使用Router自动处理url和view的连接
"""
from django.conf.urls import url,include
from product import views

# product app url 配置
urlpatterns = [
    url(r'^test/$', views.GetMessageView.as_view()),
]

