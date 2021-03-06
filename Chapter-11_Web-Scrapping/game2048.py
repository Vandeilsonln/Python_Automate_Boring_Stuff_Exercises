#! python3
#! game2018.py - A simple script which will play 2048 directly from the website

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


PATH = r"C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)

# Open the website
browser.get('https://play2048.co/')
page = browser.find_element_by_tag_name('html')

# Functions to play and re-play the game
def play_game(actionList, webPage):
    for _ in range(100):    # instead of a FOR, I'd like to make it run until it detects the 'game over' screen.
        for j in actionList:
            webPage.send_keys(j)

def restart_game(webPage):
    webPage.find_element_by_xpath('//a[text()="Try again"]').click()


# Create a list of actions
actions = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]

while True:
    # Play!
    play_game(actions, page)

    # Get the score
    score = browser.find_element_by_class_name('score-container').text
    print('Your score: ', score)
    
    # Write the score in a .txt file
    with open('Chapter-11_Web-Scrapping\scores_2048.txt', 'a') as scoreLog:
        scoreLog.write(score)
        scoreLog.write('\n')
    
    # Restart - or not
    playAgain = input('Would you like to try another shot? (Y/N)')
    if playAgain.lower() != 'y':
        break
    restart_game(page)

print('Hope to see you soon!')
# Get the average score and print it to the screen
with open(r'Chapter-11_Web-Scrapping\scores_2048.txt', 'r') as scoreLog:
    listOfScores = scoreLog.readlines()
    lenght = len(listOfScores)
    avg = 0
    for i in listOfScores:
        avg += int(i)
    avg = avg / lenght
    print('Average: ', avg)    
browser.quit()