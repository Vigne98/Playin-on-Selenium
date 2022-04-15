from selenium import webdriver
import unittest
import time

tc = unittest.TestCase('__init__')
#load chrome driver to PATH
driver = webdriver.Chrome(executable_path=r"C:\Selenium Drivers\chromedriver.exe")
driver.get("http://automationpractice.com/index.php")
driver.find_element_by_id("search_query_top").send_keys("buscar")
driver.find_element_by_name("submit_search").click()
#bad practise but effective this time, timout of the whole file
time.sleep(5)
#Checking if the text inside xpath is the same as the expected one
tc.assertEqual('No results were found for your search "buscar"', driver.find_element_by_xpath('//*[@id="center_column"]/p').text)
#if true it will continue with the code (close browser)
driver.close()
