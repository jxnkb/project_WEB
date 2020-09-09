#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import os

#获取文件
f=open('C:\\Users\Joseph\Desktop\电商系统-阿里云环境.txt','r')
a=f.read().splitlines()
url=a[1]
root=a[3]
pw=a[5]
front=a[-1]

d=webdriver.Firefox()

def admin_login():
    from selenium import webdriver
    from time import sleep
    from selenium.webdriver.common.keys import Keys
    import os
    f = open('C:\\Users\Joseph\Desktop\电商系统-阿里云环境.txt', 'r')
    a = f.read().splitlines()
    url = a[1]
    root = a[3]
    pw = a[5]
    d.get(url)
    a=d.find_element_by_id('username')
    a.send_keys(root)
    b=d.find_element_by_id('password')
    b.send_keys(pw)
    d.find_element_by_partial_link_text('登 陆').click()

admin_login()
sleep(6)
d.get_screenshot_as_file('jt1.png')
d.close()

def user_login():
    from selenium import webdriver
    from time import sleep
    from selenium.webdriver.common.keys import Keys
    import os
    f = open('C:\\Users\Joseph\Desktop\电商系统-阿里云环境.txt', 'r')
    a = f.read().splitlines()
    front = a[-1]
    d.get(front)
    d.find_element_by_partial_link_text('登陆').click()
    a=d.find_element_by_id('username')
    a.send_keys('jxnkb')
    b=d.find_element_by_id('password')
    b.send_keys('1qaz2wsx')
    d.find_element_by_partial_link_text('登     陆').click()


user_login()
sleep(6)
a=d.find_element_by_name('kw')
a.send_keys('苹果')
a.submit()
sleep(3)
d.find_element_by_partial_link_text('苹果').click()
sleep(2)
d.find_element_by_partial_link_text('加入购物车').click()
sleep(2)
d.get_screenshot_as_file('pg.png')
d.quit()