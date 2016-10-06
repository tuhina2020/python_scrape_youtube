from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import csv

# from commandline go to the folder with this python file
# run python youtube_data.py
# the data will be displayed in the window


# the parameter movie should be present(exactly) in the yoube video name
def get_youtube_data(movie):
	driver = webdriver.Chrome()
	driver.get('https://www.youtube.com/')	
	searchBoxID = "masthead-search-term"
	buttonID = "search-btn"
	buttonXpath = "//form/button[@id='search-btn']"
	LinkXpath = "//a[contains(@title, '%s')]" % movie
	subscriptionXpath = "//div[@id='watch7-views-info']/div[@class='watch-view-count']"

	searchBoxElement = WebDriverWait(driver, 10).until( lambda driver : driver.find_element_by_id(searchBoxID))
	searchButton = WebDriverWait(driver, 10).until( lambda driver : driver.find_element_by_xpath(buttonXpath))

	searchBoxElement.clear()
	searchBoxElement.send_keys(movie)
	searchButton.click()
	l = WebDriverWait(driver, 10).until( lambda driver : driver.find_elements_by_xpath(LinkXpath))
	movieLink = WebDriverWait(driver, 10).until( lambda driver : l[0])
	movieLink.click()

	subscriptions = WebDriverWait(driver, 30).until( lambda driver : driver.find_element_by_xpath(subscriptionXpath))
	print str(movie)+ " "+ str(subscriptions.get_attribute('innerHTML').encode('utf-8') )


# replace the parameters passsed with movie name
get_youtube_data('The Legend of Tarzan')
