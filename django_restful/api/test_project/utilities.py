# -*-coding:utf-8 -*-
# File :utilities.py
# Author:George
# Date : 2019/1/16
# motto: Someone always give up while someone always try!
"""
    将需要完善的函数写在这里
"""
import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText


def send_mail(latest_report):
    """
    将最近生成的测试报告发送的函数
    :param latest_report:最近生成文件的路径
    :return:
    """
    fr = open(latest_report, "rb")
    mail_content = fr.read()
    fr.close()

    smtpServer = "smtp.163.com"

    account = "onebigbera@163.com"
    password = "george9527"

    sender = "onebigbera@163.com"
    receiver = "onebigbera@163.com"

    subject = "Web Selenium自动化测试报告"
    msg = MIMEText(mail_content, "html", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = sender
    msg["To"] = receiver

    smtp = smtplib.SMTP_SSL(smtpServer, 465)
    smtp.helo(smtpServer)
    smtp.ehlo(smtpServer)
    smtp.login(account, password)
    try:
        print("开始发送邮件...")
        smtp.sendmail(sender, receiver, msg.as_string())
    except BaseException as e:
        print(e)
    print("邮件发送完成...")


def latest_report(report_dir):
    """
    在汇报目录下寻找最新的测试报告的函数
    :param report_dir:
    :return: 返回最近生成文件的路径
    """
    lists = os.listdir(report_dir)
    # lambda 函数返回的是report_dir目录下文件fn的创建时间 sort 函数中按照key=time进行排序,注意匿名函数lambda的用法
    lists.sort(key=lambda fn: os.path.getatime(report_dir + "\\" + fn))
    print("最近生成的汇报文件为:%s" % lists[-1])

    # 用 os.path.join()方法将最近生成文件的路径拼接起来
    file = os.path.join(report_dir, lists[-1])
    print("最近生成的文件路径为: %s" % file)
    return file


d