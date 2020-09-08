#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#find_element_by_xpath()函数
#案例:在百度首页上用xpath随便找一个元素,并打印这个元素的其他属性值
from selenium import webdriver
import os
dr=webdriver.Firefox()
# dr.get('http://www.baidu.com')
# w=dr.find_element_by_xpath('//head[meta/@name="referrer"]')
# print(w.get_attribute('content'))
# dr.quit()



#find_element_by_css_selector()函数
#案例:自己写个有超链接的标签,通过class样式,找到该标签的href属性值
# dr.get('file:///'+os.path.abspath('html/css.html'))
# w=dr.find_element_by_css_selector('a.content')
# print(w.get_attribute('href'))
# dr.quit()

#find_elements_by_id()函数
#案列:自己写一个html文件,定义两个id属性值相同的标签,通过id获取多个元素,然后打印出各自其他的属性
# dr.get('file:///'+os.path.abspath('html/id.html'))
# w=dr.find_elements_by_id('yy')
# for i in w:
#     print(i.get_attribute('name'))
# dr.quit()


#find_elements_by_name()函数
#案例:自己写一个html文件,定义两个name属性值相同的标签,通过name获取多个元素,然后打印出各自其他的属性
# dr.get('file:///'+os.path.abspath('html/name.html'))
# w=dr.find_elements_by_name('mak')
# print(w[0].get_attribute('id'))
# print(w[1].get_attribute('href'))
# dr.quit()


#find_elements_by_link_text()函数
# dr.get('http://39.96.181.61/qftest-ds/')
# w=dr.find_elements_by_link_text('苹果')
# print(len(w))
# for i in w:
#     print(i.get_attribute('href'))
# dr.quit()


#find_elements_by_partial_link_text()函数
# dr.get('http://www.baidu.com')
# w=dr.find_elements_by_partial_link_text('百度热搜')
# for i in w:
#     print(w.get_attribute('href'))
# dr.quit()



#find_elements_by_tag_name()函数
#案例:获取淘宝首页有多少个div,并打印出div里的id属性值
# dr.get('http://www.taobao.com')
# w=dr.find_elements_by_tag_name('div')
# print(len(w))
# for i in w:
#     if i.get_attribute('id'):
#       print(i.get_attribute('id'))
# dr.quit()


#find_elements_by_class_name()函数
#案例:自己写一个有类样式的html页面,定义段落和链接标签,引用类样式,然后通过本函数获取这两个标签的其他属性
# dr.get('file:///'+os.path.abspath('html/01.html'))
# w=dr.find_elements_by_class_name('yangshi1')
# print(w[0].get_attribute('name'))
# print(w[1].get_attribute('id'))
# dr.quit()


#find_elements_by_xpath()函数
# dr.get('http://www.baidu.com')
# w=dr.find_elements_by_xpath('//*[@class="c-color-gray2"][@target="_blank"]')
# print(len(w))
# for i in w:
#     if i.get_attribute('href'):
#        print(i.get_attribute('href'))
# dr.quit()


#find_elements_by_css_selector()函数
#案例:写一个html文件,写类样式,名字要.myclass,定义多个超链接标签,引入类样式,获取各个超链表标签的链接
# dr.get('file:///'+os.path.abspath('html/csses.html'))
# w=dr.find_elements_by_css_selector('a.mylcass')
# for i in range(len(w)):
#     print(w[i].get_attribute('href'))
# dr.quit()