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
url='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
dr.get(url)
#切换到目标元素的窗口iframeResult
dr.switch_to.frame('iframeResult')
#确定要拖拽的目标元素
s=dr.find_element_by_id('draggable')
#要拖入到的目标元素位置
e=dr.find_element_by_id('droppable')
#执行拖拽动作
ActionChains(dr).drag_and_drop(s,e).perform()
