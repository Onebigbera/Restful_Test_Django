# -*-coding:utf-8 -*-
# File :restful_api_locust.py
# Author:George
# Date : 2019/1/17
# motto: Someone always give up while someone always try!
from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    """
    @task(1) 装饰器代表分配负载的压力百分比
    定义一个用户行为类
    """

    @task(2)
    def test_users(self):
        self.client.get('/api/users/', auth=('george', 'kaige1992'))

    @task(1)
    def test_group(self):
        """
        注意自己定义的路由
        :return:
        """
        self.client.get('/api/groups/', auth=('george', 'kaige1992'))


class WebsiteUser(HttpLocust):
    """
    这个类用来配置最大、最小响应时间 指定用户行为类
    task_set: 指向一个定义的用户行为类
    min_wait: 执行事务之间用户等待时间的下限(单位：毫秒)
    max_wait: 执行事务之间用户等待时间的上限(单位：毫秒)
    """
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000


"""
    命令行执行:
    locust -f file_path(xxx/restful_locust.py) --host=http://127.0.0.1:8000
"""
