from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')


try:
	input1 = browser.find_element(By.NAME, 'firstname')
	input1.send_keys('Ivan')
	input2 = browser.find_element(By.NAME, 'lastname')
	input2.send_keys('Petrov')
	input3 = browser.find_element(By.NAME, 'email')
	input3.send_keys('alisasasasasa@mail.ru')
	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'file.txt')
	input_file = browser.find_element(By.ID, 'file')
	input_file.send_keys(file_path)
	submit = browser.find_element(By.CLASS_NAME, 'btn')
	submit.click()


finally:
	time.sleep(10)
	browser.quit()



