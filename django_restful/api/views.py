from django.shortcuts import render
# from django.contrib.auth.models import User, Group
from api.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer

"""
    视图函数 基于 viewsets写法,注释是基于Swagger规范文档生成器中系统中定义好的方法，按照规范书写
"""


class UserViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Return a user instance.

        list:
            Return all users, ordered by most recently joined.
        create:
            create an new user.

        delete:
            Remove an existing user.

        partial_update:
            Update one or more fields on an existing user.

        update:
            Update an user.

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
            retrieve:
                Return a group instance.

            list:
                Return all group, ordered by most recently joined.

            delete:
                Remove an existing group.

            create:
                create an new group.

            partial_update:
                Update one or more fields on an existing group.

            update:
                Update a group.

        """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
