#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import os

dr=webdriver.Firefox()
# dr.get('file:///'+os.path.abspath('01HTML/10HTML.html'))
# e=dr.find_element_by_name('文本')
# sleep(2)
# #往元素输入内容
# e.send_keys('maker')
# sleep(2)
# #删除一个字付
# e.send_keys(Keys.BACK_SPACE)
# sleep(2)
# #全选
# e.send_keys(Keys.CONTROL,'a')
# sleep(2)
# #剪切
# e.send_keys(Keys.CONTROL,'x')
# sleep(2)
# #粘贴
# e.send_keys(Keys.CONTROL,'v')
# sleep(2)

#案例:在百度搜索栏中,进行输入,删除,全选,剪切,粘贴功能
dr=webdriver.Firefox()
dr.get("https://www.baidu.com")
e=dr.find_element_by_id('kw')
sleep(2)
e.send_keys('丰田车')
sleep(2)
e.send_keys(Keys.BACK_SPACE)
sleep(2)
e.send_keys(Keys.CONTROL,'a')
sleep(2)
e.send_keys(Keys.CONTROL,'x')
sleep(2)
e.send_keys(Keys.CONTROL,'v')
sleep(2)
e.send_keys(Keys.ENTER)#回车