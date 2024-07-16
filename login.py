from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

url = 'https://secure-retreat-92358.herokuapp.com/'
driver.get(url)
time.sleep(4)

f_name = driver.find_element(By.NAME, value='fName')
l_name = driver.find_element(By.NAME, value='lName')

email = driver.find_element(By.NAME, value='email')

f_name.send_keys('Sagar')
l_name.send_keys('Alias')
email.send_keys('jacky@test.com')

button = driver.find_element(By.XPATH, value='//button[@type="submit"]')

button.click()

time.sleep(5)
driver.quit()