#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
'''
• text。• 获取元素标签对之间间的文本值
• size。• 获取元素的尺寸大小
• id。• Selenium内部的一个元素属性，用于判断两个元素是否是相同的元素。
• screenshot()方法。
• 给元素一个快照，并保存为PNG格式的图片。
'''

from selenium import webdriver
import os

dr=webdriver.Firefox()
# dr.get('file:///'+os.path.abspath('01HTML/02HTML.html'))
# e=dr.find_element_by_id('maker')
# #获取标签对之间的文字
# print(e.text) #我是段落
# ee=dr.find_element_by_id('maker2')
# ee2=dr.find_element_by_name('username')
# #获取元素的尺寸大小
# print(ee.size) #{'height': 22.0, 'width': 1223.0}
# #获取的是元素的id,不是属性id的值
# print(ee.id) #2aa2c99f-567c-446e-8685-71ce80a6b39a
# print(ee2.id) #2aa2c99f-567c-446e-8685-71ce80a6b39a
# #给元素一个快照
# ee2.screenshot('./a.png')

dr.get('https://www.baidu.com')
e=dr.find_element_by_tag_name('body')
#给百度主体部分一个快照
e.screenshot('b.png')