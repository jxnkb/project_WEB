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
dr.get("file:///"+os.path.abspath('01HTML/04HTML.html'))
# e=dr.find_elements_by_name('maker')
# print(e[0].get_attribute('id'))
# print(e[1].get_attribute('href'))
# print(len(e))
# dr.quit()

#案例:自己写一个html文件,定义两个name属性值相同的标签,通过name获取多个元素,然后打印出各自其他的属性
dr.get("file:///"+os.path.abspath('01HTML/04HTML.html'))
e=dr.find_elements_by_name('maker')
for i in e:
    print(i.get_attribute('id'))

dr.quit()