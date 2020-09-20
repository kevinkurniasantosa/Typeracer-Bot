import time
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

print('import success')

url = 'https://play.typeracer.com/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximixed')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.set_capability("acceptInsecureCerts", True)

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)
driver.maximize_window()

try:
    time.sleep(2)
    driver.find_element_by_xpath("//button[@class='qc-cmp-button qc-cmp-secondary-button']").click()
except:
    pass

# Typing Race
def typing_race():
    time.sleep(3)
    typing_race_button = driver.find_element_by_xpath("//table[@class='mainMenuItemText']//a[@class='gwt-Anchor']")
    typing_race_button.click()

    while True:
        # time.sleep(2)
        # practice_text = driver.find_element_by_xpath("//table[@class='inputPanel']//tbody//tr").text.strip()
        # print('Text: ' + practice_text)

        input('Press any key to read text..')
        practice_text = driver.find_element_by_xpath("//table[@class='inputPanel']//tbody//tr").text.strip()
        print('Text: ' + practice_text) 

        input('Press any key to continue..')
        # time.sleep(10) # Wait until start 
        
        print('Typing..')
        input_box = driver.find_element_by_xpath("//input[@class='txtInput']")
        input_box.send_keys(practice_text)

        time.sleep(3)

# Practice
def practice_race():
    time.sleep(3)
    practice_race_button = driver.find_element_by_xpath("//table[@class='mainMenuItem']//a[@class='gwt-Anchor']")
    practice_race_button.click()

    # time.sleep(2)

    input('Press any key to read the entire text')

    practice_text = driver.find_element_by_xpath("//table[@class='inputPanel']//tbody//tr").text.strip()
    print('Text: ' + practice_text)
    input('Press any key to continue..')
    # time.sleep(3) # Wait until start 
    
    input('Press any key to start typing..')
    print('Typing..')
    input_box = driver.find_element_by_xpath("//input[@class='txtInput']")
    input_box.click()
    input_box.send_keys(practice_text)

# Race with your friends
def race_your_friends():
    time.sleep(3)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.ALT + 'p')

    input('Press any key to read the text..')
    practice_text = driver.find_element_by_xpath("//table[@class='inputPanel']//tbody//tr").text.strip()
    print('Text: ' + practice_text)
    
    input('Press any key to start typing..')
    print('Typing..')
    input_box = driver.find_element_by_xpath("//input[@class='txtInput']")
    input_box.send_keys(practice_text)

if __name__ == '__main__':
    input_option = input('''Choose options:\n1. Typing race\n2. Practice\n3. Race with friends \n''')

    if int(input_option) == 1:
        typing_race()
    elif int(input_option) == 2:
        practice_race()
    elif int(input_option) == 3:
        race_your_friends()
    else:
        print('Wrong input..')