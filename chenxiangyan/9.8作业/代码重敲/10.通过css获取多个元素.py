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

dr.get('file:///'+os.path.abspath('h10.html'))
e=dr.find_elements_by_css_selector('p.class')
for i in e:
    print(i.get_attribute('id'))
d=dr.find_elements_by_css_selector('a.myclass')
for i in d:
    print(i.get_attribute('href'))
dr.quit()

