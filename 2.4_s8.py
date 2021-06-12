# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 22:36:53 2021

@author: user
"""

import time
from selenium import webdriver
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link='http://suninjuly.github.io/explicit_wait2.html'

try:
    browser=webdriver.Chrome()
    browser.implicitly_wait(14)
    browser.get(link)   
    
    count=WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
        )
    
    btn1=browser.find_element_by_id("book")
    btn1.click()
    
    x_element=browser.find_element_by_id('input_value')
    x=x_element.text
    y=calc(x)
    
    input1=browser.find_element_by_id('answer')
    input1.send_keys(y)
    
    
    btn2=browser.find_element_by_id("solve")
    btn2.click()
    
finally:
    time.sleep(12)
    browser.quit()