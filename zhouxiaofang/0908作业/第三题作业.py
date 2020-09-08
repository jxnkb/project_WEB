#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# 三．	通过获取多个元素的方式获取元素，分别用id,name,链接文字，子链接文字，标签名，class,路径，css,
# 在电商网上至少各自找2个以上元素，并打印出其他属性，这里一个.py文件
from selenium import webdriver
dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/user/register.html')
# a=dr.find_elements_by_id('username')
# for i in a:
#   print(a[0].get_attribute('name'))
#   print(a[0].get_attribute('type'))


# dr.get('http://39.96.181.61/qftest-ds/user/register.html')
# b=dr.find_elements_by_name('email')
# for i in b:
#   print(b[0].get_attribute('id'))
#   print(b[0].get_attribute('type'))


# dr.get('http://39.96.181.61/qftest-ds/user/register.html')
# c=dr.find_elements_by_link_text('立即注册')
# for i in c:
#   print(i.get_attribute('href'))
#   print(c[0].get_attribute('class'))


# dr.get('http://39.96.181.61/qftest-ds/')
# d=dr.find_elements_by_partial_link_text('我的购物车')
# for i in d:
#   print(d[0].get_attribute('href'))  #http://39.96.181.61/qftest-ds/cart/index.html
#   print(d[0].get_attribute('id'))  #cartbar


# dr.get('http://39.96.181.61/qftest-ds/index.php?m=backend&c=main&a=index')
# e=dr.find_elements_by_tag_name('div')
# for i in e:
#   print(e[0].get_attribute('class'))



# dr.get('https://www.taobao.com')
# f=dr.find_elements_by_class_name('tbh-nav.J_Module.tb-pass  ')
# for i in f:
#   print(f[0].get_attribute('data-name'))
#   print(f[0].get_attribute('data-spm'))


# dr.get('https://www.baidu.com')
# g=dr.find_elements_by_xpath('html/body/div/div')
# for i in g:
#   print(g[0].get_attribute('id'))



# dr.get('http://39.96.181.61/qftest-ds/')
# h=dr.find_elements_by_css_selector('a.red')
# for i in h:
#   print(h[0].get_attribute('href'))

dr.quit()