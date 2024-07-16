from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

url = 'https://orteil.dashnet.org/cookieclicker/'
driver.get(url)

time.sleep(3)
got_it_btn = driver.find_element(By.XPATH, value='//a[@class="cc_btn cc_btn_accept_all"]')
got_it_btn.click() if got_it_btn else None
langBtn = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
langBtn.click() if langBtn else None

time.sleep(3)
cookie = driver.find_element(By.ID, value='bigCookie')

# checks for upgrades in every 30 seconds
check_time = int(time.time()) + 30

# game runs for 5 mins and then quits
game_quite_after = int(time.time()) + (5*60)

while True:

    if int(time.time()) == game_quite_after:
        break
    
    cookie.click()

    try:
        close_btn = driver.find_element(By.XPATH, '//div[@class="framed close sidenote"]')
        close_btn.click()
    except:
        pass
    
    if int(time.time()) == check_time:
        products = driver.find_elements(By.CSS_SELECTOR, value='#products .product.unlocked.enabled')
        # print(products)
        print('inside check time')

        # checks for highest possible upgrade available
        for i in range(len(products)-1, -1, -1):
            products[i].click()
        check_time = int(time.time()) + 30


time.sleep(2)
while True:
    try:
        # score of 'speed of click' will be displayed at the end
        score_element = driver.find_element(By.XPATH, value='//div[@id="cookiesPerSecond"]')
        print('Your score -> Cookies', score_element.text)
        break
    except:
        print('Error')
        pass

driver.quit()