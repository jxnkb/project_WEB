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
dr.get("file:///"+os.path.abspath('01HTML/02HTML.html'))
e=dr.find_element_by_id('maker')
print(e.get_attribute('id'))  #maker
print(e.get_attribute('lala')) #aaa
print(e.get_property('id'))   #maker
#get_property不能获取自己定义的元素属性
print(e.get_property('lala')) #None