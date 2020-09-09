#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
'''
  • 获取当前窗口句柄：driver.current_window_handle
    • 获取浏览器所有句柄：driver.window_handles
    • 切换到指定的浏览器窗口：driver.switch_to.window(handle)
'''
from selenium import webdriver
from time import sleep

# dr=webdriver.Firefox()
# dr.get('https://www.taobao.com')
# #获取淘宝首页的句柄
# h1=dr.current_window_handle
# print(h1)
# sleep(3)
# dr.find_element_by_link_text('聚划算').click()
# h2=dr.current_window_handle  #获取的是淘宝首页的句柄
# print(h2)
# sleep(3)
# dr.find_element_by_link_text('天猫超市').click()
# h3=dr.current_window_handle  #获取的是淘宝首页的句柄
# print(h3)
# sleep(3)
#
# #获取浏览器中所有窗口的句柄
# hs=dr.window_handles
# print(hs)
# #把天猫超市窗口绑定给浏览器
# dr.switch_to.window(hs[1])
# sleep(2)
# dr.get_screenshot_as_file('3.png')
# sleep(1)
# dr.close()

#案例：打开百度首页，点击新闻，点击地图，点击视频，然后关闭地图页面,截取视频页面的图像，退出浏览器

dr=webdriver.Firefox()
dr.get('https://www.baidu.com')
sleep(3)
dr.find_element_by_link_text('新闻').click()
sleep(3)
dr.find_element_by_link_text('地图').click()
sleep(3)
dr.find_element_by_link_text('视频').click()
sleep(3)
hs=dr.window_handles#获取浏览器中所有窗口的句柄
dr.switch_to.window(hs[2])#把地图绑定给浏览器
sleep(2)
dr.close()
sleep(1)
dr.switch_to.window(hs[1])#把视频绑定给浏览器
dr.get_screenshot_as_file('4.png')
sleep(2)
dr.quit()