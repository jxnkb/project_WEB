#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# 1.简述自动化测试流程？
# 答:自动测试决定
#   测试工具获取
#   自动化测试引入
#   制定测试计划,测试设计,测试开发
#   测试执行与管理
#   测试审评和评估

# 2.简述自动化测试的优势和局限性？
# 答:优势:可重复,可程序化,可靠,提高测试的精确度,提升测试资源的利用率
# 局限性:如果代码不对，就无法得出准确结果;如果被测试的程序界面修改了，代码也不能正常运行没有错误联想功能

# 3.请在电商网站上找10个元素,用id和name方式获取,打印元素除id和name外的其他属性,提交到git上
from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/")
# e=dr.find_element_by_name('kw')
# print(e.get_attribute('type'))
# dr.quit()

# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/")
# e=dr.find_element_by_id('top-userbar')
# print(e.get_attribute('class'))
# dr.quit()

# 四.电商网站上找5个超链接元素,通过超链接文字获取元素,打印链接地址,提交到git上
dr=webdriver.Firefox()
dr.get("http://39.96.181.61/qftest-ds/")
e=dr.find_element_by_link_text('首页')  #dsfs #中国 wan #a  #dady
print(e.get_attribute('href'))
dr.quit()

