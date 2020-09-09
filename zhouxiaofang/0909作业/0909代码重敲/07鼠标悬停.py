#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains

dr=webdriver.Firefox()
dr.get('https://www.baidu.com')
e=dr.find_element_by_tag_name('span')
print(e.get_attribute('id'))
e=dr.find_element_by_link_text('更多')

#鼠标悬停:move_to_element
ActionChains(dr).move_to_element(e).perform()
