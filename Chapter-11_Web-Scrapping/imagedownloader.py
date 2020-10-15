#! python3
# imagedownloader.py - Goes to imgur.com website, search  for a few pictures and download them.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import urllib3

PATH = r"C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)

# Get to the website
browser.get('https://imgur.com/')

# TODO: Agree with the cookies
# sleep(3)
# browser.find_element_by_xpath().click()

# Search something
seachBar = browser.find_element_by_class_name('Searchbar-textInput')
seachBar.send_keys('Ireland')
seachBar.submit()

# identify the images
picturesList = browser.find_element_by_class_name('image-list-link').get_attribute('href')

# download them
urllib3.request.urlencode(picturesList, 'my-test.jpg')