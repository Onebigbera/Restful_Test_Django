from django.test import TestCase

# Create your tests here.
import requests
import unittest
from django.test import TestCase

"""
    (1)测试用例的编写是一样的 就是继承的父类为 django自带的TestCase, TestCase类其实是unittest.TestCase 的后代类
    运行django 项目下面的所有的test.py  >python manage.py test
    (2)测试指定的测试类    python manage.py test api.tests.UserTest (app名称.模块名称.测试类)
    (3)测试具体的某一条测试用例   python manage.py test api.tests.UserTest.test_1group_developer（app名称.模块名称.测试类名.类的方法名称）
    (4) @unittest.skip("reason") 装饰器可以对 Django 中的 TestCase用例的测试用例生效
"""


# @TestCase.skipTest('test_case')
class UserTest(TestCase):
    """
    对序列化的User类的测试 UserViewSet对象的测试
    """

    def setUp(self):
        """
        定义User类中基本的url和授权信息
        :return:
        """
        self.base_url = 'http://127.0.0.1:8000/api/users'
        self.auth = ('george', 'kaige1992')

    @unittest.skip('to skip this case...')
    def test_1get_user(self):
        """
        向服务器请求数据 幂等性且安全
        :return:
        """
        r = requests.get(self.base_url + '/1/', auth=self.auth)
        result = r.json()

        # 断言检验
        self.assertEqual(result['username'], 'george')
        self.assertEqual(result['email'], '2578288992@qq.com')

    @unittest.skip('to skip this case...')
    def test_2add_user(self):
        """
        参照着生成的API文档操作 特别是 groups的值,非幂等性 非安全性
        :return:
        """
        form_data = {"username": "jordan", 'email': 'jordan123@qq.com', 'groups': 'http://127.0.0.1:8000/api/groups/1/'}
        # 不需要添加 id 只需要加上'/' 即可
        r = requests.post(self.base_url + '/', data=form_data, auth=self.auth)
        result = r.json()

        # 虽然并没有 KeyError 但是报错为 KyeError todo
        self.assertEqual(result['username'], 'jordan')
        self.assertEqual(result['email'], 'jordan123@qq.com')
        self.assertEqual(result.get('username', 'jordan'), 'jordan')
        self.assertEqual(result.get('email', 'jordan123@qq.com'), 'jordan123@qq.com')

    def test_3update_user(self):
        """
        修改用户信息,注意要把 post 提交用户信息 在此时不能再提交
        :return:
        """
        # 定义修改的字段
        form_data = {'email': 'jordan@163.com'}
        r = requests.patch(self.base_url + '/5/', data=form_data, auth=self.auth)
        result = r.json()

        self.assertEqual(result['email'], 'jordan@163.com')
        self.assertEqual(result['username'], 'jordan')

    @unittest.skip('to skip this case...')
    def test_4delete_user(self):
        """
        删除用户信息 一般企业中不会让你真正删除信息都是 根据字段 idDeleted 的状态变更 在 url 中指定数据 id 即可
        :return:
        """
        r = requests.delete(self.base_url + '/5/', auth=self.auth)
        # 响应信息为空 使用 r.json 会现实编码错误 直接根据状态码判断更好
        # result = r.json()

        self.assertEqual(r.status_code, 204)

    def test_5no_auth(self):
        """
        测试在未授权情况
        :return:
        """
        r = requests.get(self.base_url)
        result = r.json()

        # 注意 detail会因为项目设置的语言(ZH-Hans| en-us) 而导致语言差异
        self.assertEqual(result['detail'], '身份认证信息未提供。')

    def tearDown(self):
        pass


class GroupTest(TestCase):

    def setUp(self):
        """
        定义根url和认证信息
        :return:
        """
        self.base_url = 'http://127.0.0.1:8000/api/groups'
        self.auth = ('george', 'kaige1992')

    def test_1group_developer(self):
        """

        :return:
        """
        r = requests.get(self.base_url + "/1/", auth=self.auth)
        result = r.json()

        self.assertEqual(result['url'], 'http://127.0.0.1:8000/api/groups/1/')
        self.assertEqual(result['name'], 'Tester')

    @unittest.skip('To skip the case for other case...')
    def test_2add_group(self):
        """
        测试增加用户组
        定义用户组信息 使用POST请求 发送请求
        不用指定url 系统会自己分配url
        :return:
        """
        form_data = {'name': "Unittest"}
        r = requests.post(self.base_url + '/', data=form_data, auth=self.auth)
        result = r.json()

        self.assertEqual(result['name'], 'Unittest')
        self.assertEqual(result['url'], 'http://127.0.0.1:8000/api/groups/3/')

    def update_3update_group(self):
        """
        局部更新请求
        :return:
        """
        form_data = {'name': "Blue"}
        r = requests.patch(self.base_url + '/3/', data=form_data, auth=self.auth)
        result = r.json()

        self.assertEqual(result['name'], "Blue")

    @unittest.skip('do\'not delete source twice!')
    def test_3delete_group(self):
        """
        删除指定的id的群组
        :return:
        """
        r = requests.delete(self.base_url + '/3/', auth=self.auth)
        # result = r.json()

        # 删除信息后成功返回状态码为204
        self.assertEqual(r.status_code, 204)

    def test_4no_auth(self):
        """
        未认证情况下
        :return:
        """
        r = requests.get(self.base_url)
        result = r.json()

        self.assertEqual(result['detail'], '身份认证信息未提供。')

    def tearDown(self):
        pass
