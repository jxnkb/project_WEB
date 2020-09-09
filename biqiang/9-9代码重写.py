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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
d=webdriver.Firefox()

# #案例:淘宝首页搜索栏上面点击天猫,然后在搜索栏写'软件测试',之后再清除
# d.get('https://taobao.com')
# sleep(3)
# d.find_element_by_xpath("//ul[@class='ks-switchable-nav']/li[2]").click()
# a=d.find_element_by_id('q')
# a.send_keys('软件测试')
# sleep(3)
# a.clear()
# sleep(3)
# d.quit()

# #yuansu
# d.get('https://baidu.com')
# a=d.find_element_by_id('su')
# print(a.id,a.size)
# a.screenshot('bdtp.png')

# #案例:在淘宝首页上的搜索栏中输入软件测试,然后按回车,之后打印本页的标题和url
# from selenium.webdriver.common.keys import Keys
# d.get('https://taobao.com')
# sleep(3)
# a=d.find_element_by_id('q')
# a.send_keys('软件测试',Keys.ENTER)
# print(d.title,d.current_url)

# #mouse action
# from selenium.webdriver.common.action_chains import ActionChains
# d.get('https://baidu.com')
# a=d.find_element_by_tag_name('body')
# ActionChains(d).context_click(a).perform()
# ActionChains(d).move_to_element(d.find_element_by_partial_link_text('新闻')).perform()
# sleep(2)
# ActionChains(d).move_to_element(d.find_element_by_partial_link_text('地图')).perform()
# sleep(2)
# ActionChains(d).move_to_element(d.find_element_by_partial_link_text('视频')).perform()
# sleep(2)
# ActionChains(d).move_to_element(d.find_element_by_partial_link_text('学术')).perform()
# sleep(2)
# d.quit()

# #案例:在百度搜索栏中,进行输入,删除,全选,剪切,粘贴功能
# d.get('https://baidu.com')
# a=d.find_element_by_id('kw')
# a.send_keys('123456789',Keys.BACKSPACE,Keys.BACKSPACE)
# sleep(2)
# a.send_keys(Keys.BACKSPACE,Keys.BACKSPACE)
# sleep(2)
# a.send_keys(Keys.CONTROL,"a")
# sleep(2)
# a.send_keys(Keys.CONTROL,"x")
# sleep(2)
# a.send_keys(Keys.CONTROL,"v")
# sleep(2)

#案例:进入淘宝,然后设置浏览器的大小400,500,然后最大,最小,再最大,转入到百度,然后后退,再前进
# d.get('https://taobao.com')
# sleep(2)
# d.set_window_size(400,500)
# sleep(2)
# d.maximize_window()
# sleep(2)
# d.minimize_window()
# sleep(2)
# d.maximize_window()
# sleep(2)
# d.get('https://baidu.com')
# sleep(2)
# d.back()
# sleep(2)
# d.forward()

# #案例:打开淘宝,刷新页面,点击天猫超市,然后截图,然后关闭淘宝首页,最后退出浏览器
# d.get('https://taobao.com')
# sleep(2)
# d.refresh()
# sleep(2)
# d.find_element_by_partial_link_text('天猫超市').click()
# sleep(2)
# d.get_screenshot_as_file('jt1.png')
# sleep(2)
# d.close()
# sleep(2)
# d.quit()

# #获取淘宝首页的句柄
# d.get('https://taobao.com')
# sleep(2)
# print(d.current_window_handle)

# # 把天猫超市窗口绑定给浏览器
# d.get('https://taobao.com')
# sleep(2)
# d.find_element_by_partial_link_text('天猫超市').click()
# sleep(2)
# a=d.window_handles
# d.switch_to.window(a[1])
# sleep(2)
# d.close()


# #案例：打开百度首页，点击新闻，点击地图，点击视频，然后关闭地图页面,截取视频页面的图像，退出浏览器
# d.get('https://baidu.com')
# sleep(2)
# d.find_element_by_partial_link_text('新闻').click()
# d.find_element_by_partial_link_text('地图').click()
# d.find_element_by_partial_link_text('视频').click()
# sleep(2)
# a=d.window_handles
# d.switch_to.window(a[2])
# sleep(2)
# d.close()
# d.switch_to.window(a[1])
# sleep(2)
# d.get_screenshot_as_file('bdsp.png')
# d.quit()
