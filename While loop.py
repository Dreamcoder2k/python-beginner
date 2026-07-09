#While loop = execute some code WHILE some condition is true

#basic
name = input("Enter your name:")

while name == "":
    print("You did not enter your name")
    name= input("Enter your name:")

print(f"Hello {name}")

#With logical operators NOT
food = input("Enter a food you like (q to quit):")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit):")
print("bye")

#With OR operator
num = int(input("Enter a number between 10 - 20:"))

while num < 10 or num > 20:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 10 - 20:1"))
print(f"Your number is {num}")