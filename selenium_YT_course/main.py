import os
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.amazon.com/s?k=vase")

elem_list = driver.find_element(By.CSS_SELECTOR, "div.s-main-slot.s-result-list.s-search-results.sg-row")
items = elem_list.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

for item in items:
    title = item.find_element(By.TAG_NAME, "h2").text
    price = "No price found"

    try:
        price = item.find_element(By.CSS_SELECTOR, ".a-price").text.replace("\n", ".")
    except:
        pass

    print("Title: " + title)
    print("Price: " + price)