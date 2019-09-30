# -*-coding:utf-8 -*-
# File :serializers.py
# Author:George
# Date : 2019/1/15
# motto: Someone always give up while someone always try!
"""
    将模型序列化 转化成xml、json类型数据
"""
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:

        model = Book
        # 指定展示所有的字段
        fields = "__all__"

