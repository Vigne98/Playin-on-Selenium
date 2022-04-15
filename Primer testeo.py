from selenium import webdriver
import unittest
import time

tc = unittest.TestCase('__init__')

driver = webdriver.Chrome(executable_path=r"C:\Selenium Drivers\chromedriver.exe")
driver.get("http://automationpractice.com/index.php")
driver.find_element_by_id("search_query_top").send_keys("buscar")
driver.find_element_by_name("submit_search").click()
time.sleep(5)
tc.assertEqual('No results were found for your search "buscar"', driver.find_element_by_xpath('//*[@id="center_column"]/p').text)
driver.close()
