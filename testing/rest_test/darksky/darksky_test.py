import requests

# DarkSky API key to be used
key = "ad569ffabac9984810d3c89bdfd8375d"

# GET response and print ok code in console
url = f"https://api.darksky.net/forecast/{key}/37.8267,-122.4233"
response = requests.get(url)
print(response.ok)

# Write the response to a JSON file
with open("darksky_response.json", "w") as wf:
    wf.write(response.text)

# Create a Python dict out of the response's JSON
responseJSON = response.json()

# Get the just the set of "hourly" infomation. The API provides this hour + the next 48
response_hourly = responseJSON["hourly"]["data"]
response_len = len(response_hourly)

# Get the average temperature over this time span
sum_temp = 0
for hour in response_hourly:
    sum_temp += hour["temperature"]

average_temp = sum_temp / response_len

# Print results
print(f"Number of hours: {response_len}")
print(f"Average temp is: {average_temp}")
