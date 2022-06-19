from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
driver.get("https://www.python.org/")
time_events = driver.find_elements(By.CSS_SELECTOR, '.event-widget li time')
news_events = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

events = {}
for n in range(len(time_events)):
    events[n] = {
        "time": time_events[n].text,
        "name": news_events[n].text
        }
print(events)

driver.quit()
