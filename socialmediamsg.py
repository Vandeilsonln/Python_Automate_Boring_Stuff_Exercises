#! python 3 
# socialmediamsg.py - Access a social media and send messages to a user.

from selenium import webdriver
from time import sleep

PATH = r"C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)

# Go to the social media and log in
browser.get('https://pt-br.facebook.com/')

# Access the message's screen

# Send a message to a user