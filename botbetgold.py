from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import sys
import random
import eel
from selenium.webdriver.common.by import By


select = "prev"


@eel.expose
def cek_select(info):
	global select
	if(info == "1"):
		select = "prev"
	else:
		select = "live"
	print("local",select)

@eel.expose
def betgold_auth(url):
	global options, driver, active
	active = True;
	options = webdriver.FirefoxOptions()
	options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0")
	options.set_preference("dom.webdriver.enabled", False)
	driver = webdriver.Firefox(executable_path = 'geckodriver.exe' , options = options)
	driver.get(url = url)	 

@eel.expose
def off_bot(exit_1):
	if (exit_1 == "1"):
		driver.quit();
		driver.close();
		print("stins")


def class_exists(class_name,element):
	try:
		element.find_element_by_class_name(class_name)
		exist = True
		
	except NoSuchElementException:
		exist = False
	return exist



def xpath_exists(xpath):
	try:
		driver.find_element_by_xpath(xpath)
		exist = True

	except NoSuchElementException:
		exist = False
	return exist


def click(selector,elements):
	try:
		b = random.randint(2, 5)
		for i in range(b):
			a = random.randint(0, len(elements)-1)
			if (selector == "live"):
				if(not(class_exists("disabled",elements[a]))):
					elements[a].location_once_scrolled_into_view
					time.sleep(1)
					elements[a].location_once_scrolled_into_view
					elements[a].click()
					time.sleep(1)
			else:
				elements[a].location_once_scrolled_into_view
				time.sleep(1)
				elements[a].location_once_scrolled_into_view
				elements[a].click()
				time.sleep(1)
		exist = True
	except:
		exist = False
	return exist



def click_accept(selector):
	try:
		driver.find_element_by_class_name('play_ticket').location_once_scrolled_into_view
		time.sleep(2)
		driver.find_element_by_class_name('play_ticket').location_once_scrolled_into_view
		driver.find_element_by_class_name('play_ticket').click()
		time.sleep(1)
		driver.find_element_by_class_name('confirm_ticket').location_once_scrolled_into_view
		time.sleep(1)
		driver.find_element_by_class_name('confirm_ticket').location_once_scrolled_into_view
		driver.find_element_by_class_name('confirm_ticket').click()
		if (selector == "live"):
			time.speep(5)
			if(xpath_exists("//strong[@data-v-32273d4a='']")):
				driver.find_element_by_class_name('remove_ticket').location_once_scrolled_into_view
				driver.find_element_by_class_name('remove_ticket').click()
				time.sleep(1)
				driver.find_element_by_class_name('clear_ticket').click()
			time.speep(5)
		else:
			time.sleep(3)
			if(xpath_exists("//strong[@data-v-32273d4a='']")):
				driver.find_element_by_class_name('remove_ticket').location_once_scrolled_into_view
				driver.find_element_by_class_name('remove_ticket').click()
				time.sleep(1)
				driver.find_element_by_class_name('clear_ticket').click()
			time.speep(1)
		if(xpath_exists("//button[@data-v-1fd3ad26='']")):
			driver.find_element_by_xpath("//button[@data-v-1fd3ad26='']").click()
		time.sleep(2)
		exist = True
	except:
		exist = False
	print("global",select)
	return exist




@eel.expose
def click_tiket():
	if(xpath_exists("//button[@data-v-1fd3ad26='']")):
		driver.find_element_by_xpath("//button[@data-v-1fd3ad26='']").click()
	elements = driver.find_elements_by_class_name('real-bet');
	if (click(select, elements)):
		if(click_accept(select)):
			pass
		else:
			pass
	else:
		pass




eel.init("")
eel.start("bot.html",size = (480, 640))	



	

		