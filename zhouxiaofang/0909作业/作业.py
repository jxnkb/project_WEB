#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# 二．	自动化登入电商系统后台,登入后截图
# 注意：网站,用户名和密码要通过代码获取
f=open('1.txt','r',encoding='gbk')
a=f.read().splitlines()
# print(a)
url=a[1]
username=a[3]
passwd=a[5]
# print(url,username,passwd)

from selenium import webdriver
from time import sleep
dr=webdriver.Firefox()
dr.get(url)
#获取用户名输入框元素
e=dr.find_element_by_id('username')
#输入用户名
e.send_keys(username)
sleep(3)
#获取密码输入框元素
e2=dr.find_element_by_id('password')
#输入密码
e2.send_keys(passwd)
sleep(3)
#点击登陆
e4=dr.find_element_by_link_text('登 陆')
e4.click()
sleep(8)
#截图
dr.get_screenshot_as_file('c.png')
dr.quit()

# 三．	自动化登入电商系统前台，把苹果加入到购物车
# 注意：网站要通过代码获取
f=open('1.txt','r',encoding='gbk')
b=f.read().splitlines()
# print(b)
url2=b[7]
from selenium import webdriver
from time import sleep
dr=webdriver.Firefox()
dr.get(url2)
e=dr.find_element_by_name('kw')
# print(e.get_attribute('class'))
#输入框输入'苹果'
e.send_keys('苹果')
sleep(3)
#提交
e.submit()
sleep(3)
#获取苹果元素
e2=dr.find_element_by_xpath("//div[@class='im']/a/img")
#点击苹果
e2.click()
sleep(3)
#获取加入购物车元素
e3=dr.find_element_by_xpath("//div[@class='buy mt30']/a[@class='add-cart icon']")
#点击加入购物车
e3.click()
sleep(5)
#截图
dr.get_screenshot_as_file('d.png')
dr.quit()