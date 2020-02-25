import requests

url = "https://jsonplaceholder.typicode.com/photos"
get_response = requests.get(url)

# write the response to a new JSON file in this directory
with open("get_results.json", "w") as wf:
    wf.write(get_response.text)

# do the same as above, but get just one record with id 300
url_300 = "https://jsonplaceholder.typicode.com/photos/300"
get_response_300 = requests.get(url_300)

# write the response to a new JSON file in this directory
with open("get_results_just_one.json", "w") as wf:
    wf.write(get_response_300.text)

jsonPayload = {
    "albumId": 1,
    "title": "test",
    "url": "nothing.com",
    "thumbnailUrl": "nothing.com",
    }

# post the new JSON object to the 
post_response = requests.post(url, json=jsonPayload)

# write the response to a new JSON file in this directory
with open("post_results.json", "w") as wf:
    wf.write(post_response.text)

# to change one particular record, use the id 300 one from before
put_response = requests.put(url_300, json=jsonPayload)

# write the response to a new JSON file in this directory
with open("put_results.json", "w") as wf:
    wf.write(put_response.text)

delete_response = requests.delete(url_300)

# write the response to a new JSON file in this directory
with open("delete_results.json", "w") as wf:
    wf.write(delete_response.text)

# use the get_response's JSON to make a python dict
my_json = get_response_300.json()
# print out the 
print(my_json["id"])