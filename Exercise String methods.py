#validate user input
#username no more than 12 characters
#username must not contain spaces
#username must not contain digits

username= input("Enter a username :")

if len(username) >12:
    print("Your username should be in 12 ")
elif not username.find(" ") == -1:
    print("your username must not contain spaces")
elif not  username.isalpha():
    print("Your username must not in digits")
else:
    print(f"Welcome {username}")