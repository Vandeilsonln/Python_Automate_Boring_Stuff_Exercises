from selenium import webdriver
import time


PATH = r"C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)

browser.get('https://cursos.alura.com.br//loginForm')
browser.implicitly_wait(5)
searchElem = browser.find_element_by_id('login-email')
searchElem.send_keys('vandernobrel@gmail.com')

passElem = browser.find_element_by_id('password')
passElem.send_keys('nopasswordhere')
passElem.submit()

# nextElem = browser.find_element_by_class_name('btn-login')
# nextElem.click()


time.sleep(3)
browser.close()