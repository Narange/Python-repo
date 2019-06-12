import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Taxi_Driver")
# Always check response status
res.raise_for_status()
print(f"Status code: {res.status_code}")

# Put the HTML in a BeautifulSoup object
soup = bs4.BeautifulSoup(res.text, features="lxml")
print(type(soup))

# Get all elements in the document
list_of_elems = soup.select("*")


# Write the text from each element to a txt file
def all_elems_to_txt():
    with open("output_all_elements.txt", "w") as output_file:

        for i in list_of_elems:
            try:
                elem_to_write = i.getText()
                output_file.write(elem_to_write)
            except UnicodeEncodeError as e:
                print("[DEBUG] " + str(e))
                pass


all_elems_to_txt()
