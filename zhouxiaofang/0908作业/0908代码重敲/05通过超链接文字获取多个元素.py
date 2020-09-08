#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

from selenium import webdriver
dr=webdriver.Firefox()
dr.get('http://39.96.181.61/qftest-ds/')
e=dr.find_elements_by_link_text('[美食专栏]诗词')
print(len(e)) #4
for i in e:
    print(i.get_attribute('href'))
    #http://39.96.181.61/qftest-ds/article/view.html?id=442
    # http://39.96.181.61/qftest-ds/article/view.html?id=441
    # http://39.96.181.61/qftest-ds/article/view.html?id=440
    # http://39.96.181.61/qftest-ds/article/view.html?id=439
dr.quit()