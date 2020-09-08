#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# 二．	在电商网上通过路径和css各找一个元素，并打印其他属性值，这里一个.py文件
from selenium import webdriver
dr=webdriver.Firefox()
dr.get('http://39.96.181.61/qftest-ds/')
# e=dr.find_element_by_xpath('html/head/meta[2]')
# print(e.get_attribute('name')) #verydows-baseurl

e=dr.find_element_by_css_selector('a.red')
print(e.get_attribute('href')) #http://39.96.181.61/qftest-ds/user/register.html

dr.quit()