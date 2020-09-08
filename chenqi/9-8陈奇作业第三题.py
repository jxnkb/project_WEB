#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#三．通过获取多个元素的方式获取元素，分别用id,name,链接文字，子链接文字
# ，标签名，class,路径，css,在电商网上至少各自找2个以上元素，并打印出其他属性，这里一个.py文件
#find_elements_by_id()函数
from selenium import webdriver
dr=webdriver.Firefox()
import os
dr.get('file:///'+os.path.abspath('html/banan.html'))
a1=dr.find_elements_by_id('yy')
a2=dr.find_elements_by_name('mak')
a3=dr.find_elements_by_link_text('淘宝')
a4=dr.find_elements_by_partial_link_text('我是a里面的P')
a5=dr.find_elements_by_tag_name('a')
a6=dr.find_elements_by_class_name('yangshi1')
a7=dr.find_elements_by_xpath('//*[@id="yy"]')
a8=dr.find_elements_by_css_selector('a.content')
def banan():

    for i in a1:
        print(i.get_attribute('name'))
    for i in a2:
        print(i.get_attribute('id'))
    for i in a3:
        print(i.get_attribute('href'))
    for i in a4:
        print(i.get_attribute('href'))
    for i in a5:
        print(i.get_attribute('href'))
    for i in a6:
        print(i.get_attribute('name'))
    for i in a7:
        print(i.get_attribute('name'))
    for i in a8:
        print(i.get_attribute('href'))

banan()

dr.quit()






