#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#三．自动化登入电商系统前台，把苹果加入到购物车
# 注意：网站要通过代码获取
f=open('环境.txt','r')
list=f.read().splitlines()
# print(list)
from selenium import webdriver
from time import sleep
dr=webdriver.Firefox()
dr.get(list[7])
w=dr.find_element_by_name('kw')
w.send_keys('苹果')
sleep(3)
w1=dr.find_element_by_xpath('//*[@class="fr"][@type="submit"]').click() #点击搜索
sleep(3)
w2=dr.find_element_by_xpath('//div[@class="im"]/a/img').click()   #点击苹果的链接
sleep(3)
dr.find_element_by_xpath('//div[@class="buy mt30"]/a[@class="add-cart icon"]').click() #点击加入购物车
sleep(3)
dr.get_screenshot_as_file('04.png')
dr.quit()