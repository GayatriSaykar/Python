"""def greet():
    print("Hello, world!")

greet()   # Output: Hello, world!"""


"""def greet(name):
    print(f"Hello, {name}!")

greet("Alex")     # Output: Hello, Alex!
greet("Sam")      # Output: Hello, Sam!"""

"""def greet(name, greeting):
    print(f"{greeting}, {name}!")

greet("Alex", "Hi")   # Output: Hi, Alex!"""

"""def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alex")             # Output: Hello, Alex!
greet("Alex", "Welcome")  # Output: Welcome, Alex!"""


"""def add(a, b):
    return a + b

result = add(3, 4)
print(result)   # Output: 7"""

"""def add(a, b):
    return a + b
print(add(10, 5) * 2)   # Output: 30"""

#coordinates example
"""def get_coordinates():
    return 10.0, 20.0

x, y = get_coordinates()
print(f"x: {x}, y: {y}")   # Output: x: 10.0, y: 20.0"""

"""def greet(name):
    print(f"Hello, {name}!")

result = greet("Alex")
print(result)   # Output: None"""


#The global keyword (use sparingly)
#If you truly need to change a global variable from inside a function, you can declare it with the global keyword:

"""count = 0

def increment():
    global count
    count = count + 1

increment()
print(count)   # Output: 1"""


def increment(count):
    return count + 1

count = 0
count = increment(count)
print(count)   # Output: 1