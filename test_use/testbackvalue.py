# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 21:21:48 2019

file:///G:/gaobur/%E7%BD%91%E9%A1%B5%E8%AE%B0%E5%BD%95/%E6%88%91%E7%9A%84%20BK%20%E4%BD%93%E9%AA%8C%20-%20%E8%B0%A2%E8%B0%A2.html

@author: bye
"""

from selenium import webdriver
import time

def login():
    driver = webdriver.Chrome()
    driver.get("file:///G:/gaobur/%E7%BD%91%E9%A1%B5%E8%AE%B0%E5%BD%95/%E6%88%91%E7%9A%84%20BK%20%E4%BD%93%E9%AA%8C%20-%20%E8%B0%A2%E8%B0%A2.html")

    time.sleep(3)
#    login = driver.find_elements_by_class_name('ValCode').text
    #//*[@id="finishIncentiveHolder"]/p[3]
    #/html/body/div[1]/div[3]/div[2]/form/div/div/div/div/div[1]/div/p[3]
    #driver.find_element_by_xpath('//input[@id="NextButton"]')
    login = driver.find_element_by_xpath('//*[@id="finishIncentiveHolder"]/p[3]').text
    print(login)
#    print(type(login)) #查看变量类型
    with open('test.txt', 'w') as f:     # 打开test.txt   如果文件不存在，创建该文件。
        f.write(login)  # 把变量var写入test.txt。这里var必须是str格式，如果不是，则可以转一下。


            
if __name__ == '__main__':
    login()