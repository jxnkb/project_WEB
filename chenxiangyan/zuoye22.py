#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
from time import sleep
import os
dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/')
# e=dr.find_element_by_id('logined-userbar-tpl')
# print(e.get_attribute('type'))
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/user/login.html')
# e=dr.find_element_by_id('password')
# print(e.get_attribute('name'))
# dr.quit()

#dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/user/login.html')
# e=dr.find_element_by_id('username')
# print(e.get_attribute('type'))
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/user/login.html')
# e=dr.find_element_by_id('login-form')
# print(e.get_attribute('method'))
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/user/register.html')
# e=dr.find_element_by_id('repassword')
# print(e.get_attribute('type'))
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/user/register.html')
# e=dr.find_element_by_name('keywords')
# print(e.get_attribute('content'))
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/user/register.html')
# e=dr.find_element_by_id('description')
# print(e.get_attribute('content'))
# dr.quit()

dr=webdriver.Firefox()
dr.get('http://39.96.181.61/qftest-ds/user/register.html')
e=dr.find_element_by_id('username')
print(e.get_attribute('type'))
dr.quit()

dr=webdriver.Firefox()
dr.get('http://39.96.181.61/qftest-ds/user/register.html')
e=dr.find_element_by_id('email')
print(e.get_attribute('type'))
dr.quit()

dr=webdriver.Firefox()
dr.get('http://39.96.181.61/qftest-ds/user/register.html')
e=dr.find_element_by_id('agree')
print(e.get_attribute('type'))
dr.quit()
