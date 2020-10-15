from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


PATH = r"C:\Program Files (x86)\chromedriver.exe"

browser = webdriver.Chrome(PATH)

browser.get('https://techwithtim.net/')
sleep(1)

initial = browser.find_element_by_link_text('Python Programming')
initial.click()
sleep(1)

course = browser.find_element_by_link_text('Beginner Python Tutorials')
course.click()

sleep(1)
browser.back()
