import requests

api_key = "gjAbZNghx3R5ZLGPNwqlbC0W3rS7SvKR6vMuXytJ"

date = input("Whats the date you want to check out?: ")

response = requests.get("https://api.nasa.gov/planetary/apod", params={"api_key": api_key, "date": date})

data = response.json()

url = requests.get(data["hdurl"])
print(url.headers["content-type"])


extension = url.headers["content-type"].split("/")[1]
name = input("What do you want to name the photo?: ")
place = input("Where do you want to save it?: ")

with open(place + "/" + name + "." + extension, "wb") as file:
    file.write(url.content)
