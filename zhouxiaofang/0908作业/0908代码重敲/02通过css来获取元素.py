#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#案例:自己写个有超链接的标签,通过class样式,找到该标签的href属性值
from selenium import webdriver
import os
# dr=webdriver.Firefox()
# dr.get("file:///"+os.path.abspath("01HTML/02HTML.html"))
# # e=dr.find_element_by_css_selector('p.content') #maker
# e=dr.find_element_by_css_selector('a.mya') #https://www.baidu.com/
# print(e.get_attribute('href'))
# # print(e.get_attribute('id'))
# dr.quit()


#案例:在百度上找一个元素,用css方式
dr=webdriver.Firefox()
dr.get('https://www.baidu.com')
e=dr.find_element_by_css_selector('div.s-isindex-wrap')
print(e.get_attribute('class')) #s-top-wrap s-isindex-wrap
dr.quit()
