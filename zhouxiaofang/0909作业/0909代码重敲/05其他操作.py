#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
import time
dr=webdriver.Firefox()
# dr.get('https://www.baidu.com')
# e=dr.find_element_by_id('kw')
# e.send_keys('软件测试')
# time.sleep(2)
# #回车
# e.submit()
# #获取页面标题
# print(dr.title)
# #获取页面的地址
# print(dr.current_url)
# time.sleep(2)
# dr.quit()

#案例:在淘宝首页上的搜索栏中输入软件测试,然后按回车,之后打印本页的标题和url
dr.get('https://www.taobao.com')
e=dr.find_element_by_id('q')
e.send_keys('软件测试')
time.sleep(2)
e.submit()
print(dr.title)
print(dr.current_url)
time.sleep(2)
dr.quit()