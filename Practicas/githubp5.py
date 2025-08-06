from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.Wikipedia.org")

web_element = driver.find_element(By.NAME,'search')
web_element.send_keys("Pinochet"+Keys.ENTER)

time.sleep(30)