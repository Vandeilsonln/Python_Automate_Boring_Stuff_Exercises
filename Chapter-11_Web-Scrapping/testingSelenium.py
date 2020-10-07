#! python3

from selenium import webdriver
PATH = r"C:\Program Files (x86)\chromedriver.exe"

browser = webdriver.Chrome(PATH)

browser.get('https://techwithtim.net')
print(browser.title)
browser.close()
# browser.quit()  - Close the entire browser