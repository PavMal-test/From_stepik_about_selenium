# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 21:03:00 2021

@author: user
"""

from selenium import webdriver

import unittest



browser = webdriver.Chrome()

browser.implicitly_wait(3)



# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
class TestStringMethods(unittest.TestCase):

    def test_reg1(self):
        browser = webdriver.Chrome()
        
        link = "http://suninjuly.github.io/registration1.html"

        browser.get(link)
       

# Заполняем обязательные поля

        input1= browser.find_element_by_css_selector("input.first:required")
        input1.send_keys("Ivan")
        
        input2= browser.find_element_by_css_selector("input.second:required")
        input2.send_keys("Ivanof")   
        
        input3= browser.find_element_by_css_selector("input.third:required")
        input3.send_keys("Ivanofloop.com")
        
        
                                                     
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        
        h1= browser.find_element_by_css_selector('.container h1')
        self.assertEqual(h1.text, 'Congratulations! You have successfully registered!', 'NO successfull registration message')
        
        browser.quit()
        
        
    def test_reg2(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"

        browser.get(link)

# Заполняем обязательные поля
        input1= browser.find_element_by_css_selector("input.first:required")
        input1.send_keys("Ivan")
        input2= browser.find_element_by_css_selector(" input.second:required")
        input2.send_keys("Ivanof")    
        input3= browser.find_element_by_css_selector("input.third:required")
        input3.send_keys("Ivanofloop.com")
        
                                                     
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        
        h1= browser.find_element_by_css_selector('.container h1')
        self.assertEqual(h1.text, 'Congratulations! You have successfully registered!', 'NO successfull registration message')
        browser.quit()

if __name__ == '__main__':
    unittest.main() 
    
browser.quit()
   # ожидание чтобы визуально оценить результаты прохождения скрипта

    # закрываем браузер после всех манипуляций




    