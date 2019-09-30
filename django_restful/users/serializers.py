# -*-coding:utf-8 -*-
# File :serializers.py
# Author:George
# Date : 2019/1/15
# motto: Someone always give up while someone always try!
"""
    serializers.py 序列化器文件 对models进行序列化
"""
from rest_framework import serializers
from .models import Text,Author

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        # 指向模型为 models.py 中的 'Author'类
        model = Author
        # 所有字段都展示
        fields = "__all__"


class TextSerializers(serializers.ModelSerializer):

    # 设置author查询
    author = AuthorSerializers()

    class Meta:
        """fields是筛选指定字段 可以全选，也可以自定义"""
        model = Text
        fields = "__all__"






