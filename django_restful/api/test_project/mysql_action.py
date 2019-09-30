# -*-coding:utf-8 -*-
# File :mysql_action.py
# Author:George
# Date : 2019/1/16
# motto: Someone always give up while someone always try!
"""
    mysql 数据库相关的初始化操作
    使用 ymal(Yet Another Markdown Language )
    养成一遍写代码一遍测试的习惯 不能等代码完成了很多再测试 会极大地浪费时间和精力
"""

from pymysql import connect
import yaml
# from run_test import logging
import logging


class DB(object):
    """
    封装数据库操作的类
    """

    def __init__(self):
        logging.info("==============init data=========")
        logging.info("connect db...")
        # 创建连接对象
        self.conn = connect(host='127.0.0.1', user='root', password='george9527', db='django_restful_test')

    def clear(self, table_name):
        logging.info('clear db_table {}...'.format(table_name))
        # 需要执行的SQL语句 truncate:清除表数据和记录, 注意使用纯字符串凭拼接 truncate 和表名之间有个空格
        # clear_sql = 'truncate' + " "+table_name + ';'
        clear_sql = "truncate {};".format(table_name)

        # 创建游标执行SQL语句
        with self.conn.cursor() as cursor:
            # 清除外键
            cursor.execute('set foreign_key_checks=0;')
            cursor.execute(clear_sql)

    def insert(self, table_name, table_data):
        logging.info("==============insert data=========")
        for key in table_data:
            # 格式处理-将 key 对应的值转变为字符串格式并加上单引号
            table_data[key] = "'" + str(table_data[key]) + "'"
            # logging.info(type(table_data[key]))
        # 将字典的keys 连接起来变为字符串
        str_keys = ','.join(table_data.keys())
        # logging.info(str_keys)
        logging.info(type(str_keys))  # <class 'str'>
        # 将字典的values连接起来 变为字符串
        str_values = ','.join(table_data.values())
        # logging.info(str_values)
        insert_sql = 'insert into ' + table_name + '(' + str_keys + ')' + 'values' + '(' + str_values + ')' + ';'
        logging.info(insert_sql)
        with self.conn.cursor() as cursor:
            cursor.execute(insert_sql)
        self.conn.commit()

    def close(self):
        logging.info("close db...")
        self.conn.close()
        logging.info("==============init finished =========")

    def init_data(self, datas):
        """
        初始化数据设置
        先将每个数据表清空 然后从yaml文件中读取数据存储到数据库中
        :param data:
        :return:
        """
        logging.info('init db...')
        # 需要得到datas.items()具体 学习ymal语法
        for table, data in datas.items():
            # 每次都先将表中数据清除
            self.clear(table)
            for d in data:
                # 遍历小组 将小组中的每项数据插入到数据库
                self.insert(table, d)


if __name__ == "__main__":
    db = DB()

    # 测试clear()函数是否生效
    # db.clear("group_test")

    # 测试插入数据
    # user_data = {'id': 2, 'username': 'tom', 'email': 'tom@qq.com'}
    # db.insert('user_test', user_data)

    # 测试数据库能否正常关闭
    # db.close()

    # 读取 ymal 文件中的内容 文档流 能够获取table信息和data数据

    # todo : 这是数据库初始化器 保证数据库中没有脏数据
    with open('datas.ymal', 'r') as fr:
        datas = yaml.load(fr)
        db.init_data(datas)
