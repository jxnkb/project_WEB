#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
#后台的网址
# with open('peng.txt','r',encoding='gbk') as f:
#     hwy=f.readline()
#     hwy=f.readline()
#     #print(hwy)
# #账号
# with open('peng.txt','r',encoding='gbk') as f1:
#     a=f1.read().splitlines()
# zh=a[3]
# #print(zh)
# #密码
# with open('peng.txt','r',encoding='gbk') as f1:
#     a=f1.read().splitlines()
# mm=a[5]
# #print(mm)
# dr=webdriver.Firefox()
# dr.get(hwy)
# a=dr.find_element_by_id("username")
# a.send_keys(zh)
# b=dr.find_element_by_id("password")
# b.send_keys(mm)
# #友情提示：用超链接不行
# dr.find_element_by_class_name("btn.unslt").click()
# sleep(2)
# dr.get_screenshot_as_file('1.png')


with open('peng.txt','r',encoding='gbk') as f1:
    a=f1.read().splitlines()
qwy=a[7]
# print(qwy)

dd=webdriver.Firefox()
dd.get(qwy)
a=dd.find_element_by_name('kw')
a.send_keys('苹果')
a.submit()
sleep(2)
e=dd.find_element_by_link_text('苹果').click()
e=dd.find_element_by_link_text('加入购物车').click()
dd.get_screenshot_as_file('2.png')