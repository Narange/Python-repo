import requests

url = "https://jsonplaceholder.typicode.com/photos"
response = requests.get(url)

# list of JSON objects
request_list = response.json()

# set of URLs
# elems in a set must be unique, so a set can be searched in constant time
url_dict = {}

for elem in request_list:
    
    current_id = elem["id"]
    current_url = elem["url"]

    if current_url in url_dict:
        print(f"Element with id {current_id} is a duplicate of URL: {current_url} which initially was seen at id {url_dict[current_url]}")
    else:
        url_dict[current_url] = current_id
