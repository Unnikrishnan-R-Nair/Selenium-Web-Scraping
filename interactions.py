from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

url = 'https://en.wikipedia.org/wiki/Main_Page'

driver.get(url)

time.sleep(3)
article_count = driver.find_element(By.CSS_SELECTOR, value='div#articlecount a').text

print(article_count)

search = driver.find_element(By.NAME, value='search')
search.send_keys("Python", Keys.ENTER)


# driver.quit()

