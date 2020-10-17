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

# Function to play the game
def play_game(actionList, webPage):
    for i in range(100):
        for j in actionList:
            print(j)
            webPage.send_keys(j)
    return "Finished"

# Create a list of actions
actions = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]
            
# Play!)
page = browser.find_element_by_tag_name('html')
play_game(actions, page)

# Get the score
score = browser.find_element_by_class_name('score-container').text
print('Your score: ', score)

# Write the score in a .txt file

# Get the average score and print to the screen

# Click to restart the game
playAgain = input('Would you like to try another shot? (Y/N)')
while True:
    print("Okay, let's do it!")
    
    tryAgain = browser.find_element_by_xpath('//a[text()="Try again"]')
    tryAgain.click()
    play_game(actions, page)

    score = browser.find_element_by_class_name('score-container').text
    print('Your score: ', score)
    playAgain = input('Would you like to try another shot? (Y/N)')
    if playAgain.lower() != 'y':
        break

print('Hope to see you soon!')