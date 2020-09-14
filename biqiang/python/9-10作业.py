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

#第二题
# d=webdriver.Firefox()
# d.get("https://qq.com")
# sd='document.documentElement.scrollTop='
# sleep(4)
# for i in range(5000):
#     d.execute_script(sd+str(i*2))

#第三题
d=webdriver.Firefox()
def user_login():
    from selenium import webdriver
    from time import sleep
    from selenium.webdriver.common.keys import Keys
    import os
    f = open('C:\\Users\Joseph\Desktop\电商系统-阿里云环境.txt', 'r')
    a = f.read().splitlines()
    front = a[-1]
    d.get(front)
    d.find_element_by_partial_link_text('登陆').click()
    a=d.find_element_by_id('username')
    a.send_keys('jxnkb')
    b=d.find_element_by_id('password')
    b.send_keys('1qaz2wsx')
    d.find_element_by_partial_link_text('登     陆').click()



def add_adr():
    from selenium.webdriver.support.select import Select
    d.find_element_by_partial_link_text('收件地址').click()
    sleep(3)
    d.find_element_by_id('newadrbtn').click()
    sleep(2)
    d.find_element_by_id('receiver').send_keys('张三')

    a1=d.find_element_by_id('areaslt-province')
    Select(a1).select_by_visible_text('广东省')
    a2=d.find_element_by_id('areaslt-city')
    Select(a2).select_by_visible_text('深圳市')
    a3=d.find_element_by_id('areaslt-borough')
    Select(a3).select_by_visible_text('宝安区')
    d.find_element_by_id('address').send_keys('宝安大道西部硅谷a605')
    d.find_element_by_id('zip').send_keys('341400')
    d.find_element_by_id('mobile').send_keys('13666666333')
    d.find_element_by_class_name('sm-green').click()



def user_logout():
    from selenium.webdriver.common.action_chains import ActionChains
    c1=d.find_element_by_xpath('//div[@id="top-userbar"]/a[1]')
    ActionChains(d).move_to_element(c1).perform()
    sleep(2)
    d.find_element_by_partial_link_text('退出').click()


# user_login()
# sleep(5)
# add_adr()
# sleep(5)
# user_logout()

#第四题
def register():
    import random
    d.get('http://39.96.181.61/qftest-ds/')
    sleep(1)
    d.find_element_by_partial_link_text('免费注册').click()
    sleep(3)
    a=d.find_element_by_id('username')
    sleep(2)
    a.send_keys('sjs%df3n1%dh'%(random.randint(0,99),random.randint(0,99)))
    b=d.find_element_by_id('email')
    sleep(2)
    b.send_keys('10j1s%d41s%d23q@ss.com'%(random.randint(0,99),random.randint(0,99)))
    c=d.find_element_by_id('password')
    sleep(2)
    c.send_keys('121e2d2')
    e=d.find_element_by_id('repassword')
    sleep(2)
    e.send_keys('121e2d2')
    sleep(3)
    d.find_element_by_class_name('form-submit').click()
    sleep(5)
    #print(d.current_url)
    if d.current_url == 'http://39.96.181.61/qftest-ds/user/index.html':
        print('注册成功')
    else:
        print('注册失败')
    d.quit()

# register()


