from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

url = 'https://www.python.org/'
driver.get(url)

time_elements = driver.find_elements(By.CSS_SELECTOR, value='div.event-widget.last ul li time')
all_events = driver.find_elements(By.CSS_SELECTOR, value='div.event-widget.last ul li a')

print(time_elements)
print(all_events)

event_dict = {}
for i in range(len(time_elements)):
    event_dict[i] = {
        'time':time_elements[i].text, 
        'name': all_events[i].text
        }

print(event_dict)

# {0: {'time': '2024-07-07', 'name': 'Django - The Powerhouse'}, 1: {'time': '2024-07-08', 'name': 'SciPy US 2024'}, 2: {'time': '2024-07-08', 'name': 'EuroPython 2024'}, 3: {'time': '2024-07-08', 'name': 'Django - The Powerhouse'}, 4: {'time': '2024-07-10', 'name': 'PyCon Nigeria 2024'}}

driver.quit()