#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
import os
import csv
import time

with open('data.csv','r',encoding='utf-8') as f:
    data=csv.reader(f)
    mylist=[]
    for d in data:
        mylist.append(d[0])
    print(mylist)

    dr=webdriver.Firefox()
    #打开网络
    dr.get('http://39.96.181.61/qftest-ds/')
    time.sleep(2)
    #获取免费注册元素并点击
    dr.find_element_by_link_text('免费注册').click()
    time.sleep(3)
    # 获取用户名输入框,并输入数据
    dr.find_element_by_id('username').send_keys(mylist[0])
    time.sleep(2)
    # 获取邮箱输入框,并输入数据
    dr.find_element_by_id('email').send_keys(mylist[1])
    time.sleep(2)
    # 获取密码输入框,并输入数据
    dr.find_element_by_id('password').send_keys(mylist[2])
    time.sleep(2)
    # 获取确认密码输入框,并输入数据
    dr.find_element_by_id('repassword').send_keys(mylist[3])
    time.sleep(2)
    # 获取'立即注册'元素,并点击
    dr.find_element_by_link_text('立即注册').click()

    # 休眠一下
    time.sleep(9)

    # 获取断言的url
    myurl = mylist[4]

    if dr.current_url == myurl:
        print("测试用例ok")
    else:
        print("测试用例错误")

    time.sleep(2)

    dr.quit()

