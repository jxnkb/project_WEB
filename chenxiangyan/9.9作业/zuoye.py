#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
############1.鼠标键盘##########
# from selenium import webdriver
# from time import sleep
# dr=webdriver.Firefox()
# dr.get('https://www.baidu.com')
# # dr.get('https://www.baidu.com')
# d=dr.find_element_by_id("kw")
# #在元素中输入文字
# d.send_keys('软件测试')
# sleep(2)
# #清空
# d.clear()
# sleep(2)
# dr.quit()

# e=dr.find_element_by_link_text('新闻')
# #点击元素
# e.click()
# sleep(2)
# dr.quit()

#案例:淘宝首页搜索栏上面点击天猫,
# 然后在搜索栏写'软件测试',之后再清
# dr.get('https://www.taobao.com')
# e=dr.find_element_by_xpath("//ul[@class='ks-switchable-nav']/li[2]")
# sleep(2)
# e.click()
# ee=dr.find_element_by_id('q')
# ee.send_keys('软件测试')
# sleep(2)
# ee.clear()
# sleep(2)
# dr.quit()
# clear():清除文本
# send_keys(value):模拟按键输入
# click():单击元素，如按钮操作

##########获取元素的属性值#######
# from selenium import webdriver
# import os
# dr=webdriver.Firefox()
# dr.get('file:///'+os.path.abspath('02HTML.html'))
# e=dr.find_element_by_id('maker')
# print(e.get_attribute('id'))
# print(e.get_attribute('lala'))
# print(e.get_property('id')) #获得属性值。自定义属性不能获取
# print(e.get_property('lala'))

#########获取元素的属性信息########
# text:获取元素标签对之间的文本值
# size：获取元素的尺寸大小
# id： seleniumn 内部的一个元素属性，用于判断两个元素是否是相同的元素
# screenshot()给元素截图，保存为png格式

# from selenium import webdriver
# from time import sleep
# import os
# dr=webdriver.Firefox()
# dr.get('file:///'+os.path.abspath('02HTML.html'))
# e=dr.find_element_by_id('maker')
# print(e.text)#获取标签对之间的文字
# ee=dr.find_element_by_id('maker2')
# ee2=dr.find_element_by_name('username')
# print(ee.get_attribute('name'))
# print(ee.size)
# print(ee.id)#获取的是元素的属性信息id，不是属性id的值
# print(ee2.id)
# ee2.screenshot('11.png')
#
#
# dr=webdriver.Firefox()
# dr.get('http://www.baidu.com')
# e=dr.find_element_by_tag_name('body')
# e.screenshot('22.png')
# dr.quit()

##########4.获取元素基本状态信息#########
# from selenium import webdriver
# import os
# dr=webdriver.Firefox()
# dr.get('file:///'+os.path.abspath('04HTML.html'))
# e=dr.find_element_by_name('c1')
# ee=dr.find_element_by_name('c3')
# print(e.is_selected())#判断元素是否被选择
# print(ee.is_selected())


###########5.其他操作#####
# from selenium import webdriver
# import os
# from time import sleep
# dr=webdriver.Firefox()
# dr.get('http://www.baidu.com')
# e=dr.find_element_by_id('kw')
# e.send_keys('软件测试')
# sleep(2)
# e.submit()#回车
# print(dr.title)#获取页面标题
# print(dr.current_url)#获取页面的地址
# sleep(2)
# dr.quit()

#案例:在淘宝首页上的搜索栏中输入软件测试,
# 然后按回车,之后打印本页的标题和url
# dr=webdriver.Firefox()
# dr.get('http://www.taobao.com')
# e=dr.find_element_by_id('q')
# e.send_keys('软件测试')
# sleep(2)
# e.submit()
# print(dr.title)
# print(dr.current_url)
# sleep(2)
# dr.quit()

############6.鼠标########
# from selenium import webdriver
# import os
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
# dr=webdriver.Firefox()
# dr.get('http://www.baidu.com')
# e=dr.find_element_by_tag_name('body')
# ActionChains(dr).context_click(e).perform()#鼠标右键单击
# sleep(2)
# dr.quit()

# dr.get('file://'+os.path.abspath('06HTML.html'))
# e=dr.find_element_by_xpath('//input[@value="按键2"]')
# ActionChains(dr).double_click(e).perform()


#########7.鼠标悬停########
# from selenium import webdriver
# import os
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
# dr=webdriver.Firefox()
# dr.get('https://baidu.com')
# e=dr.find_element_by_tag_name('span')
# print(e.get_attribute('id'))
# e=dr.find_element_by_link_text('更多')
#
# ActionChains(dr).move_to_element(e).perform()#鼠标悬停

##########8.鼠标拖动#########
# from selenium import webdriver
# import os
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
# dr=webdriver.Firefox()
# dr.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# dr.switch_to.frame('iframeResult')#切换到目标元素的窗口iframeResult
# s=dr.find_element_by_id('draggable')#确定要拖拽的目标元素
# e=dr.find_element_by_id('droppable')#要拖入的目标元素
# ActionChains(dr).drag_and_drop(s,e).perform()

###9.下拉列表的操作######
# from selenium import webdriver
# import os
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
# from selenium.webdriver.support.select import Select
# dr=webdriver.Firefox()
# '''
# 3.选择下列列表中的元素有三种方式
# • select_by_index() #索引
# • select_by_visible_text()#文本
# • select_by_value()#value属性的值
# '''
# dr.get('file://'+os.path.abspath('09HTML.html'))
# e=dr.find_element_by_name('sel')
# sleep(2)
# listobj=Select(e)#把元素转换为列表
# listobj.select_by_index(0)#通过下标选择选项
# listobj.select_by_value('aaaa')#通过value值选择选项
# listobj.select_by_visible_text('北京烤鸭')

