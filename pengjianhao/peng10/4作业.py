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
# 获取浏览器
# 打开网站

#登入系统用例
def login(dr):
    #获取登入元素,并点击
    dr.find_element_by_link_text('登陆').click()
    time.sleep(2)
    #获取用户名输入框,并输入数据
    dr.find_element_by_id('username').send_keys('test2')

    #获取密码输入框,并输入数据
    dr.find_element_by_id('password').send_keys('123456')
    #获取登入按键元素,并点击
    dr.find_element_by_link_text('登     陆').click()

def logout(dr):
    #点击收货地址
    dr.find_element_by_link_text('收件地址').click()
    time.sleep(2)
    #点击新建收件人信息
    dr.find_element_by_id('newadrbtn').click()
    time.sleep(2)
    #获取收件人的输入框 ，写入收件人名
    dr.find_element_by_id('receiver').send_keys('彭先生')
    time.sleep(1)
    #点击所在地
    dr.find_element_by_id('areaslt-province').click()
    time.sleep(1)
    #点击广东省
    dr.find_element_by_xpath('//*[@value="19"]').click()
    time.sleep(1)
    #点击选择城市
    dr.find_element_by_id('areaslt-city').click()
    time.sleep(1)
    dr.find_element_by_xpath('//select[@id="areaslt-city"]/option[13]').click()
    time.sleep(1)
    #点击选择县
    dr.find_element_by_id('areaslt-borough').click()
    time.sleep(2)
    dr.find_element_by_xpath('//select[@id="areaslt-borough"]/option[9]').click()
    time.sleep(2)
    #获取详细地址框并输入
    dr.find_element_by_id('address').send_keys('和山岩')
    time.sleep(2)
    #获取邮编的输入框并输入
    dr.find_element_by_id('zip').send_keys('514500')
    time.sleep(1)
    #获取手机号码输入框并输入
    dr.find_element_by_id('mobile').send_keys('15302628888')
    time.sleep(1)
    #点击保存信息
    dr.find_element_by_xpath('//*[@class="sm-green"]').click()
    time.sleep(1)
    #获取退出登入元素,并点击
    # dr.find_element_by_link_text('退出登录')
    #获取用户名元素,并进行鼠标悬停,然后获取退出元素,并进行点击
    e=dr.find_element_by_xpath('//*[@id="top-userbar"]/a')
    ActionChains(dr).move_to_element(e).perform()
    dr.find_element_by_link_text('退出').click()

if __name__=='__main__':

    # 获取浏览器
    dr=webdriver.Firefox()
    # 打开网站
    dr.get('http://39.96.181.61/qftest-ds/')
    time.sleep(2)
    #调用登入函数
    login(dr)
    time.sleep(5)
    #调用退出函数
    logout(dr)
    time.sleep(5)
    #关闭浏览器
    dr.quit()


