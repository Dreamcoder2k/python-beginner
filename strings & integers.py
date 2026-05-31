#variable = A container for a value (string, integer, float, boolean)


#strings
from operator import truediv

first_name="bro"
food= "pizza"
email = "bro@fake.com"

#integers
age=25
quantity=3.5

#float
price =10.99
gpa = 3.2
print(f"the price is ${price}")
print(f"the gpa is: {gpa}")

#boolean
is_student= False
for_sale = False

if is_student:
    print("That item is for sale")
else:
    print("that item is not available")

#boolean
is_student= False
for_sale = False
is_online = True

if is_online:
    print("You are online")
else:
    print("you are offline")


#strings
user_name = "bro code"
year = 2024
pi =3.14
is_admin = True

print(f"Hey {user_name}")
print(f"you are {year}")
print(f"Pi value is {pi} ")

if is_admin:
    print("if it is true")
else:
    print("it is not true")