from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.youtube.com/")

elem = driver.find_element_by_id("masthead-search-term")
elem.send_keys("python datastructures")
elem.send_keys(Keys.ENTER)
time.sleep(5)
driver.close()
