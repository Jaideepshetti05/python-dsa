import requests

ip = requests.get("https://api64.ipify.org").text
print("Your IP:", ip)