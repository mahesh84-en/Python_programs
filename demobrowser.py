import time

from selenium import webdriver

#we directly not with the chrome browser. firstly, we will interact with chrome service then chrome service will interact with the chrome.
#we have to make sure that iur chrome version and chrome service version should be same

driver = webdriver.Chrome(executable_path="C:/Users/DELL/Downloads/chromedriver-win64/chromedriver.exe")
driver.get("https://www.distacart.com")
time.sleep(2)