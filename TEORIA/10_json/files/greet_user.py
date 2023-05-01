import json

filename = "./files/user_name.json"
with open(filename) as f:
    user_name = json.load(f)

print(f"Hello {user_name}! Have a nice day!")
# Hello Naia! Have a nice day!