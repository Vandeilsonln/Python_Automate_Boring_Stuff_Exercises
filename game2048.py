#! python3
#! game2018.py - A simple script which will play 2048 directly from the website

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint

PATH = r"C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)

# Open the website
browser.get('https://play2048.co/')

# Create a list of actions
actions = ['Keys.UP', 'Keys.RIGHT', 'Keys.DOWN', 'Keys.LEFT']

# Play! (a specific number of times)
page = browser.find_element_by_tag_name('html')
for i in range(250):
    a = randint(0, len(actions)-1)
    print(a)
    page.send_keys(actions[a])


# Get the score

# Write the score in a .txt file

# Get the average score and print to the screen

# Click to restart the game