#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# from selenium import webdriver
# import os
# import time
# dr=webdriver.Firefox()
# dr.get('file:///'+os.path.abspath('01HTML/01HTML.html'))
# e=dr.find_element_by_xpath('/html/body/form[1]')#找的是form
# # e=dr.find_element_by_xpath('//form[1]')#找的是form
# # e=dr.find_element_by_xpath("//form[@id='loginForm']")#找的是form
# # e=dr.find_element_by_xpath('//form[input/@name="username"]')#找的是form
# # e=dr.find_element_by_xpath('//form[@id="loginForm"]/input[1]')#找的是input
# # e=dr.find_element_by_xpath("//input[@name='username']")#找的是input
# # e=dr.find_element_by_xpath("//input[@name='cin'][@type='submit']")#找的是input
# e=dr.find_element_by_xpath("//*[@name='cin'][@type='submit']")#找的是input

# print(e.get_attribute('id'))
# dr.quit()

#案例:在百度首页上用xpath随便找一个元素,并打印这个元素的其他属性值
from selenium import webdriver
dr=webdriver.Firefox()
# dr.get('https://www.baidu.com')
# e=dr.find_element_by_xpath("/html/head/meta[4]")
# e=dr.find_element_by_xpath('//head[meta/@name="theme-color"]') #找的是head
# e = dr.find_element_by_xpath('//meta[@name="theme-color"]') #找的是meta
# print(e.get_attribute('content'))  #2932e1

# dr.get('https://www.taobao.com')
# # xx=dr.find_element_by_xpath("/div[@class='cover J_Cover']/div[2]")
# print(xx.get_attribute('class'))
dr.quit()