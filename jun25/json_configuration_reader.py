import json

config = {
    "application": "Inventory System",
    "version": "1.0",
    "theme": "Dark",
    "language": "English"
}

with open("config.json", "w") as file:
    json.dump(config, file, indent=4)

print("Configuration Saved.\n")

with open("config.json", "r") as file:
    settings = json.load(file)

print("Application Settings")
print("-" * 30)

for key, value in settings.items():
    print(f"{key} : {value}")