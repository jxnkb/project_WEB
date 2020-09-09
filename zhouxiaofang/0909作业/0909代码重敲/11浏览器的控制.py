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

dr=webdriver.Firefox()
# dr.get('https://www.baidu.com')
# sleep(2)
# #设置浏览器窗口的大小
# dr.set_window_size(400,800)
# sleep(2)
# #让浏览器最小化
# dr.minimize_window()
# sleep(2)
# #让浏览器最大化
# dr.maximize_window()
# sleep(2)
#
# #转到别的页面
# dr.get('https://www.taobao.com')
# sleep(2)
# #后退到百度
# dr.back()
# sleep(2)
# #前进到淘宝
# dr.forward()
# sleep(2)
# dr.quit()

#案例:进入淘宝,然后设置浏览器的大小400,500,然后最大,最小,再最大,转入到百度,然后后退,再前进
dr.get('https://www.taobao.com')
sleep(2)
#设置浏览器窗口的大小
dr.set_window_size(400,500)
sleep(2)
#让浏览器最大化
dr.maximize_window()
sleep(2)
#让浏览器最小化
dr.minimize_window()
sleep(2)
#让浏览器最大化
dr.maximize_window()
sleep(2)

#转到别的页面
dr.get('https://www.baidu.com')
sleep(2)
#后退到淘宝
dr.back()
sleep(2)
#前进到百度
dr.forward()
sleep(2)
dr.quit()