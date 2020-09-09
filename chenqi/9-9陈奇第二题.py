#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#二．自动化登入电商系统后台,登入后截图
#注意：网站,用户名和密码要通过代码获取
f=open('环境.txt','r')
list=f.read().splitlines()
# print(list)
from selenium import webdriver
from time import sleep
dr=webdriver.Firefox()
dr.get(list[1])
# dr.switch_to.frame('login')
s=dr.find_element_by_id('username')
s.send_keys(list[3])
s1=dr.find_element_by_id('password')
s1.send_keys(list[5])
e=dr.find_element_by_link_text('登 陆').click()
sleep(5)
dr.get_screenshot_as_file('03.png')
dr.quit()