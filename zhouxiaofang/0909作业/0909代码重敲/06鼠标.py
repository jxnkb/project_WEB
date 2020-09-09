#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

dr=webdriver.Firefox()
# dr.get('https://www.baidu.com')
# e=dr.find_element_by_tag_name('body')
# #在百度页面空白部分 鼠标右键单击
# ActionChains(dr).context_click(e).perform()
# dr.quit()

dr.get('file:///'+os.path.abspath('01HTML/06HTMLl.html'))
e=dr.find_element_by_xpath('//input[@value="按键2"]')
#鼠标左键双击
ActionChains(dr).double_click(e).perform()