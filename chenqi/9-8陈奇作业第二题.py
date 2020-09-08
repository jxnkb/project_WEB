#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#二．在电商网上通过路径和css各找一个元素，并打印其他属性值，这里一个.py文件
#第一个
from selenium import webdriver
dr=webdriver.Firefox()
dr.get('http://39.96.181.61/qftest-ds/')
w=dr.find_element_by_css_selector('a.red')
print(w.get_attribute('href'))
dr.quit()   #http://39.96.181.61/qftest-ds/user/register.html

#第二个
w=dr.find_element_by_xpath('//*[@target="_blank"]')
print(w.get_attribute('href'))
dr.quit()  #http://39.96.181.61/qftest-ds/dfgt




