# -*-coding:utf-8 -*-
# File :serializers.py
# Author:George
# Date : 2019/1/15
# motto: Someone always give up while someone always try!
"""
    序列化器可以将模型转换成需要返回的json、xml格式类型数据，在app下面创建该文件
"""
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    创建模型类的序列化器对象
    """
    class Meta:
        # 指出需要序列化的模型
        model = Product
        # 指定需要展示的字段
        fields = ('pro_id','name','price','describe', 'isDeleted')
