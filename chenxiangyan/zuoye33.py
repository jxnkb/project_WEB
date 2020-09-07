#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

from selenium import webdriver
import os
dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/user/register.html')
# e=dr.find_element_by_link_text('登陆')
# print(e.get_attribute('href'))
# dr.quit()

# dr.get('http://39.96.181.61/qftest-ds/user/register.html')
# e=dr.find_element_by_link_text('立即注册')
# print(e.get_attribute('href'))
# dr.quit()

dr.get('http://39.96.181.61/qftest-ds/user/register.html')
e=dr.find_element_by_link_text('首页')
print(e.get_attribute('href'))
dr.quit()

# dr.get('http://39.96.181.61/qftest-ds/user/register.html')
# e=dr.find_element_by_link_text('触屏版')
# print(e.get_attribute('href'))
# dr.quit()

dr.get('http://39.96.181.61/qftest-ds/user/login.html')
e=dr.find_element_by_link_text('忘记密码？')
print(e.get_attribute('href'))
dr.quit()