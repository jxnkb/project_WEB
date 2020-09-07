#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
'''
1.简述自动化测试流程？
    1.自动测试决定
    2.测试工具获取
    3.自动化测试引入
    4.制定测试计划（5w1H）、测试设计（测试用例：测试步骤、测试数据、预期结果）、测试开发（编写测试脚本、在工具中完成测试场景的开发）---最关键的一个环节
    5.测试执行与管理（脚本的运行、过程监控、结果管理）
    6.测试审评和评估
2.简述自动化测试的优势和局限性？
    效率高，优化成本，可靠，可重用，规范化；
    会遗漏部分缺陷。




'''






from selenium import webdriver
from time import sleep
d=webdriver.Firefox()
d.get('http://39.96.181.61/qftest-ds/user/register.html')
a=d.find_element_by_id("register-form") #type,rel,href
a1=a.get_attribute('method')
a2=a.get_attribute('action')
print(a1,a2)



# 4.电商网站上找5个超链接元素,通过超链接文字获取元素,打印链接地址,提交到git上

b=d.find_element_by_partial_link_text("Verydows")
b1=b.get_attribute('href')
print(b1)

d.quit()










