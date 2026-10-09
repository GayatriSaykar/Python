"""user = {
    "name": "Alex",
    "age": 25,
    "email": "alex@example.com"
}

print(user["name"])   # Output: Alex
print(user["age"])    # Output: 25

print(user.get("name"))"""


user = {"name": "Alex", "age": 25, "email": "alex@example.com"}

for key, value in user.items():
    print(f"{key}: {value}")

