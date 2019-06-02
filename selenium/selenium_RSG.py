"""
Go to a Wikipedia article, get all <p> text,
and feed it to the RSG (Random Sentence Generator) in this dir
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)


# Open Wikipedia article for the given query
def go_to_article(article):
    driver.get("https://en.wikipedia.org")
    elem = driver.find_element_by_id("searchInput")
    elem.send_keys(article)
    elem = driver.find_element_by_id("searchButton")
    elem.click()


# Return the text from all <p> elems on page as one string
def get_all_p_text():
    all_p_elems = driver.find_elements_by_tag_name("p")

    all_text = ""
    for p in all_p_elems:
        all_text += p.text

    return all_text


# Open RSG.html and use the plot text to generate random sentences
def do_RSG():
    # Open Wiki article and get all <p> text
    go_to_article("The Giver")
    wiki_p_text = get_all_p_text()

    # Open a new tab and switch focus to it
    driver.execute_script("window.open("")")
    driver.switch_to.window(driver.window_handles[1])

    # Open the random sentence generator. Using absolute path here.
    driver.get("C:\\Users\\Max\\Desktop\\Python-repo\\selenium\\RSG.html")

    # Paste text into the textarea
    elem = driver.find_element_by_id("inputTextField")
    elem.clear()
    elem.send_keys(wiki_p_text)

    elem = driver.find_element_by_id("buttonGenerate")
    elem.click()


do_RSG()
