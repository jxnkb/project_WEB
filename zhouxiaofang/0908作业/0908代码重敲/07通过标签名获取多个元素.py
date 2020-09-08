#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
import time
# dr=webdriver.Firefox()
# dr.get('https://www.baidu.com')
# e=dr.find_elements_by_tag_name('div')
# print(len(e))
# dr.quit()

#案例:获取淘宝首页有多少个div,并打印出div里的id属性值
dr=webdriver.Firefox()
dr.get("https://www.taobao.com")
e=dr.find_elements_by_tag_name('div')
time.sleep(5)
print(len(e))
print("-----------")
for i in e:
    if i.get_attribute('id'):
        print(i.get_attribute('id'))
dr.quit()
