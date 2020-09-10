#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#引入模块
from selenium import webdriver
import time
#获取浏览器
dr=webdriver.Firefox()
#打开网站
dr.get('http://39.96.181.61/qftest-ds/')
time.sleep(2)
#获取免费注册元素并点击
dr.find_element_by_link_text('免费注册').click()
time.sleep(3)
#获取用户名输入框,并输入数据
dr.find_element_by_id('username').send_keys('test2')
time.sleep(2)
#获取邮箱输入框,并输入数据
dr.find_element_by_id('email').send_keys('test2@qq.com')
time.sleep(2)
#获取密码输入框,并输入数据
dr.find_element_by_id('password').send_keys('123456')
time.sleep(2)
#获取确认密码输入框,并输入数据
dr.find_element_by_id('repassword').send_keys('123456')
time.sleep(2)
#获取'立即注册'元素,并点击
dr.find_element_by_link_text('立即注册').click()
time.sleep(8)
#获取当前页面的url
url=dr.current_url
print(url)
#进行判断http://39.96.181.61/qftest-ds/user/index.html
if url=='http://39.96.181.61/qftest-ds/user/index.html':
    print("测试用例ok")
else:
    print("测试用例错误")
time.sleep(5)
#关闭浏览器
dr.quit()

