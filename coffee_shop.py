print("Welcome to the Coffee Shop!")
print("What would you like to order?")

total_bill = 0.0
order = []


coffee_shop={"coffee":100,"tea":50,"bread":20}

while True:
    cust_choice=input("Please confirm your order or type 'done' to finish: ").lower()
    if cust_choice=="done":
        break
    if cust_choice in coffee_shop:
        order.append(cust_choice)
        print(f"Added {cust_choice} to your order.")
    else:
        print("Sorry, we don't have that item. Please choose from the menu.")


print("\nThank you for your order! Here is your receipt:")
print("Have a great day!")


for item in order:
    price = coffee_shop[item]
    print(f"Item: {item.capitalize()} - ${price:.2f}")
    total_bill += price

print("---------------")

 # Display the final calculated total
print(f"Total Bill: ${total_bill:.2f}")




    

