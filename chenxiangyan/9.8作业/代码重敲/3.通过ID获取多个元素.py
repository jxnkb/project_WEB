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
dr.get('file:///'+os.path.abspath('h3.html'))
e=dr.find_elements_by_id('maker')
print(type(e))
print(e[0].get_attribute('name'))
dr.quit()

#自己写一个html文件,定义两个id属性值相同的标签,通过id获取多个元素,然后打印出各自其他的属性
dr=webdriver.Firefox()
dr.get('file:///'+os.path.abspath('h3.html'))
e=dr.find_elements_by_id('code')
for i in e:
    print(i.get_attribute('name'))
    dr.quit()

dr=webdriver.Firefox()
dr.get('http://www.baidu.com')
e=dr.find_elements_by_id('wrapper')
print(len(e))