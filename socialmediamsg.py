#! python 3 
# socialmediamsg.py - Access a social media and send messages to a user.

from selenium import webdriver
from time import sleep

PATH = r"C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)

# Go to the social media and log in
browser.get('https://www.facebook.com')

email = browser.find_element_by_id('email')
password = browser.find_element_by_id('pass')
enter = browser.find_element_by_id('u_0_b')

email.send_keys('email')
password.send_keys('pass')
enter.click()
sleep(5)
# Access the message's screen
messageScreen = browser.find_element_by_css_selector('[aria-label=Messenger]')
messageScreen.click()
sleep(5)
goToMessenger = browser.find_element_by_xpath('//a[text()="Ver tudo no Messenger"]')
goToMessenger.click()
# Send a message to a user
