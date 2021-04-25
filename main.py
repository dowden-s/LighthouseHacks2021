from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
from time import sleep    
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


import time

speechDocList = []

numberOfSearches = 0

f = open("oppSpeechDoc.txt", "r")
for x in f:
    numberOfSearches += 1
    str = x
    if (str.find("\n") != -1):
        size = len(str)
        mod_string = str[:size - 1]
        str = mod_string
    speechDocList.append(str)

#xpaths
searchbuttonxpath = '//*[@id="globalsearch"]/button'
searchbarxpath = '//*[@id="headerglobalsearchinput"]'

PATH = "C:\Program Files (x86)\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(PATH, desired_capabilities=chrome_options.to_capabilities())


#ldcasewiki

i = 0
while i<numberOfSearches:
    driver.get("https://hsld.debatecoaches.org/Main/")

    driver.find_element_by_xpath(searchbuttonxpath).click()
    search = driver.find_element_by_xpath(searchbarxpath)
    search.send_keys(speechDocList[i])
    i += 1
    search.send_keys(Keys.RETURN)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[i])
    

time.sleep(1000)
