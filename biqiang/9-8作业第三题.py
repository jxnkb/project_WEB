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
a=d.find_elements_by_id('top-userbar')
a1=d.find_elements_by_id('logined-userbar-tpl')
b=a[0].get_attribute('class')
b1=a1[0].get_attribute('type')
print(b,b1)

c=d.find_elements_by_name('kw')
c1=d.find_elements_by_name('keywords')
e=c[0].get_attribute('type')
e1=c1[0].get_attribute('content')
print(e,e1)

f=d.find_elements_by_link_text('Verydows')
f1=d.find_elements_by_partial_link_text('登陆')
f2=f[0].get_attribute('href')
f3=f1[0].get_attribute('href')
print(f2,f3)

g=d.find_elements_by_tag_name('div')
for i in g:
    if i.get_attribute('class'):
        print(i.get_attribute('class'))

h=d.find_elements_by_class_name('topper-userbar.fl')
h1=d.find_elements_by_class_name('red')
h2=h[0].get_attribute('id')
h3=h1[0].get_attribute('href')
print(h2,h3)

j=d.find_elements_by_css_selector('div.topper-userbar.fl')
j1=d.find_elements_by_css_selector('a.red')
j2=h[0].get_attribute('id')
j3=h1[0].get_attribute('href')
print(j2,j3)

k=d.find_elements_by_xpath('//meta')
for i in k:
    if i.get_attribute('name'):
        print(i.get_attribute('name'))

d.quit()



# def hunt(x):


















