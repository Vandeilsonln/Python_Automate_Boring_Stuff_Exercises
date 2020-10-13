from selenium import webdriver
import time


PATH = r"C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)

print(type(browser))

browser.get('https://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('col-sm-12')
    print('Found %s element with that class name!' % (elem.tag_name))
except:
    print('It was not able to find an element with that name.')

linkElem = browser.find_element_by_link_text("See what's new in the second edition.")

print(type(linkElem))
linkElem.click()    # follows the link


time.sleep(3)
browser.close()