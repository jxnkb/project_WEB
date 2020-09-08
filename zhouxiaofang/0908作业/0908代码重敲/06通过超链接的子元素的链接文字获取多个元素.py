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
dr.get('file:///'+os.path.abspath('01HTML/06HTML.html'))
e=dr.find_elements_by_partial_link_text('aaa')
for i in e:
  print(i.get_attribute('href'))

dr.quit()