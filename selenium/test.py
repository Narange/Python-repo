from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import wait

driver = webdriver.Chrome()
driver.get("https://www.duckduckgo.com")

elem = webdriver
elem = driver.find_element_by_id("search_form_homepage")
elem.send_keys("wikipedia")

elem = driver.find_element_by_id("search_button_homepage")
elem.click()

