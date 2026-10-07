"""fav_col=input("What is you fav col")
print("I love", fav_col)"""

"""age = int(input("How old are you? "))
print("Next year you will be", age + 1)"""

"""name = "Alex"
print(f"Hello, {name}!")"""


"""age = input("How old are you? ")
print(f"Next year you will be {age + 1}") # Works perfectly!""" # Need to check it

#User= input("What is your name?")
#input= "Hi" + " " + User
#print(input)
#print(f"Welcome, {User}")

#print("-"* 20)
#n=int(input("enter number"))
#print("# " * n)

"""name=input("Enter name:")
up_name=name.upper()
lw_name=name.lower()
tl_name=name.title()
print("up_name:" ,up_name)
print("lw_name:", lw_name)
print("Title:",tl_name)"""

#print('She said,"Hi!"')
#print("She said" , "Hi!")

"""score = 98.5
print(type(score)) # Output: <class 'float'>"""

no_of_subjects= int(input("Enter no. of subjects"))
total = 0

for i in range(no_of_subjects):
    grade=int(input("Enter grade:"))
    total+=grade
    gpa=total/no_of_subjects

print("Your GPA is:", gpa)