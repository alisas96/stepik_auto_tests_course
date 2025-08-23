from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
	result = math.log(abs(12 * math.sin(x)))
	return result


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')


try:
	browser.find_element(By.CLASS_NAME, 'btn').click()
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)
	x = int(browser.find_element(By.ID, 'input_value').text)
	input = browser.find_element(By.ID, 'answer')
	input.send_keys(calc(x))
	browser.find_element(By.CLASS_NAME, 'btn').click()


finally:
	time.sleep(10)
	browser.quit()