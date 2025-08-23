from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')


try:
	def calc(x):
		return math.log(abs(12 * math.sin(x)))


	button = browser.find_element(By.ID, 'book')
	WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
	button.click()


	x = int(browser.find_element(By.ID, 'input_value').text)
	input = browser.find_element(By.ID, 'answer')
	input.send_keys(calc(x))
	browser.find_element(By.ID, 'solve').click()


finally:
	time.sleep(10)
	browser.quit()
