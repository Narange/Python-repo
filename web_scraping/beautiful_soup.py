import requests
import bs4
import re

res = requests.get("https://en.wikipedia.org/wiki/Taxi_Driver")
# Check response status
res.raise_for_status()
print(f"Status code: {res.status_code}")

# Put the HTML in a BeautifulSoup object
soup = bs4.BeautifulSoup(res.text, features="lxml")
print(type(soup))

# Get all <p> elements in the document
list_of_p = soup.select("p")


# Write the text from each element to a txt file
def all_p_to_txt():
    with open("output_all_p.txt", "w") as output_file:

        # regex pattern: any brackets containing only digits (Wiki references)
        pattern = re.compile(r"\[\d*\]")

        for i in list_of_p:
            try:
                elem_to_write = i.getText()
                elem_to_write = re.sub(pattern, "", elem_to_write)
                output_file.write(elem_to_write)
            except UnicodeEncodeError as e:
                print("[DEBUG] " + str(e))


all_p_to_txt()
