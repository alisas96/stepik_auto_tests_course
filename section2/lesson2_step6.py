from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


link = 'https://SunInJuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
	result = (math.log(abs(12 * math.sin(x))))
	return result


try:
	x = int(browser.find_element(By.ID, 'input_value').text)
	input = browser.find_element(By.ID, 'answer')
	input.send_keys(calc(x))
	chekbox = browser.find_element(By.ID, 'robotCheckbox')
	chekbox.click()
	radio = browser.find_element(By.ID, 'robotsRule')
	browser.execute_script('return arguments[0].scrollIntoView(true);', radio)
	radio.click()
	submit = browser.find_element(By.CLASS_NAME, 'btn')
	submit.click()


finally:
	time.sleep(10)
	browser.quit()