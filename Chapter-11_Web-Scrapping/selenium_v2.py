from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


PATH = r"C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)

browser.get('https://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
time.sleep(1)
htmlElem.send_keys(Keys.END)    # scrolls to bottom
time.sleep(1)
htmlElem.send_keys(Keys.HOME)   # scrolls to top

time.sleep(3)
browser.close()