##############10.键盘的操作########
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# import os
# dr=webdriver.Firefox()
# dr.get('file:///'+os.path.abspath('10HTML.html'))
# e=dr.find_element_by_name('文本')
# sleep(2)
# #往元素输入内容
# e.send_keys('maker')
# sleep(2)
# e.send_keys(Keys.BACK_SPACE) #删除一个字符
# sleep(2)
# e.send_keys(Keys.CONTROL,'a')#全选
# sleep(2)
# e.send_keys(Keys.CONTROL,'x')#剪切
# sleep(2)
# e.send_keys(Keys.CONTROL,'v')#粘贴
# sleep(2)
#
# #案例:在百度搜索栏中,进行输入,删除,全选,剪切,粘贴功能
# dr.get('http://www.baidu.com')
# e=dr.find_element_by_id('kw')
# sleep(2)
# e.send_keys('benchi')
# sleep(2)
# e.send_keys(Keys.BACK_SPACE)
# sleep(2)
# e.send_keys(Keys.CONTROL,'a')
# sleep(2)
# e.send_keys(Keys.CONTROL,'x')
# sleep(2)
# e.send_keys(Keys.CONTROL,'v')
# sleep(2)
# e.send_keys(Keys.ENTER)#回车
# dr.quit()

##########11.浏览器的控制###########
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
dr=webdriver.Firefox()
# dr.get('http://www.baidu.com')
# sleep(2)
# dr.set_window_size(200,400)#设置浏览器窗口的大小
# sleep(2)
# dr.minimize_window()
# sleep(2)
# dr.maximize_window()
# sleep(2)
#
# dr.get('http://www.taobao.com')
# sleep(2)
# dr.back()
# sleep(2)
# dr.forward()
# sleep(2)
# dr.quit()

#案例:进入淘宝,然后设置浏览器的大小400,500,然后最大,最小,再最大,转入到百度,然后后退,再前进
# dr=webdriver.Firefox()
# dr.get('http://www.taobao.com')
# sleep(2)
# dr.set_window_size(400,600)
# sleep(2)
# #让浏览器最大化
# dr.maximize_window()
# sleep(2)
# #让浏览器最小化
# dr.minimize_window()
# sleep(2)
# #让浏览器最大化
# dr.maximize_window()
# sleep(2)
#
# #转到别的页面
# dr.get('http://www.baidu.com')
# sleep(2)
# dr.back()
# sleep(2)
# dr.forward()
# sleep(2)
# dr.quit()

############12.浏览器的操作########
# from selenium import webdriver
# from time import sleep
# dr=webdriver.Firefox()
# dr.get('http://www.taobao.com')
# sleep(2)
# dr.refresh()
# sleep(2)
# dr.get_screenshot_as_file('ss.png')#截图
# sleep(2)
# dr.find_element_by_link_text('聚划算').click()
# sleep(2)
# dr.close()
# sleep(2)
# dr.quit()
#案例:打开淘宝,刷新页面,点击天猫超市,然后截图,然后关闭淘宝首页,最后退出浏览器
# dr.get('http://www.taobao.com')
# sleep(2)
# dr.refresh()#刷新
# sleep(2)
# #点击天猫超市
# dr.find_element_by_link_text('天猫超市').click()
# sleep(2)
# #截图
# dr.get_screenshot_as_file('qq.png')
# dr.close()
# dr.quit()

##########13.多窗口处理#####
'''
  • 获取当前窗口句柄：driver.current_window_handle
    • 获取浏览器所有句柄：driver.window_handles
    • 切换到指定的浏览器窗口：driver.switch_to.window(handle)
'''
# from selenium import webdriver
# from time import sleep
# dr=webdriver.Firefox()
# dr.get('http://www.taobao.com')
# hs=dr.window_handles#获取淘宝首页的句柄
# print(type(hs))
# dr.find_element_by_link_text('聚划算').click()
# dr.find_element_by_link_text('天猫超市').click()
# # dr.switch_to.window(hs[1])#把天猫超市窗口绑定给浏览器
# dr.switch_to.window(hs[1])
# sleep(3)
# dr.get_screenshot_as_file('qk.png')
# sleep(3)
# dr.quit()

#二．	自动化登入电商系统后台,登入后截图
#注意：网站,用户名和密码要通过代码获取

f=open('denglu.txt','r',encoding='gbk')
a = f.read().splitlines()
h=a[7]
# w=a[1]
# y=a[3]
# m=a[5]
# from selenium import webdriver
# from time import sleep
# import os
# dr=webdriver.Firefox()
#
# dr.get(w)
# e=dr.find_element_by_id('username')
# # print(e.get_attribute('type'))
# e.send_keys(y)
# sleep(2)
# f=dr.find_element_by_id('password')
# f.send_keys(m)
# sleep(2)
# g=dr.find_element_by_link_text('登 陆')
# g.click()
# sleep(10)
# dr.get_screenshot_as_file('ss.png')
# dr.quit()

h=a[7]
from selenium import webdriver
from time import sleep
import os
dr=webdriver.Firefox()
dr.get(h)
z=dr.find_element_by_name('kw')
z.send_keys('苹果')
sleep(3)
z.submit()

# c=dr.find_element_by_xpath('//div[@class="im"]/a/img')
c=dr.find_element_by_xpath("//li[@title='苹果']/h3/a")
c.click()
sleep(3)
o=dr.find_element_by_link_text('加入购物车')
o.click()
sleep(5)
dr.get_screenshot_as_file('rr.png')
dr.quit()