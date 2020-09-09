#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
'''
3.选择下列列表中的元素有三种方式
• select_by_index() #索引
• select_by_visible_text()#文本
• select_by_value()#value属性的值
'''
from selenium import webdriver
import os
from selenium.webdriver.support.select import Select
import time
dr=webdriver.Firefox()
dr.get('file:///'+os.path.abspath('01HTML/09HTML.html'))
e=dr.find_element_by_name('sel')
time.sleep(3)
#把元素转换成为列表
liste=Select(e)
#通过下标选择选项
liste.select_by_index(0)
#通过value值来选择选项
liste.select_by_value('aaaa')
#通过文本获取选项
liste.select_by_visible_text('北京烤鸭')

