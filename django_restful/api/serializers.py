# -*-coding:utf-8 -*-
# File :serializers.py
# Author:George
# Date : 2019/1/15
# motto: Someone always give up while someone always try!
"""
    序列化器，将User和Group表进行重新设计
"""
# 使用django 自带的 User 和 Group 表
# from django.contrib.auth.models import User, Group
from rest_framework import serializers
# 使用自定义的 User和Group表
from api.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    继承serializer.HyperlinkedModelSerializer,重写User类
    """

    class Meta:
        """模型指向User"""
        model = User
        # 如果做了修改 此处要一起更改 虽然url字段我们在模型中没有定义，但是其会自动生成
        fields = ('url', 'username', 'email')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    继承serializer.HyperlinkedModelSerializer 将 Group 重写
    """

    class Meta:
        """模型指向Group"""
        model = Group
        # 自定义字段 url是我们自定义的API
        fields = "__all__"
