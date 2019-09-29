# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 08:42:41 2019

@author: bye
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.common.keys import Keys
import time
 
 
class TellBK(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
 
    def test_fillFeedBack(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://tellburgerking.com.cn')
        time.sleep(10)
 
        # Page 1 - Welcome
        # 点击继续
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="NextButton"]')))
        element.click()
 
        # Page 2 - Fill the codes and continue
        # 填写调查代码, FeedbackCode.txt保存调查代码，3个一组，空格分开
        codefile = open('FeedbackCode.txt', 'r')
        feedbackcode = codefile.read().split(" ")
        codefile.close()
        for i in range(len(feedbackcode)):
            driver.find_element_by_xpath('//input[@id="CN{}"]'.format(i+1)).send_keys(feedbackcode[i])
        # 点击开始
        driver.find_element_by_xpath('//input[@id="NextButton"]').submit()
 
        # Page 3 - Page 12
        radiovaluelist = [('simpleInput rblv', 2), ('simpleInput rblv', 2), ('simpleInput rblv', 1),
                          ('simpleInput rbl', 5), ('simpleInput rbl', 5), ('simpleInput rbl', 5),
                          ('simpleInput rbl', 5), ('simpleInput rbl', 9), ('simpleInput rbl', 2),
                          ('simpleInput rbl', 5)]
        for radiovalue in radiovaluelist:
            self.selectRadiosSubmit(radiovalue)
 
        # Page 13 - Say something
#　　　　with open('HappyReason.txt') as filereason:
#            reasontext = filereason.read()
#        driver.find_element_by_xpath('//textarea[@id="S000122"]').send_keys(reasontext)
        # Next
        driver.find_element_by_xpath('//input[@id="NextButton"]').submit()
 
        # Page 14 - What you ordered
        element = self.driver.find_element_by_id("R000091")#我没有点主食
        self.driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_xpath('//input[@id="NextButton"]').submit()
 
        element = self.driver.find_element_by_id("R000097")#我没有点小时或甜品
        self.driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_xpath('//input[@id="NextButton"]').submit()
 
        # Page 16 - Page 19
        radiovaluelist = [('simpleInput rbl', 1), ('simpleInput rblv', 5),
                          ('simpleInput rblv', 2), ('simpleInput rblv', 1), ]
        for radiovalue in radiovaluelist:
            self.selectRadiosSubmit(radiovalue)
 
        # Page - Gender and age
        driver.find_element_by_xpath("//select[@id='R069000']").find_element_by_xpath("//option[@value='2']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//select[@id='R070000']").find_element_by_xpath("//option[@value='3']").click()
        driver.find_element_by_xpath('//input[@id="NextButton"]').submit()
        time.sleep(3)
 
        # Page -  Share zip code
        driver.find_element_by_xpath('//input[@id="NextButton"]').click()
        time.sleep(10)
 
        # Page - Last page get screenshot
#        driver.get_screenshot_as_file('%s.png' % time.strftime("%Y%m%d.%H.%M.%S"))
        # Page - Last page get saveintxt
        login = driver.find_element_by_xpath('//*[@id="finishIncentiveHolder"]/p[3]').text
        print(login)
                        #    print(type(login)) #查看变量类型
        with open('%s.txt' % feedbackcode, 'w') as f:     # 打开test.txt   如果文件不存在，创建该文件。
            f.write(login)
      
    def selectRadiosSubmit(self, radioattribute):
        elements = self.driver.find_elements_by_xpath(
            '//input[@class="{}" and @value="{}"]'.format(radioattribute[0], radioattribute[1]))
        print(len(elements))
        for element in elements:
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(3)
        self.driver.find_element_by_xpath('//input[@id="NextButton"]').submit()
        time.sleep(3)
 
    def tearDown(self) -> None:
        self.driver.quit()
 
 
if __name__ == "__main__":
    unittest.main()
    
    
    
#    　　需要注意的几个问题：
#
#汉堡王客户调查页面的Radio是没办法直接调用click的， 会抛‘could not be scrolled into view’ Exception.需要调用Javascript进行点击。没有试ActionChains可否操作， 同样的问题对于checkbox也是，需要调用Javascript进行点击。
#汉堡王客户调查页面的Radio也是有区别的，有的class = 'simpleInput rbl', 有的class = 'simpleInput rblv'
#页面上多组Radio的ID值是变动的，不能直接使用，所以用了class 加 value定位。原本我打算用ends-with的，但是试了好像不行。这个ends-with对于xpath的定位比较弱，不太好匹配上，即使你觉得本应该没问题， 不建议使用。
#selenimu的上脚本点击的速度是远超过页面响应速度的，所以必要的时候，要强制time.sleep(), 或者使用WebDriver的显示等待。建议每个action后都稍微sleep下，特别是页面跳转的时候。对于关键元素WebDriver进行check
#这些页面里面没有iframe，所以你不会碰到iframe导致的元素找不到的问题。
#还需要注意button上的click()和submit()方法是略有不同的。click()对于button来说都可以使用，submit()用于在点击button后提交表单数据，使用需要满足一定的条件， 比如按钮的type='submit',而且这个按钮要在<form> tag里面。
#我没有添加exception的处理，这里的代码只是基础代码，可以自行优化，以及组织。
#最后的验证码是保存在一个png文件里面的，需要自己手动去查看。没来得及是实现和抓取。