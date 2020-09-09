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
dr.get("file:///"+os.path.abspath('01HTML/04HTML.html'))
e=dr.find_element_by_name('c1')
ee=dr.find_element_by_name('c3')
#判断元素是否处于选择状态
print(e.is_selected()) #True

# <input disabled type="checkbox" name="c3" value="c"/>郭富城
# 添加了disabled 无法被选择
print(ee.is_selected()) #False

e2=dr.find_element_by_name('c88')
#判断元素的可用性
# 如果元素属性中添加了disabled,表示该元素不可用
print(ee.is_enabled()) #False

#检查该元素是否用户可见
#p{display:none;}<!-- 隐藏了 -->
#如果给标签添加了隐藏样式:p{display:none;}该元素会被隐藏
print(e2.is_displayed()) #False



