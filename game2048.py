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
actions = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]

# Play! (a specific number of times)
page = browser.find_element_by_tag_name('html')

for i in range(100):
    for j in actions:
        print(j)
        page.send_keys(j)
        # sleep(1)

# Get the score
score = browser.find_element_by_class_name('score-container').text
print(score)

# Click on 'Try Again'
sleep(3)
print('Time to try again!')
tryAgain = browser.find_element_by_xpath('//a[text()="Try again"]')
tryAgain.click()
# Write the score in a .txt file

# Get the average score and print to the screen

# Click to restart the game