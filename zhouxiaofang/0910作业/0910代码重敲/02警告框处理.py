#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

dr=webdriver.Firefox()
dr.get('https://www.baidu.com')
dr.maximize_window()

#获取元素
e=dr.find_element_by_tag_name('span')

#控制鼠标悬停到设置元素
ActionChains(dr).move_to_element(e).perform()
time.sleep(3)

#点击搜索设置
dr.find_element_by_link_text('搜索设置').click()
time.sleep(3)

#选择显示20条
e=dr.find_element_by_id('nr_2')
e.click()
time.sleep(3)

#点击保存设置按键
dr.find_element_by_link_text('保存设置').click()
time.sleep(3)

#暂时将浏览器对象driver交给alert用
dd=dr.switch_to.alert
#获取警告框的文本信息
print(dd.text)

# accept()：接受现有警告框，就是点他的确定按钮
# dd.accept()
time.sleep(3)

# ：放弃现有警告框，取消
dd.dismiss()

dr.quit()
