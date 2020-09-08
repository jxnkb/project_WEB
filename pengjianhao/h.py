#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/')
# e=dr.find_element_by_xpath('/html/body/div[1]')
# print(e.get_attribute('class'))
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/')
# e=dr.find_element_by_xpath('//div[@id="top-userbar"]')
# print(e.get_attribute('class'))
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/')
# e=dr.find_elements_by_css_selector('div.topper-userbar.fl')
# for i in e:
#     print(i.get_attribute('id'))
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/')
# e=dr.find_element_by_css_selector('div.guarantee.radius4.cut')
# print(e.get_attribute('name'))
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/')
# e=dr.find_elements_by_link_text('臭豆腐')
# print(len(e))
# for i in e:
#     print(i.get_attribute('href'))
#
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/')
# e=dr.find_elements_by_link_text('dsfs')
# print(len(e))
# for i in e:
#     print(i.get_attribute('target'))
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/')
# e=dr.find_elements_by_partial_link_text('烧猪')
# for i in e:
#     print(i.get_attribute('href'))
#
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/')
# e=dr.find_elements_by_partial_link_text('dsfs')
# for i in e:
#     print(i.get_attribute('target'))
# dr.quit()


# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/")
# e=dr.find_elements_by_tag_name('div')
# for i in e:
#     if i.get_attribute('id'):
#         print(i.get_attribute('class'))
# dr.quit()

# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/")
# e=dr.find_elements_by_tag_name('a')
# for i in e:
#     if i.get_attribute('class'):
#         print(i.get_attribute('href'))
# dr.quit()


# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/')
# e=dr.find_elements_by_id('top-userbar')
# print(e[0].get_attribute('class'))
# dr.quit()

#通过id的获取其他元素的只有class
# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/')
# e=dr.find_elements_by_id('top-userbar')
# for i in e:
#     print(i.get_attribute('class'))
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/')
# e=dr.find_elements_by_name('description')
# print(e.get_attribute('content'))
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/')
# e=dr.find_elements_by_name('keywords')
# for i in e:
#     print(i.get_attribute('content'))
# dr.quit()