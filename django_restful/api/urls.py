# -*-coding:utf-8 -*-
# File :urls.py
# Author:George
# Date : 2019/1/15
# motto: Someone always give up while someone always try!
"""
    使用 viewsets 方式的路由写法
"""
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api import views
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

schema_view = get_schema_view(title="API", renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

router = DefaultRouter()
# users就是二级路由
router.register(r'users', views.UserViewSet)

# groups就是二级路由
router.register(r'groups', views.GroupViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs/', schema_view, name='docs'),
]
