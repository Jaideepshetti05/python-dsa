wifi_name = input("Enter WiFi Name: ")
password = input("Enter Password: ")

with open("wifi.txt", "a") as file:
    file.write(f"{wifi_name} : {password}\n")

print("Saved Successfully!")