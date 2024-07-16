from selenium import webdriver

import time

from selenium.webdriver.common.by import By

import json

import jsonlines

def get_service_category(service_category):
    service_list = []
    for el in service_category:
        if 'spr_offer1' in el.get_attribute('class') and 'Offer1' not in service_list:
            service_list.append('Offer1')
        elif 'spr_offer4' in el.get_attribute('class') and 'Offer4' not in service_list:
            service_list.append('Offer4')
        elif 'spr_offer10' in el.get_attribute('class') and 'Offer10' not in service_list:
            service_list.append('Offer10')

    return service_list



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

url = 'https://www.kia.com/th/en/shopping-tools/find-a-dealer.html'

driver.get(url)

time.sleep(3)
consent_btn=driver.find_element(By.XPATH, value='//*[@id="cookie_notice"]/div/a')
consent_btn.click()

time.sleep(3)
page_buttons = driver.find_elements(By.XPATH, value='//div[@class="location_listview"]//a[@class="pg_num"]')
page_no = 2

while True:
    time.sleep(5)
    
    all_trs = driver.find_elements(By.XPATH, value='//tbody/tr[@class="ng-scope"]')
    for tr in all_trs:
        name = tr.find_element(By.XPATH, value='.//th[@class="ng-binding"]').text or ''
        address = tr.find_element(By.XPATH, value='.//div[@class="ng-binding"]').text.split('- Phone :') or ''
        phone = address[1].strip().split('- Facebook : ')[0]
        hours = tr.find_element(By.XPATH, value='.//td[@class="tleft ng-binding"]').text or ''
        hours_list = hours.split('\n')
        hours_dict = {hours_list[0]: hours_list[2], hours_list[4]:hours_list[6]}
        service_category = driver.find_elements(By.CSS_SELECTOR, value='.offerList span')

        data = {
            'name': name,
            'address':address[0],
            'phone': phone,
            'hours': hours_dict,
            'service_category': get_service_category(service_category)
        }
        with open('kia_dealer_data.jsonl', mode='a') as file:
            json.dump(data, file)
            file.write('\n')
    
    time.sleep(3)
    for btn in page_buttons:
        if 'pg_num_on' not in btn.get_attribute('class') and btn.text == str(page_no):
            page_no+=1
            time.sleep(3)
            btn.click()
            break
        
        elif page_no == 4:
            page_no+=1

        
    print(page_no)
        
    if page_no > 4:
        break
   

time.sleep(2)
driver.quit()
