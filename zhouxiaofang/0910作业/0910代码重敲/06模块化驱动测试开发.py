#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#引入模块
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

#登入系统用例
def login(dr):
    #获取登入元素,并点击
    dr.find_element_by_link_text('登陆').click()
    time.sleep(2)
    #获取用户名输入框,并输入数据
    dr.find_element_by_id('username').send_keys('test2')
    #获取密码输入框,并输入数据
    dr.find_elememt_by_id('password').send_keys(123456)
    #获取登陆按键元素,并点击
    dr.find_element_by_link_text('登     陆').click()

def logout(dr):
    # 获取退出登入元素,并点击
    # dr.find_element_by_link_text('退出登录')
    # 获取用户名元素,并进行鼠标悬停,然后获取退出元素,并进行点击
    e = dr.find_element_by_xpath('//*[@id="top-userbar"]/a')
    ActionChains(dr).move_to_element(e).perform()
    dr.find_element_by_link_text('退出').click()

if __name__ == '__main__':

    # 获取浏览器
    dr = webdriver.Firefox()
    # 打开网站
    dr.get('http://39.96.181.61/qftest-ds/')
    time.sleep(2)
    # 调用登入函数
    login(dr)
    time.sleep(5)
    # 调用退出函数
    logout(dr)
    time.sleep(5)
    # 关闭浏览器
    dr.quit()
