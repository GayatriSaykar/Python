"""with open("notes.txt","r") as file:
    contents=file.read()
    print(contents)
# File is automatically closed here"""

"""with open("notes.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())   # .strip() removes the trailing newline"""


with open("greeting.txt", "r") as file:
    for line in file:
        print(line.strip())

with open("greeting.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("Welcome to Python.\n")

with open("greeting.txt", "a") as file:
    file.write("New entry added.\n")

tasks = ["Buy groceries\n", "Walk the dog\n", "Finish homework\n"]

with open("greeting.txt", "w") as file:
    file.writelines(tasks)

