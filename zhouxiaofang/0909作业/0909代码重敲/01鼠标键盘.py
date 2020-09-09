#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
'''
clear()： 清除文本。
send_keys (value)： 模拟按键输入。
click()： 单击元素。例如按钮操作。
'''
from selenium import webdriver
import time
dr=webdriver.Firefox()
# dr.get('https://www.baidu.com')
# e=dr.find_element_by_id('kw')
# #在元素中输入文字
# e.send_keys('软件测试')
# time.sleep(3)
# #清空
# e.clear()
# time.sleep(3)
# dr.quit()


# e=dr.find_element_by_link_text('新闻')
# #点击元素
# e.click()
# time.sleep(2)
# dr.quit()

#案例:淘宝首页搜索栏上面点击天猫,然后在搜索栏写'软件测试',之后再清除
dr.get('https://www.taobao.com')
e=dr.find_element_by_xpath("//ul[@class='ks-switchable-nav']/li[2]")
time.sleep(1)
e.click()
ee=dr.find_element_by_id('q')
ee.send_keys('软件测试')
time.sleep(2)
ee.clear()
time.sleep(2)
dr.quit()