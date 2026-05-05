import requests

url = input("Enter image URL: ")
img = requests.get(url).content

with open("image.jpg", "wb") as f:
    f.write(img)

print("Downloaded")