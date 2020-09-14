#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
from time import sleep
import os
d=webdriver.Firefox()


#案例:在百度首页上用xpath随便找一个元素,并打印这个元素的其他属性值
# d.get('https://www.baidu.com/')
# a=d.find_element_by_tag_name('link')
# a1=a.get_attribute('href')
# print(a1)
#
#案例:自己写个有超链接的标签,通过class样式,找到该标签的href属性值
# d.get('file:///'+os.path.abspath('h1.html'))
# a=d.find_element_by_css_selector('a.bd')
# print(a.get_attribute('href'))



#案例:在百度上找一个元素,用css方式
# d.get('https://baidu.com')
# a=d.find_element_by_css_selector('div.wrapper_new')
# print(a.get_attribute('id'))

#自己写一个html文件,定义两个id属性值相同的标签,通过id获取多个元素,然后打印出各自其他的属性
# d.get('file:///'+os.path.abspath('h1.html'))
# a=d.find_elements_by_id('wbk')
# a1=a[0].get_attribute('name')
# a2=a[2].get_attribute('name')
# print(a1,a2)


#案例:自己写一个html文件,定义两个name属性值相同的标签,通过name获取多个元素,然后打印出各自其他的属性
# d.get('file:///'+os.path.abspath('h1.html'))
# a=d.find_elements_by_name('tc')
# a1=a[0].get_attribute('value')
# a2=a[1].get_attribute('value')
# print(a1,a2)

#案例:获取淘宝首页有多少个div,并打印出div里的id属性值
# d.get("https://taobao.com")
# sleep(3)
# a=d.find_elements_by_tag_name('div')
# print(len(a))
# for i in a:
#     if i.get_attribute('id'):
#         print(i.get_attribute('id'))

#案例:自己写一个有类样式的html页面,定义段落和链接标签,引用类样式,然后通过本函数获取这两个标签的其他属性
d.get("file:///"+os.path.abspath('h1.html'))
a=d.find_elements_by_class_name('qw')
a1=a[1].get_attribute('name')
a2=a[2].get_attribute('name')
print(a1,a2)









