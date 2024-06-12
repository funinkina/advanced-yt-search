from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
search_term = 'python'
over_20_filter = '&sp=EgQQARgC'
under_20_filter = '&sp=EgQQARgD'
driver.get("https://www.youtube.com/results?search_query=" + search_term.replace(' ', '+') + over_20_filter)
search_results = driver.find_elements(By.TAG_NAME, 'ytd-video-renderer')
for result in search_results:
    title_element = result.find_element(By.ID, 'video-title')
    print(title_element.text)
    print(title_element.get_attribute('href'))
    channel_name = result.find_element(By.TAG_NAME, 'yt-formatted-string')
    print(channel_name.text)

time.sleep(20)
driver.quit()
