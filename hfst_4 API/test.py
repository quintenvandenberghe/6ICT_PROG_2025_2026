import requests

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url).json()

print(response) # <Response [200]>

with open("joke.txt", "w") as file:
    file.write(response["value"])
