#! python 3 
# socialmediamsg.py - Access a social media and send messages to a user.

from selenium import webdriver
from time import sleep

PATH = r"C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)

# Go to the social media and log in
browser.get('https://pt-br.facebook.com/')

email = browser.find_element_by_id('email')
password = browser.find_element_by_id('pass')
enter = browser.find_element_by_id('u_0_b')

email.send_keys('your_email')
password.send_keys('your_password')
enter.click()
sleep(10)
# Access the message's screen
messageScreen = browser.find_elements_by_css_selector('[aria-label=Messenger]')
messageScreen[0].click()

# Send a message to a user