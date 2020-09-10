#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
import time
dr=webdriver.Firefox()
#打开qq的首页
dr.get('https://www.qq.com')
#点击邮件图标
dr.find_element_by_link_text('Qmail').click()
#获取浏览器中所有页面的句柄
hs=dr.window_handles
#切换到邮箱页面
dr.switch_to.window(hs[1])
time.sleep(2)
#获取邮箱页面里的小窗口
iframeobj=dr.find_element_by_xpath('//*[@id="login_frame"]')
#print(iframeobj.get_attribute("name"))

#切换到frame
dr.switch_to.frame(iframeobj)
time.sleep(2)

#获取账号密码登录元素并点击
if dr.find_element_by_xpath('//body/div[@id="login"]/div[@id="header"]/div[@id="switch"]/a[2]'):
    dr.find_element_by_xpath('//body/div[@id="login"]/div[@id="header"]/div[@id="switch"]/a[2]').click()
time.sleep(3)

#获取输入框元素并输入qq号码
dr.find_element_by_xpath('//*[@id="u"]').send_keys('2644684923')
time.sleep(2)
#获取输入框元素并输入密码
dr.find_element_by_xpath('//*[@id="p"]').send_keys('123456')
time.sleep(2)
#点击登入
dr.find_element_by_xpath('//*[@id="login_button"]').click()
time.sleep(2)

#切换回主体
dr.switch_to.default_content()

#点击邮箱页面的基本版
dr.find_element_by_link_text('基本版').click()

time.sleep(2)

dr.quit()