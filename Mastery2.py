# -*- coding: utf-8 -*-
#start BrowserStackLocal ./BrowserStackLocal --key MDKicy4nya2192zewKpz
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import unittest, time, re

desired_cap = {'browser': 'Chrome','browser_version': '80.0','os': 'OS X','os_version': 'High Sierra','project': 'MASTERY','browserstack.debug': 'true', 'resolution': '1600x1200'}

browser = webdriver.Remote(
    command_executor='http://scottmaretick2:MDKicy4nya2192zewKpz@hub.browserstack.com:80/wd/hub', desired_capabilities= desired_cap)

#CHROME
#browser = webdriver.Chrome("/Users/scottmaretick/Desktop/chromedriver")
browser.get("https://www.mastery.net/")

#PAGING DOWN MAIN PAGE START
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot2.png');
browser.execute_script("window.scrollTo(600,900);")
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot3.png');
browser.execute_script("window.scrollTo(900,1500);") #MASTERY TEAM
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot4.png');
browser.execute_script("window.scrollTo(1500,2400);") #WE'RE HIRING
time.sleep(10)

#BACKEND ENGINEER
browser.find_element_by_css_selector("div.careers-item:nth-child(1) > a:nth-child(1)").click()
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot5.png');
browser.execute_script("window.scrollTo(200,600);")
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot6.png');
browser.execute_script("window.scrollTo(600,900);") 
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot7.png');
browser.back() #BACK TO WE'RE HIRING

#FRONTEND ENGINEER
browser.find_element_by_css_selector("div.careers-item:nth-child(2) > a:nth-child(1)").click()
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot6.png'); 
browser.execute_script("window.scrollTo(200,600);")
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot6.png');
browser.execute_script("window.scrollTo(600,900);") 
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot7.png');
browser.back() #BACK TO WE'RE HIRING

#MOBILE ENGINEER
browser.find_element_by_css_selector("div.careers-item:nth-child(3) > a:nth-child(1)").click() 
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot8.png');
browser.execute_script("window.scrollTo(200,600);")
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot9.png');
browser.execute_script("window.scrollTo(600,900);") 
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot10.png');
browser.back() #BACK TO WE'RE HIRING

#CLIENT SERVICES
browser.find_element_by_css_selector("div.careers-item:nth-child(4) > a:nth-child(1)").click()
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot11.png'); 
browser.execute_script("window.scrollTo(200,600);")
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot12.png');
browser.back()

#QA
browser.find_element_by_css_selector("div.careers-item:nth-child(5) > a:nth-child(1)").click() 
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot13.png');
browser.execute_script("window.scrollTo(200,600);")
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot14.png');
browser.execute_script("window.scrollTo(600,900);") 
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot15.png');
browser.execute_script("window.scrollTo(900,1200);")
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot16.png');
browser.execute_script("window.scrollTo(1200,1800);")
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot17.png');
browser.back()

#DATA SCIENCES
browser.find_element_by_css_selector("div.careers-item:nth-child(6) > a:nth-child(1)").click() 
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot16.png');
browser.execute_script("window.scrollTo(200,600);")
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot17.png');
browser.back()

#PEOPLE TEAM
browser.find_element_by_css_selector("div.careers-item:nth-child(7) > a:nth-child(1)").click()
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot18.png'); 
browser.execute_script("window.scrollTo(200,600);")
browser.back()

#GENERAL INTEREST
browser.find_element_by_css_selector("div.careers-item:nth-child(8) > a:nth-child(1)").click() 
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot19.png');
browser.execute_script("window.scrollTo(200,600);")
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot20.png');
browser.back()

browser.execute_script("window.scrollTo(2400,2600);") #BOTTOM OF PAGE
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot14.png');	
#PAGING DOWN MAIN PAGE END
print browser.title

#SEE ALL OPENINGS
browser.find_element_by_css_selector("html body section#careers.careers.bg-full-black.paragraph div.container-1200 div.careers-inner div.button a").click()
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot15.png');
browser.execute_script("window.scrollTo(200,600);")
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot16.png');
browser.execute_script("window.scrollTo(600,900);")
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot17.png');
browser.execute_script("window.scrollTo(900,1200);")
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot18.png');
browser.back()

browser.execute_script("window.scrollTo(0,600);") #BACK TO TOP OF PAGE

browser.find_element_by_css_selector(".menu > a:nth-child(1)").click() #PRODUCT 
print browser.title
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot19.png');
browser.find_element_by_css_selector(".menu > a:nth-child(2)").click() #THE TEAM
print browser.title
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot20.png');
browser.find_element_by_css_selector(".menu > a:nth-child(3)").click() #CAREERS
browser.execute_script("window.scrollTo(2400,2600);") #BOTTOM OF CAREERS PAGE
time.sleep(10)
print browser.title
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot17.png');
browser.find_element_by_css_selector(".menu > a:nth-child(3)").click() #GET IN TOUCH
time.sleep(10)
print browser.title
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot18.png');
browser.quit()
