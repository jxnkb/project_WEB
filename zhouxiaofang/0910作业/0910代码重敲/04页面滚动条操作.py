#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
import time
'''
使用JS实现
• 到底部：js="document.documentElement.scrollTop=10000"
• 到顶部： js="document.documentElement.scrollTop=0"
• 左右移动：js="window.scrollTo(200,1000)"
• Js代码的执行需要用到的方法：driver.execute_script(js)
'''

dr=webdriver.Firefox()
dr.get('https://www.hao123.com/')
dr.set_window_size(400,800)
time.sleep(3)
#把滚动条拖到底部
js="document.documentElement.scrollTop=10000"
dr.execute_script(js)
time.sleep(2)
#把滚动条拖到顶部
js="document.documentElement.scrollTop=0"
dr.execute_script(js)
time.sleep(2)

js="window.scrollTo(200,1000)"
dr.execute_script(js)
time.sleep(2)