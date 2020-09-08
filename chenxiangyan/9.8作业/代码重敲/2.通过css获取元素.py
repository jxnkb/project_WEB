#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
import os
# dr=webdriver.Firefox()
# dr.get('file:///'+os.path.abspath('h2.html'))
# e=dr.find_element_by_css_selector('p.content')
# e=dr.find_element_by_css_selector('a.mya')
#
# print(e.get_attribute('href'))

# dr.quit()

#案例:在百度上找一个元素,用css方式
# dr=webdriver.Firefox()
# dr.get('https://www.baidu.com')
# e=dr.find_element_by_css_selector('div.s-isindex-wrap')
# print(e.get_attribute('class'))
# dr.quit()

dr=webdriver.Firefox()
dr.get('file:///'+os.path.abspath('h2.html'))
e=dr.find_element_by_css_selector('p.myb.myc.myd')
print(e.get_attribute('id'))
dr.quit()







