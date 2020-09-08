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
dr.get('file:///'+os.path.abspath('01HTML/09HTML.html'))
# e=dr.find_elements_by_xpath("//input[@name='cin']")
# e=dr.find_elements_by_xpath("//form[@id='loginForm']/input")
# e=dr.find_elements_by_xpath("//*[@name='cin']")


# e=dr.find_elements_by_xpath('/html/body/form')
# e=dr.find_elements_by_xpath('//form')
# e=dr.find_elements_by_xpath('//form[input/@name="username"]')
e=dr.find_elements_by_xpath("//input[@name='cin'][@type='submit']")
print(len(e))
for i in e:
    print(i.get_attribute('value'))
print(len(e))
# print(e[0].get_attribute('type'))
# print(e[1].get_attribute('type'))



dr.quit()


