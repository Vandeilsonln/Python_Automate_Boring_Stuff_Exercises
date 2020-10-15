#! python3
#! game2018.py - A simple script which will play 2048 directly from the website

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


PATH = r"C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)

# Open the website
browser.get('https://play2048.co/')

# Create a list of actions

# Play! (a specific number of times)

# Get the score

# Write the score in a .txt file

# Get the average score and print to the screen

# Click to restart the game