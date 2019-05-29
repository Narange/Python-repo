from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)


# Open Wikipedia article for the given query (a movie)
# TODO: Return the text of "Plot" section using XPath
def go_to_wiki_article(query):
    driver.get("https://en.wikipedia.org")
    elem = driver.find_element_by_id("searchInput")
    elem.send_keys(query)
    elem = driver.find_element_by_id("searchButton")
    elem.click()


# TODO: open RSG.html and use the plot text to generate random sentences
def do_RSG():
    pass


# so far, just goes to the Wiki article for the query
go_to_wiki_article("Taxi Driver")
