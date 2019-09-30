# -*-coding:utf-8 -*-
# File :test_unittest_restful.py
# Author:George
# Date : 2019/1/16
# motto: Someone always give up while someone always try!
"""
    数据初始化封装后完整的测试类的封装
    测试用例必须使用 test 开头
    在 test 后面接00n 用来控制测试用例执行顺序
    调试的时候需要单个都调试成功
"""
import requests
import unittest
import yaml
from mysql_action import DB
import logging


class UserTest(unittest.TestCase):
    """
    对序列化的User类的测试 UserViewSet对象的测试
    ctrl + r(replace) 批量替换
    """

    def setUp(self):
        """
        定义User类中基本的url和授权信息
        :return:
        """

        self.base_url = 'http://127.0.0.1:8000/api/users'
        self.auth = ('george', 'kaige1992')

    def test_001_get_user(self):
        """
        向服务器请求数据 幂等性且安全
        :return:
        """
        logging.info("=========test_001_get_user==========")
        r = requests.get(self.base_url + '/1/', auth=self.auth)
        # Returns the json-encoded content of a response in python object
        result = r.json()

        self.assertEqual(result['username'], 'george')
        self.assertEqual(result['email'], 'george@163.com')

    def test_002_add_user(self):
        """
        参照着生成的API文档操作 非幂等性 非安全性
        :return:
        """
        logging.info("=========test_002_add_user==========")
        form_data = {"username": "jordan", 'email': 'jordan123@qq.com'}
        # 不需要添加 id 只需要加上'/' 即可
        r = requests.post(self.base_url + '/', data=form_data, auth=self.auth)
        result = r.json()

        self.assertEqual(result['username'], 'jordan')
        self.assertEqual(result['email'], 'jordan123@qq.com')

    def test_003_update_user(self):
        """
        修改用户信息,注意要把 post 提交用户信息 在此时不能再提交
        :return:
        """
        logging.info("=========test_003_update_user==========")
        form_data = {'email': 'steven@gmail.com'}
        r = requests.patch(self.base_url + '/2/', data=form_data, auth=self.auth)
        result = r.json()

        self.assertEqual(result['email'], 'steven@gmail.com')
        self.assertEqual(result['username'], 'steven')

    def test_004_delete_user(self):
        """
        删除用户信息 一般企业中不会让你真正删除信息都是 根据字段 idDeleted 的状态变更 在 url 中指定数据 id 即可
        :return:
        """
        logging.info("=========test_004_delete_user==========")
        r = requests.delete(self.base_url + '/2/', auth=self.auth)
        # 响应信息为空 使用 r.json 会现实编码错误 直接根据状态码判断更好
        # result = r.json()

        self.assertEqual(r.status_code, 204)

    def test_005_no_auth(self):
        """
        测试在未授权情况
        :return:
        """
        logging.info("=========test_005_no_auth==========")
        r = requests.get(self.base_url)
        result = r.json()

        # 注意 detail会因为项目设置的语言(ZH-Hans| en-us) 而导致语言差异
        self.assertEqual(result['detail'], '身份认证信息未提供。')

    # def tearDown(self):
    #     pass


class GroupTest(unittest.TestCase):

    def setUp(self):
        """
        定义根url和认证信息
        :return:
        """

        self.base_url = 'http://127.0.0.1:8000/api/groups'
        self.auth = ('george', 'kaige1992')

    def test_001_group_developer(self):
        """

        :return:
        """
        logging.info("=========test_001_group_developer==========")
        r = requests.get(self.base_url + "/1/", auth=self.auth)
        result = r.json()

        self.assertEqual(result['url'], 'http://127.0.0.1:8000/api/groups/1/')
        self.assertEqual(result['name'], 'Developer')

    def test_002_add_group(self):
        """
        测试增加用户组
        定义用户组信息 使用POST请求 发送请求
        不用指定url 系统会自己分配url
        :return:
        """
        logging.info("=========test_002_add_group==========")
        form_data = {'name': "Engineer"}
        r = requests.post(self.base_url + '/', data=form_data, auth=self.auth)
        result = r.json()

        self.assertEqual(result['name'], 'Engineer')
        # self.assertEqual(result['url'], 'http://127.0.0.1:8000/api/groups/3/')

    def update_003_update_group(self):
        """
        局部更新请求
        :return:
        """
        logging.info("=========update_003_update_group==========")
        form_data = {'name': "Blue"}
        r = requests.patch(self.base_url + '/2/', data=form_data, auth=self.auth)
        result = r.json()

        self.assertEqual(result['name'], "Blue")

    def test_004_delete_group(self):
        """
        删除指定的id的群组
        :return:
        """
        logging.info("=========test_004_delete_group==========")
        r = requests.delete(self.base_url + '/2/', auth=self.auth)
        # 空对象使用.json()报错
        # result = r.json()

        # 删除信息后成功返回状态码为204
        self.assertEqual(r.status_code, 204)

    def test_005_no_auth(self):
        """
        未认证情况下
        :return:
        """
        logging.info("=========test_005_no_auth==========")
        r = requests.get(self.base_url + '/')
        result = r.json()

        self.assertEqual(result['detail'], '身份认证信息未提供。')
    #
    # def tearDown(self):
    #     pass


if __name__ == "__main__":
    db = DB()
    fr = open('datas.yaml', 'r')
    datas = yaml.load(fr)
    db.init_data(datas)
    unittest.main()
"""
    运行测试时不要点击 Run 'Unittest in test_django_restful' 直接点击 if __name__ == "__main__" 右边的按钮  选择 Run 'test_django_restful'
"""