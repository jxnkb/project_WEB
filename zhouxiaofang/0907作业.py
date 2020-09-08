#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# 3.请在电商网站上找10个元素,用id和name方式获取,
# 打印元素除id和name外的其他属性,提交到git上
from selenium import webdriver

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/')
# e=dr.find_element_by_name('kw')
# print(e.get_attribute('class'))    #fl
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/user/register.html')
# e=dr.find_element_by_name('username')
# print(e.get_attribute('type'))  #text
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/user/register.html')
# e=dr.find_element_by_name('password')
# print(e.get_attribute('type'))  #password
# dr.quit()

# dr=webdriver.Firefox()
# # dr.get('http://39.96.181.61/qftest-ds/')
# # e=dr.find_element_by_id('unlogined-userbar-tpl')
# # print(e.get_attribute('type'))    #text/template
# # dr.quit()

# dr=webdriver.Firefox()
# # dr.get('http://39.96.181.61/qftest-ds/')
# # e=dr.find_element_by_id('logined-userbar-tpl')
# # print(e.get_attribute('type'))   #text/template
# # dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/user/register.html')
# e=dr.find_element_by_id('email')
# print(e.get_attribute('type'))   #text
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/user/register.html')
# e=dr.find_element_by_id('password')
# print(e.get_attribute('type'))   #password
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/user/register.html')
# e=dr.find_element_by_id('repassword')
# print(e.get_attribute('type'))   #password
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/user/register.html')
# e=dr.find_element_by_id('username')
# print(e.get_attribute('type'))   #text
# dr.quit()

# 4.电商网站上找5个超链接元素,通过超链接文字获取元素,打印链接
from selenium import webdriver

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/index.html')
# e=dr.find_element_by_link_text('首页')
# print(e.get_attribute('href'))  #http://39.96.181.61/qftest-ds
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/index.html')
# e=dr.find_element_by_link_text('dsfs')
# print(e.get_attribute('href'))  #http://39.96.181.61/qftest-ds/index.php?m=backend&c=main&a=panel
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/index.html')
# e=dr.find_element_by_link_text('a')
# print(e.get_attribute('href'))  #http://39.96.181.61/qftest-ds/%E5%BC%80%E5%BF%83Lll56_fds
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/index.html')
# e=dr.find_element_by_link_text('dady')
# print(e.get_attribute('href'))  #http://39.96.181.61/qftest-ds/dfgt
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/index.html')
# e=dr.find_element_by_link_text('sssss')
# print(e.get_attribute('href'))  #http://39.96.181.61/qftest-ds/aaaaaaaaa
# dr.quit()