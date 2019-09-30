from django.db import models

"""
    将django自带的auth_user和auth_group变更到自定义的 User 和 Group 表中
"""


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    # groups = models.CharField(max_length=100, default='http://127.0.0.1/api/groups/1/')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user_test'


class Group(models.Model):
    # gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'group_test'
