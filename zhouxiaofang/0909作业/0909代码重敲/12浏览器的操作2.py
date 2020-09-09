#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

from selenium import webdriver
from time import sleep
dr=webdriver.Firefox()
# dr.get('https://www.taobao.com')
# sleep(3)
# #刷新
# dr.refresh()
# sleep(3)
# #截图
# dr.get_screenshot_as_file('1.png')
# sleep(3)
# #点击聚划算
# dr.find_element_by_link_text('聚划算').click()
# sleep(3)
# #关闭最前的窗口
# dr.close()
# sleep(5)
# #关闭浏览器
# dr.quit()

#案例:打开淘宝,刷新页面,点击天猫超市,然后截图,然后关闭淘宝首页,最后退出浏览器

dr.get('https://www.taobao.com')
sleep(3)
#刷新
dr.refresh()
sleep(3)
#点击天猫超市
dr.find_element_by_link_text('天猫超市').click()
sleep(3)
#截图
dr.get_screenshot_as_file('2.png')
#关闭最前的窗口
dr.close()
sleep(5)
#关闭浏览器
dr.quit()