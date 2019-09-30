from django.contrib import admin
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from api import views
from users import views
from users import urls as users_url

"""
    总的路由文件，
    路由注册 rest_frame 注册
"""
# 实例化路由器
# router = DefaultRouter()

# 注册对象视图集合
# router.register(r'text', views.TextViewSet)
# router.register(r'groups', views.GroupSerializer)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 一级路由，链接到二级路由
    url(r"^", include('product.urls')),
    url(r"^book/", include("book.urls")),
    url(r'^api/', include("api.urls")),
    # api模块认证
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
