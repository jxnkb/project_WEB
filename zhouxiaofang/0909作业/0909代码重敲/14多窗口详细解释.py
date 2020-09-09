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
dr=webdriver.Firefox()
dr.get('https://www.taobao.com')
dr.find_element_by_link_text('聚划算').click()
hs=dr.window_handles#获取浏览器中所有窗口的句柄
dr.switch_to.window(hs[1])#把淘宝首页绑定给浏览器
#浏览器是聚划算的页面
h=dr.current_window_handle#聚划算的句柄


dr.find_element_by_link_text('天猫超市').click()
dr.find_element_by_link_text('天猫').click()
dr.find_element_by_link_text('淘抢购').click()

dr.find_element_by_link_text('电器城').click()
hs=dr.window_handles#获取浏览器中所有窗口的句柄
dr.switch_to.window(hs[1])#把淘宝首页绑定给浏览器
dr.switch_to.window(h)#把淘宝首页绑定给浏览器