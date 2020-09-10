#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# 二．	页面滚动条，做成缓慢下拉的动画效果

'''
使用JS实现
• 到底部：js="document.documentElement.scrollTop=10000"
• 到顶部： js="document.documentElement.scrollTop=0"
• 左右移动：js="window.scrollTo(200,1000)"
• Js代码的执行需要用到的方法：driver.execute_script(js)
'''
'''
from selenium import webdriver
import time

dr=webdriver.Firefox()
dr.get('https://www.163.com/')
for i in range(10000):
    js="window.scrollBy(0,100)"
    dr.execute_script(js)
    time.sleep(1)

dr.quit()
'''

# 三．	登入电商系统，然后添加收件地址，然后退出电商系统，每个用例都写成模块化。

'''
#引入模块
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep

def login(dr):

    #获取登陆元素并点击
    dr.find_element_by_link_text('登陆').click()
    sleep(3)
    #获取用户名输入框并输入数据
    dr.find_element_by_id('username').send_keys('test9')
    sleep(3)
    #获取密码框并输入密码
    dr.find_element_by_id('password').send_keys('123456')
    sleep(3)
    #获取'登陆'按钮并点击
    dr.find_element_by_link_text('登     陆').click()
    sleep(3)


def setadr(dr):

    #获取'编辑'元素并点击
    dr.find_element_by_link_text('编辑').click()
    sleep(2)
    #获取'收件地址'元素并点击
    dr.find_element_by_link_text('收件地址').click()
    sleep(2)
    #获取'新建收件人信息'元素并点击
    dr.find_element_by_id('newadrbtn').click()
    sleep(2)
    #获取'收件人'输入框并输入信息
    dr.find_element_by_id('receiver').send_keys('周周')
    sleep(2)
    #获取所在地区-'选择省份'下拉列表框元素并点击
    e=dr.find_element_by_id('areaslt-province')
    e.click()
    #选择省份
    liste=Select(e)
    liste.select_by_index(19)
    sleep(2)
    #获取所在地区-'选择城市'下拉列表框按钮元素并点击
    e = dr.find_element_by_id('areaslt-city')
    e.click()
    #选择城市
    liste = Select(e)
    liste.select_by_index(3)
    sleep(2)
    #获取所在地区-'选择区/县'下拉列表框按钮元素并点击
    e = dr.find_element_by_id('areaslt-borough')
    e.click()
    #选择区/县
    liste = Select(e)
    liste.select_by_index(4)
    sleep(2)
    #获取详细地址输入框并输入详细地址
    dr.find_element_by_id('address').send_keys('西部硅谷')
    sleep(2)
    #获取邮编输入款并输入邮编
    dr.find_element_by_id('zip').send_keys('518101')
    sleep(2)
    #获取手机号码输入框并输入手机号码
    dr.find_element_by_id('mobile').send_keys('15770835722')
    sleep(2)
    #获取'保存信息'按钮元素并点击
    dr.find_element_by_class_name('sm-green').click()
    sleep(5)


def logout(dr):
    # 获取用户名元素,并进行鼠标悬停,然后获取退出元素,并进行点击
    e = dr.find_element_by_xpath('//*[@id="top-userbar"]/a')
    ActionChains(dr).move_to_element(e).perform()
    dr.find_element_by_link_text('退出').click()


if __name__ == '__main__':

    # 打开浏览器
    dr = webdriver.Firefox()
    # 打开电商系统
    dr.get('http://39.96.181.61/qftest-ds/')
    # 调用登入函数
    login(dr)
    sleep(5)
    # 调用添加收件地址函数
    setadr(dr)
    sleep(5)
    # 调用退出函数
    logout(dr)
    sleep(5)
    # 关闭浏览器
    dr.quit()

'''

# 四．	把注册功能写成模块化

'''
#引入模块
from selenium import webdriver
from time import sleep

def signin(dr):

  #获取免费注册元素并点击
  dr.find_element_by_link_text('免费注册').click()
  sleep(3)
  #获取用户名输入框,并输入数据
  e1=dr.find_element_by_id('username')
  e1.send_keys('test77')
  sleep(3)
  #获取邮箱输入框,并输入数据
  e2=dr.find_element_by_id('email')
  e2.send_keys('test77@qq.com')
  sleep(3)
  #获取密码输入框,并输入数据
  e3=dr.find_element_by_id('password')
  e3.send_keys('123456')
  sleep(3)
  #获取确认密码输入框,并输入数据
  e4=dr.find_element_by_id('repassword')
  e4.send_keys('123456')
  sleep(3)
  #获取'立即注册'元素,并点击
  e5=dr.find_element_by_link_text('立即注册')
  e5.click()
  sleep(7)
  #获取当前页面的url
  URL=dr.current_url
  print(URL)
  sleep(5)
  #进行判断http://39.96.181.61/qftest-ds/user/index.html
  if URL == 'http://39.96.181.61/qftest-ds/user/index.html':
    print('注册成功')
  sleep(3)


if __name__ == '__main__':

    # 打开浏览器
    dr=webdriver.Firefox()
    # 打开电商系统
    dr.get('http://39.96.181.61/qftest-ds/')
    # 调用登入函数
    signin(dr)
    sleep(3)

    # 关闭浏览器
    dr.quit()
'''

# 案例:用xls存储数据的方式驱动脚本开发
# excel存储数据进行数据驱动（熟练使用）：
#     先安装xlrd模块：cmd  ->  pip3 install xlrd
# 从excel文件中读入数据：
#     1、导包，import xlrd
#     2、使用xlrd的方法打开excel文件（创建一个文件对象）
#     3、获取excel文件的sheet页
#     4、获取sheet页中的行数据、列数据、单元格数据
#     5、需要遍历数据，你先要直到文件中有多少行、多少列数据
#     6、使用for循环遍历

'''
from selenium import webdriver
import os
import xlrd
import time

def read_EXCE(path,index):
    aa=xlrd.open_workbook(path) #打开xls或xlsx文件
    bb=aa.sheets()[index] #获取xls或xlsx文件中的子表
    return bb #返回子表中的所有内容

cc=read_EXCE('1.xlsx',0) #0表示第一个子表,1表示第二个子表....
mylist = []
for i in range(0,cc.nrows): #获取子表中的所有行
    dd=cc.row_values(i) #得到一行数据,以列表形式返回
    mylist.append(dd[0])
print(mylist)

dr=webdriver.Firefox()
# 打开网站
dr.get('http://39.96.181.61/qftest-ds/')
time.sleep(2)
# 获取免费注册元素并点击
dr.find_element_by_link_text('免费注册').click()
time.sleep(3)
# 获取用户名输入框,并输入数据
dr.find_element_by_id('username').send_keys(mylist[0])
time.sleep(2)
# 获取邮箱输入框,并输入数据
dr.find_element_by_id('email').send_keys(mylist[1])
time.sleep(2)
# 获取密码输入框,并输入数据
dr.find_element_by_id('password').send_keys(int(mylist[2]))
time.sleep(2)
# 获取确认密码输入框,并输入数据
dr.find_element_by_id('repassword').send_keys(int(mylist[3]))
time.sleep(2)
# 获取'立即注册'元素,并点击
dr.find_element_by_link_text('立即注册').click()

#休眠一下
time.sleep(12)

#获取断言的url
myurl=mylist[4]

if dr.current_url==myurl:
    print("测试用例ok")
else:
    print("测试用例错误")

time.sleep(2)
dr.quit()
'''