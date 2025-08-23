from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
import time


def answer(a, b):
	return a + b


try:
	link = 'https://suninjuly.github.io/selects1.html'
	browser = webdriver.Chrome()
	browser.get(link)


	a = int(browser.find_element(By.ID, 'num1').text)
	b = int(browser.find_element(By.ID, 'num2').text)


	select = Select(browser.find_element(By.ID, 'dropdown'))
	select.select_by_value(str(answer(a, b)))
	submit = browser.find_element(By.CLASS_NAME, 'btn')
	submit.click()

finally:
	time.sleep(10)
	browser.quit()
	