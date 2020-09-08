#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
import os
dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/user/register.html')
# e=dr.find_elements_by_id('username')
# print(e[0].get_attribute('name'))
# print(e[0].get_attribute('type'))
# dr.quit()

# from selenium import webdriver
# import os
# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/user/register.html')
# e=dr.find_elements_by_name('username')
# print(e[0].get_attribute('id'))
# print(e[0].get_attribute('type'))
# dr.quit()


# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/index.html')
# e=dr.find_elements_by_link_text('免费注册')
# print(e[0].get_attribute('class'))
# print(e[0].get_attribute('href'))
#
# dr.quit()

# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/index.html')
# e=dr.find_elements_by_partial_link_text('我的购物车')
# print(e[0].get_attribute('id'))
# print(e[0].get_attribute('href'))
#
# dr.quit()


# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/index.html')
# e=dr.find_elements_by_tag_name('div')
# print(e[0].get_attribute('class'))
# print(e[2].get_attribute('id'))
#
# dr.quit()

# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/search/index.html?kw=')
# e=dr.find_elements_by_class_name('red')
# print(e[0].get_attribute('href'))
# # print(e[0].get_attribute('type'))
#
# dr.quit()

# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/user/register.html')
# e=dr.find_elements_by_xpath('form[@id="register-form"]')
# print(e[0].get_attribute('method'))
# print(e[0].get_attribute('action'))
#
# dr.quit()

from selenium import webdriver
dr=webdriver.Firefox()
dr.get('http://39.96.181.61/qftest-ds/user/register.html')
d=dr.find_elements_by_css_selector('a.myclass')
print(e[0].get_attribute('method'))
print(e[0].get_attribute('action'))

dr.quit()




