from selenium import webdriver
import time 
import random
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome()
url = "https://www.myfitnesspal.com/"
user_email = 'user@email.com'
user_pass = 'password'


class MyFitnessPal:

	def __init__(self, driver,url,email,password):
		self.driver = driver
		self.url = url
		self.email = email
		self.password = password

	def navigate(self,url):
		self.driver.get(self.url)

	def login(self,email,password,driver):
		try:
			login = self.driver.find_element_by_class_name('fancylink')
			login.send_keys(Keys.RETURN)
			usernameElement = self.driver.find_element_by_name('username')
			usernameElement.send_keys(self.email)
			passwordelement = self.driver.find_element_by_name('password')
			passwordelement.send_keys(self.password)

			#loggin in to the myfitnesspal using Selenium
			usernameElement.send_keys(Keys.RETURN)

		except Exception as inst:
			print type(inst)     # the exception instance
			print inst.args      # arguments stored in .args
			print inst

	def navigateToAddFood(self,driver):
		statuselement = self.driver.find_element_by_xpath("//*[@class='add-buttons']//a[contains(@href, '/food/diary')]")
		statuselement.send_keys(Keys.RETURN)

	def selectQuickTool(self,driver,msg):
		blahCrap = self.driver.find_element_by_xpath(msg)
		blahCrap.send_keys(Keys.RETURN)

	def copyMealFromYesterday(self,driver,msg):
		mealFromYes = self.driver.find_element_by_xpath(msg)
		mealFromYes.send_keys(Keys.RETURN)

	def browserClose(self,driver):
		self.driver.close()

	def saveEntries(self,driver):
		saveEntries = self.driver.find_element_by_xpath("//*[@id='complete_day']/span/a[contains(@class, 'button complete-this-day-button')]")
		saveEntries.send_keys(Keys.RETURN)

	def waterIntake(self,driver):
		waterIntake = self.driver.find_element_by_xpath("//*[@id='water_cups']/p/a[contains(@class, 'up')]")
		waterIntake.send_keys(Keys.RETURN)

#Navigating to the url
myfitnesspal = MyFitnessPal(driver,url,user_email,user_pass)
myfitnesspal.navigate(url)

# Logging in facebook by using email and password
myfitnesspal.login(user_email,user_pass,driver)

time.sleep(5)

#Selecting Add food option
myfitnesspal.navigateToAddFood(driver)

#Select Quick tool 
myfitnesspal.selectQuickTool(driver, "//*[@id='main']//div/table/tbody/tr/td/div/a[contains(@href, '#quick_tools_0')]")

#Select copy meal from yesterday
myfitnesspal.copyMealFromYesterday(driver, "//*[@id='quick_tools_0']//ul/li/a[contains(@href, '/food/copy_meal')]")

#Entry for water intake
myfitnesspal.waterIntake(driver)

#Save the entries
myfitnesspal.saveEntries(driver)

# Closing the current Browser
myfitnesspal.browserClose(driver)
