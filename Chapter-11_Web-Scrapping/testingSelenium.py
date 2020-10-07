#! python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = r"C:\Program Files (x86)\chromedriver.exe"

browser = webdriver.Chrome(PATH)

browser.get('https://techwithtim.net')
print(browser.title)
mySearch = browser.find_element_by_name('s')
mySearch.send_keys('test')
mySearch.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'main')))
    articles = main.find_elements_by_tag_name('article')
    for i in articles:
        #header = i.find_elements_by_class_name('entry-summary')
        print(i.text)

except:
    browser.close()
    
time.sleep(5)
browser.close()
# browser.quit()  - Close the entire browser