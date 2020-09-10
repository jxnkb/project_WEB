#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

########页面滚动条缓慢下拉########
#页面滚动条，做成缓慢下拉的动画效果
# from selenium import webdriver
# from time import sleep
# #
# # '''
# # 使用JS实现
# # • 到底部：js="document.documentElement.scrollTop=10000"
# # • 到顶部： js="document.documentElement.scrollTop=0"
# # • 左右移动：js="window.scrollTo(200,1000)"
# # • Js代码的执行需要用到的方法：driver.execute_script(js)
# # '''
# dr=webdriver.Firefox()
# dr.get('https://www.163.com')
# dr.set_window_size(400,600)
# sleep(5)
# #把滚动条拖到底部
#
# for y in range(1000):
#         js='window.scrollBy(0,50)'
#         dr.execute_script(js)
#         sleep(1)
#
# dr.quit()
#
# print('------------------')
#三．登入电商系统，然后添加收件地址，然后退出电商系统，
# 每个用例都写成模块化。

#引入模块
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
# from selenium.webdriver.support.select import Select
#
# dr = webdriver.Firefox()
# # 获取浏览器
# # 打开网站
#
# #登入系统用例
# def login(dr):
#     #获取登录元素,并点击
#     dr.find_element_by_link_text('登陆').click()
#     time.sleep(2)
#     #获取用户名输入框,并输入数据
#     dr.find_element_by_id('username').send_keys('test2')
#
#     #获取密码输入框,并输入数据
#     dr.find_element_by_id('password').send_keys('123456')
#     #获取登入按键元素,并点击
#     dr.find_element_by_link_text('登     陆').click()

# def logout(dr):
#     #获取退出登入元素,并点击
#     dr.find_element_by_link_text('退出登录')
    #获取用户名元素,并进行鼠标悬停,然后获取退出元素,并进行点击
    # e=dr.find_element_by_xpath('//*[@id="top-userbar"]/a')
    # ActionChains(dr).move_to_element(e).perform()
    # dr.find_element_by_link_text('退出').click()

# def xinxi(dr):
#    #获取退出登入元素,并点击
#     s=dr.find_element_by_partial_link_text('收件地址')
#     print(s.get_attribute('href'))
#     time.sleep(3)
#     s.click()
#    #获取新建收件人信息元素，并点击
#     s=dr.find_element_by_id('newadrbtn')
#     print(s.get_attribute('class'))
#     time.sleep(4)
#     s.click()
#     dr.find_element_by_name('receiver').send_keys('chen')
#     # dr.find_element_by_name('sel')
#
#     time.sleep(5)
#
#
#     dr.find_element_by_id('areaslt-province').click()  # 所在省
#     # dr.find_element_by_id('areaslt-province').click() #所在省
#     time.sleep(3)
#     dr.find_element_by_xpath('//select[@id="areaslt-province"]/option[18]').click()
#     # dr.find_element_by_xpath('//select[@id="areaslt-province"]/option[18]').click()  # 广东
#     # print(e.get_attribute('name'))
#     time.sleep(3)
#     dr.find_element_by_id('areaslt-city').click()  # 选择县、区
#     dr.find_element_by_xpath('//select[@id="areaslt-city"]/option[5]').click()
#     time.sleep(3)
#     dr.find_element_by_id('areaslt-borough').click()  # 选择县、区
#     dr.find_element_by_xpath('//select[@id="areaslt-borough"]/option[4]').click()
#     time.sleep(3)
#     dr.find_element_by_id('address').send_keys('廉桥镇')
#     dr.find_element_by_id('zip').send_keys('422811')
#     dr.find_element_by_id('mobile').send_keys('13023545654')
#     dr.find_element_by_class_name("sm-green").click()
#     time.sleep(9)
#     dr.get_screenshot_as_file('dd.png')
# if __name__=='__main__':
#
#     # 获取浏览器
#
#     # 打开网站
#     dr.get('http://39.96.181.61/qftest-ds/')
#     time.sleep(2)
#     #调用登入函数
#     login(dr)
#     time.sleep(5)
#     xinxi(dr)
#     time.sleep(5)
#     #调用退出函数
#     # logout(dr)
#     # time.sleep(5)
#     #关闭浏览器
#     dr.quit()

#四．把注册功能写成模块化登入电商系统，
#然后添加收件地址，然后退出电商系统，每个用例都写成模块化。
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.support.select import Select

dr = webdriver.Firefox()
dr.get('http://39.96.181.61/qftest-ds/')
def login(dr):
        # dr.get('http://39.96.181.61/qftest-ds/')
        # time.sleep(5)
        # 获取免费注册元素并点击
        dr.find_element_by_link_text('免费注册').click()
        time.sleep(5)
        # 获取用户名输入框,并输入数据
        dr.find_element_by_id('username').send_keys('test584')
        time.sleep(5)
        # 获取邮箱输入框,并输入数据
        dr.find_element_by_id('email').send_keys('test62@qq.com')
        time.sleep(5)
        # 获取密码输入框,并输入数据
        dr.find_element_by_id('password').send_keys('123456')
        time.sleep(5)
        # 获取确认密码输入框,并输入数据
        dr.find_element_by_id('repassword').send_keys('123456')
        time.sleep(5)
        # 获取'立即注册'元素,并点击
        dr.find_element_by_link_text('立即注册').click()
        time.sleep(8)

def xinxi(dr):
   #获取退出登入元素,并点击
    s=dr.find_element_by_partial_link_text('收件地址')
    print(s.get_attribute('href'))
    time.sleep(5)
    s.click()
   #获取新建收件人信息元素，并点击
    s=dr.find_element_by_id('newadrbtn')
    print(s.get_attribute('class'))
    time.sleep(4)
    s.click()
    dr.find_element_by_name('receiver').send_keys('xchen')
    # dr.find_element_by_name('sel')

    time.sleep(5)


    dr.find_element_by_id('areaslt-province').click()  # 所在省
    # dr.find_element_by_id('areaslt-province').click() #所在省
    time.sleep(3)
    dr.find_element_by_xpath('//select[@id="areaslt-province"]/option[17]').click()
    # dr.find_element_by_xpath('//select[@id="areaslt-province"]/option[18]').click()  # 广东
    # print(e.get_attribute('name'))
    time.sleep(3)
    dr.find_element_by_id('areaslt-city').click()  # 选择县、区
    dr.find_element_by_xpath('//select[@id="areaslt-city"]/option[4]').click()
    time.sleep(3)
    dr.find_element_by_id('areaslt-borough').click()  # 选择县、区
    dr.find_element_by_xpath('//select[@id="areaslt-borough"]/option[4]').click()
    time.sleep(3)
    dr.find_element_by_id('address').send_keys('廉桥镇')
    dr.find_element_by_id('zip').send_keys('422811')
    dr.find_element_by_id('mobile').send_keys('13023545654')
    dr.find_element_by_class_name("sm-green").click()
    time.sleep(9)
    dr.get_screenshot_as_file('fd.png')

def logout(dr):
    #获取退出登入元素,并点击
    dr.find_element_by_link_text('退出登录')
if __name__=='__main__':
# if __name__ ==' __main__':
# # if __name__ == '__main__':
        # dr = webdriver.Firefox()
        # # 打开网站
        # dr.get('http://39.96.181.61/qftest-ds/')
        # time.sleep(9)
        # 调用登入函数
        login(dr)
        time.sleep(5)
        xinxi(dr)
        time.sleep(5)
        # 调用退出函数
        logout(dr)
        time.sleep(5)
        # 关闭浏览器
        dr.quit()