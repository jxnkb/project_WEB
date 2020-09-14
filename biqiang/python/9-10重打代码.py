#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
# d=webdriver.Firefox()


# d.get('https://mail.qq.com')
# sleep(3)
# d.switch_to.frame(d.find_element_by_id('login_frame'))
# d.find_element_by_partial_link_text('帐号密码登录').click()
# sleep(1)
# d.switch_to.default_content()
# sleep(2)
# d.find_element_by_partial_link_text('基本版').click()
# sleep(2)
# d.quit()


# d.get('https://baidu.com')
# sleep(3)
# a1=d.find_element_by_id('s-usersetting-top')
# print(a1.get_attribute('class'))
# sleep(2)
# ActionChains(d).move_to_element(a1).perform()
# d.find_element_by_partial_link_text('搜索设置').click()
# d.find_element_by_partial_link_text('保存设置').click()
# sleep(2)
# d.switch_to.alert.accept()


# d.get('https://baidu.com')
# d.implicitly_wait(3)
# a1=d.find_element_by_id('s-usersetting-top')
# print(a1.get_attribute('class'))
# d.implicitly_wait(2)
# ActionChains(d).move_to_element(a1).perform()
# d.find_element_by_partial_link_text('搜索设置').click()
# d.find_element_by_partial_link_text('保存设置').click()
# d.implicitly_wait(2)
# d.switch_to.alert.accept()

import csv
with open('../111.csv','r',encoding='utf-8')as f:
    print(f.readlines()[0])

#注册已练过




