#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains#警告窗处理需要引入这个模块
from time import sleep


#内嵌窗口的处理
# dr=webdriver.Firefox()
# #打开qq的首页
# dr.get('http://www.qq.com')
# #点击邮件图标
# #切换到邮箱页面
# dr.find_element_by_link_text('Qmail').click()
# #获取浏览器中所有页面的句柄
# hs=dr.window_handles
# #获取邮箱的句柄
# dr.switch_to.window(hs[1])
# sleep(2)
# #获取邮箱页面里的小窗口
# aa=dr.find_element_by_xpath('//*[@id="login_frame"]')
# #切换到小窗口
# sleep(6)
# dr.switch_to.frame(aa)
# sleep(3)
# #获取账号密码登陆的元素并点击
# dr.find_element_by_id('switcher_plogin').click()
# sleep(6)
# #获取输入框元素
# a=dr.find_element_by_id('u')
# #输入账号
# a.send_keys("495912990")
# sleep(2)
# #获取密码框元素
# b=dr.find_element_by_id('p')
# #输入密码
# b.send_keys('987654')
# sleep(2)
# #找到点击登陆按键的元素并且点击
# dr.find_element_by_id('login_button').click()


#警告处理
# dr=webdriver.Firefox()
# dr.get('https://www.baidu.com')
# #获取设置的元素用标签名来获取
# a=dr.find_element_by_tag_name('span')
# #控制鼠标悬停到设置元素
# ActionChains(dr).move_to_element(a).perform()
# sleep(2)
# #点击搜索设置
# dr.find_element_by_link_text('搜索设置').click()
# sleep(5)
# #点击每页50条信息的选项
# dr.find_element_by_id('nr_3').click()
# sleep(1)
# #点击保存设置
# dr.find_element_by_link_text('保存设置').click()
# sleep(2)
# # 暂时将浏览器对象driver交给alter用
# dd=dr.switch_to.alert
# #获取警告框的文本信息
# # print(dd.text)
# # accept()：接受现有警告框，就是点他的确定按钮
# dd.accept()
# sleep(3)
# # ：放弃现有警告框，取消
# # dd.dismiss()











