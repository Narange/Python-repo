import requests

r = requests.get("https://imgs.xkcd.com/comics/python.png")

print(r.status_code)

# Download the file to current dir
with open("comic.png", "wb") as f:
    f.write(r.content)
