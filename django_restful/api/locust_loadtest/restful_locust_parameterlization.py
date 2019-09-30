# -*-coding:utf-8 -*-
# File :restful_locust_parameterlization.py
# Author:George
# Date : 2019/1/17
# motto: Someone always give up while someone always try!
"""
    将用户参数化
    例如:
    http://127.0.0.1:8000/api/users/1
    http://127.0.0.1:8000/api/users/2
    http://127.0.0.1:8000/api/groups/1
    http://127.0.0.1:8000/api/groups/1
    四组参数  找到相同和不同部分 进行操作
"""
from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    """
    定义用户行为类
    """

    def on_start(self):
        """
        设置user和group参数下标初始值
        相当于 unittest中的setUp()方法
        :return:
        """
        self.users_index = 0
        self.groups_index = 0

    @task
    def test_users(self):
        """
        读取参数
        task 不设置的话  默认就是均重 1:1
        :return:
        """

        users_id = self.locust.id[self.users_index]
        url = '/api/users/' + str(users_id) + '/'
        self.client.get(url, auth=('george', 'kaige1992'))
        # 取余运算循环遍历参数  按照参数取值 self.user_index 在 1 0 1 0 之间循环
        self.users_index = (self.users_index + 1) % len(self.locust.id)

    @task
    def test_groups(self):
        """
        参数化
        :return:
        如果
        """
        groups_id = self.locust.id[self.groups_index]
        url = '/api/groups/' + str(groups_id) + "/"
        self.client.get(url, auth=('george', 'kaige1992'))
        # 同样在遍历参数 通过取余获取下标  再通过下表取值
        self.groups_index = (self.groups_index + 1) % len(self.locust.id)


class WebsiteUser(HttpLocust):
    """
    定义常用参数  当users 和 groups 的长度不一致时 需要将 id 列表单独定义 单独使用如 users_id = [1,2,3] groups_id = [1,2] 然后再分别调用
    """
    # 指向 UserBehavior
    task_set = UserBehavior
    # 设置 id
    id = [1, 2]
    # 最小等待时间
    min_wait = 3000
    # 最大等待时间
    max_wait = 6000

    # 在 WebsiteUser 里面直接定义host主机  直接定义主机即可
    host = 'http://127.0.0.1:8000'
