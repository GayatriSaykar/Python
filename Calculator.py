
menu_options = ["add", "subtract", "multiply", "divide", "quit"]

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

# Run the main program loop
while True:
    print("\nWhat would you like to do?")
    for option in menu_options:
        print(f"  - {option}")

    choice = input("\nEnter an operation: ").lower()

    if choice not in menu_options:
        print("That's not a valid option. Try again.")
        continue

    if choice == "quit":
        print("Goodbye!")
        break

    a = float(input("First number:  "))
    b = float(input("Second number: "))

    # Perform the calculation
    if choice == "add":
        result = add(a, b)
    elif choice == "subtract":
        result = subtract(a, b)
    elif choice == "multiply":
        result = multiply(a, b)
    elif choice == "divide":
        result = divide(a, b)

    if result is None:
        print("Can't divide by zero.")
    else:
        print(f"Result: {result}")

