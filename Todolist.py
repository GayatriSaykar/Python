 # Create a loop that displays a menu and responds to user input
while True:
     # Display the menu
    print("\n=== Personal To-Do List ===")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Exit")
    print("4. Clear contents from the file.")
        
     # Get the user's choice
    choice = input("Choose an option (1-3): ")
        
    if choice == "1":
        print("\n--- Current Tasks ---")

         # Open the file in Read mode and read the tasks into a list
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
                
         # Display the tasks
        for task in tasks:
            print("- " + task.strip())

                
    elif choice == "2":
        new_task = input("\nWhat do you need to do? ")

         # Open the file in Append mode to add to the end of the list
        with open("tasks.txt", "a") as file:
            file.write(new_task + "\n")
                
        print("Task saved!")
            
    elif choice == "3":
         # Exit the program
        print("\nGoodbye! Stay productive.")
        break 
    
    elif choice == "4":
        # Open in write mode to clear the file
        with open("tasks.txt", "w") as file:
            pass

        print("All tasks have been cleared!")


            
    else:
         # Handle invalid input
        print("\nInvalid choice. Please choose 1, 2, or 3.")


       