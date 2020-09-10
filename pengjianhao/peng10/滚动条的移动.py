#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
from time import  sleep
'''
使用JS实现
• 到底部：js="document.documentElement.scrollTop=10000"
• 到顶部： js="document.documentElement.scrollTop=0"
• 左右移动：js="window.scrollTo(200,1000)"
• Js代码的执行需要用到的方法：driver.execute_script(js)
'''
dr=webdriver.Firefox()
dr.get('https://lol.qq.com')
#改变窗口的大小
# dr.set_window_size(600,100)
sleep(2)
#往下移动滚动条
str1="document.documentElement.scrollTop=10000"
dd='='
mystr=str1.split(dd)
js=(mystr[0])
js1=(mystr[1])
a=100
while True:
    a+=5
    sa=str(a)
    d=js+'='+sa
    sleep(0.1)
    dr.execute_script(d)
    if a=='3500' or a==3500:
        while True:
            a -= 5
            sa = str(a)
            d = js + '=' + sa
            sleep(0.1)
            dr.execute_script(d)
            if a=='0' or a==0:
                break

#往上移动滚动条
# js='document.documentElement.scrollTop=0'
# dr.execute_script(js)
# sleep(2)
#
# js="window.scrollTo(100,200)"
# dr.execute_script(js)
# sleep(2)



