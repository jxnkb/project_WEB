#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

from selenium import webdriver
from time import sleep
d=webdriver.Firefox()
d.get('http://39.96.181.61/qftest-ds/')
sleep(2)
a=d.find_element_by_xpath('//div')
b=d.find_element_by_css_selector('a.red')
print(a.get_attribute('class'))
print(b.get_attribute('href'))

d.quit()
















