from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse

"""
    运行项目指令: python manage.py runserver
    
    视图编写方法一: 使用 APIView
"""


class GetMessageView(APIView):

    # get请求
    def get(self, request):
        # 获取参数数据
        get = request.GET

        # 获取参数
        a = get.get('a')

        print(a)
        # 返回信息
        d = {
            'status': 1,
            'message': 'Success',
        }

        return JsonResponse(d)
