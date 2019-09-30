# -*-coding:utf-8 -*-
# File :viewsets.py
# Author:George
# Date : 2019/1/15
# motto: Someone always give up while someone always try!
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Text
from .serializers import TextSerializers


class TextViewSet(viewsets.ModelViewSet):
    """要展示的数据类"""
    queryset = Text.objects.all()
    serializer_class = TextSerializers

    # 设为全部认证
    permission_classes = (IsAuthenticated,)

    # 定义一个更改名称的函数
    @action(detail=True)
    def change_name(self, request, *args, **kwargs):
        get = request.GET
        text = self.get_object()
        text.title = get.get('newName')
        text.save()
        return Response(text.title)

    @action(detail=False)
    def filter_text(self, request):
        texts = Text.objects.filter(text_id__in=range(3))
        serializer = TextSerializers(texts, many=True)
        return Response(serializer.data)
