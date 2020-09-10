#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys

dr=webdriver.Firefox()
time.sleep(3) #强制等待
#隐式等待
#在使用隐式等待的时候，实际上浏览器会在你自己设定的时间内部不断的刷新页面去寻找我们需要
# dr.implicitly_wait(10)
dr.get('https://www.baidu.com')
dr.find_element_by_id('kw')

#显示等待
try:
    ele=WebDriverWait(dr,5,0.5,ignored_exceptions=None).until(EC.presence_of_element_located((By.ID,"kw")),"找不到")
    ele.send_keys("selenium")
    time.sleep(3)
except:
    print(sys.exc_info())