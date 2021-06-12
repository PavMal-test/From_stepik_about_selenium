# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 22:55:33 2021

@author: user
"""

import time
from selenium import webdriver
import math


link="http://suninjuly.github.io/redirect_accept.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser=webdriver.Chrome()
browser.get(link)

first_window = browser.window_handles[0]



try:
    
    
    btn1=browser.find_element_by_css_selector('.trollface.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn1)
    btn1.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_element=browser.find_element_by_id('input_value')
    x=x_element.text
    y=calc(x)
    
    input1=browser.find_element_by_id('answer')
    input1.send_keys(y)
    
    btn2=browser.find_element_by_css_selector('.btn-primary')
    btn2.click()
    
    
    
    
finally:
    time.sleep(10)
    browser.quit()