#! python3
# imagedownloader.py - Goes to imgur.com website, search  for a few pictures and download them.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import urllib.request

PATH = r"C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)

# Get to the website
browser.get('https://imgur.com/')

# TODO: Agree with the cookies
sleep(1)
browser.find_element_by_xpath('//button[text()="AGREE"]').click()

# Search something
seachBar = browser.find_element_by_class_name('Searchbar-textInput')
seachBar.send_keys('kitten')
seachBar.submit()

# identify the images
picturesList = browser.find_elements_by_tag_name('img')

# download them
a = 1
for image in picturesList[0:20]:
    url = image.get_attribute('src')
    print(url)
    urllib.request.urlretrieve(url, 'my-test' + str(a) + '.jpg')
    print('Done', a)
    a +=1