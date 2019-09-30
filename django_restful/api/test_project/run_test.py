# -*-coding:utf-8 -*-
# File :run_test.py
# Author:George
# Date : 2019/1/16
# motto: Someone always give up while someone always try!
"""
    控制测试用例的执行
    将BSTestRunner.py模块放到
"""
import unittest
from BSTestRunner import BSTestRunner
from mysql_action import DB
import yaml
import time
import logging.config

CON_LOG = 'log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def run_test():
    """
    定义运行测试的函数
    :return:
    """

    # 数据初始化
    db = DB()
    with open('datas.ymal', 'r') as fr:
        datas = yaml.load(fr)
        db.init_data(datas)

    test_dir = '.'
    report_dir = "./reports/"

    # 执行测试
    discovery = unittest.defaultTestLoader.discover(test_dir, pattern="test_django_restful.py", )
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    report_path = report_dir + now + "test_report.html"
    with open(report_path, 'wb') as fw:
        runner = BSTestRunner(stream=fw, title="Django_api_test", description="Django_restful_API_Test_rport")
        logging.info("=========Start API Test==========")

        runner.run(discovery)
        logging.info("=========Finish API Test==========")


if __name__ == "__main__":
    run_test()
