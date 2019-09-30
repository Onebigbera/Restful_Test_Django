from django.shortcuts import render

"""
    使用viewsets来编写视图函数
"""
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from book.serializers import BookSerializer
from book.models import Book


class BookViewSet(viewsets.ModelViewSet):
    """
        指定queryset和序列化器类
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True)
    def change_name(self, requests, *args, **kwargs):
        get = requests.GET
        book = self.get_object()
        book.name = get.get('newName')
        book.save()

        return Response(book.name)

    @action(detail=False)
    def filter_book(self, request):
        books = Book.objects.filter(book_id__in=range(3))
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
