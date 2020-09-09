#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#鼠标键盘
#案例:淘宝首页搜索栏上面点击天猫,然后
# 在搜索栏写'软件测试',之后再清除
from selenium import webdriver
import os
from time import sleep
dr=webdriver.Firefox()
# dr.get('http://www.taobao.com')
# e=dr.find_element_by_xpath('//ul[@class="ks-switchable-nav"]/li[2]')
# sleep(2)
# e.click()
# e1=dr.find_element_by_id('q')
# e1.send_keys('软件测试')
# e1.clear()
# dr.quit()

#获取元素标签的属性值
# dr.get('http://www.taobao.com')
# e=dr.find_element_by_id('q')
# print(e.get_attribute('role'))
# print(e.get_property('name'))  #自己定义的显示None
# dr.quit()

#获取元素的属性信息
# dr.get('http://www.taobao.com')
# e=dr.find_element_by_id('q')
# print(e.size)  #size
# e=dr.find_element_by_id('mtb')
# print(e.text)  #text
# dr.quit()


#其他操作
#案例:在淘宝首页上的搜索栏中输入软件测试,
# 然后按回车,之后打印本页的标题和url
# dr.get('http://www.taobao.com')
# e=dr.find_element_by_id('q')
# e.send_keys('软件测试')
# sleep(3)
# e.submit()
# print(dr.title)
# print(dr.current_url)
# dr.quit()

#鼠标操作
#右键单击/双击/鼠标悬停
# from selenium.webdriver.common.action_chains import ActionChains
# dr.get('http://www.baidu.com')
# e=dr.find_element_by_link_text('更多')
# ActionChains(dr).context_click(e).perform()
# dr.quit()
#拖动
# dr.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# dr.switch_to.frame('iframeResult')
# a=dr.find_element_by_id('draggable')
# b=dr.find_element_by_id('droggable')
# ActionChains(dr).drag_and_drop(a,b).perform()
# dr.quit()




#下拉列表的操作
# from selenium.webdriver.support.select import Select
# dr.get('file:///'+os.path.abspath('03HTML/06.html'))
# e=dr.find_element_by_name('sel')
# list=Select(e)
# list.select_by_index(3)
# list.select_by_visible_text('北京烤鸭')
# list.select_by_value('aaa')
# dr.quit()



#键盘操作
#案例:在百度搜索栏中,进行输入,删除,全选,剪切,粘贴功能
# from selenium.webdriver.common.keys import Keys
# dr.get('http://www.baidu.com')
# e=dr.find_element_by_id('kw')
# e.send_keys('软件测试书')
# e.send_keys(Keys.BACK_SPACE)
# e.send_keys(Keys.CONTROL,'a')
# e.send_keys(Keys.CONTROL,'x')
# e.send_keys(Keys.CONTROL,'v')
# dr.quit()


#浏览器控制
#案例:打开淘宝,刷新页面,点击天猫超市,然后截图,然后关闭淘宝首页,最后退出浏览器
# dr.get('http://www.taobao.com')
# dr.refresh()
# e=dr.find_element_by_link_text('天猫超市')
# dr.get_screenshot_as_file('01.png')
# dr.close()
# dr.quit()




#多窗口处理
#案例：打开百度首页，点击新闻，点击地图，点击视频，然后关闭地图页面,截取视频页面的图像，退出浏览器
# dr.get('http://www.baidu.com')
# dr.find_element_by_link_text('新闻').click()
# dr.find_element_by_link_text('地图').click()
# dr.find_element_by_link_text('视频').click()
# hs=dr.window_handles
# dr.switch_to.window(hs[2])
# dr.close()
# dr.switch_to.window(hs[1])
# dr.get_screenshot_as_file('02.png')
# dr.quit()
