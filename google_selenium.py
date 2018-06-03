from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")
driver.get("https://www.google.com/")
ele = driver.find_element_by_name("q")
ele.send_keys("Automation with python")
ele.send_keys(Keys.RETURN)
driver.close()