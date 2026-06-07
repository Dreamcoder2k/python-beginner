#if = if the statement is true do some code
# else it is not true
from idlelib.debugger_r import restart_subprocess_debugger

#Equlas a==b
#Not Equals: a!=b
#lass than a<b
#less than or equal to a<=b
#Greater than a>b
#greater than or equal to a>=b


age = int(input("Enter your age:"))

if age >= 18:
    print("You are now signed up!")
else:
    print("You must be 18+ to sign up")


#python calculator

operator = input("Enter an operator (+ - * /):")
num1 =float( input("Enter the 1st number:"))
num2 = float(input("Enter the 2nd number:"))

if operator == "+":
    result = num1 + num2
    print(round(result))
elif operator == "-":
    result = num1 - num2
    print(round(result))
elif operator == "*":
    result = num1 * num2
    print(round(result))
elif operator == "/":
    result = num1 / num2
    print(round(result))
else:
    print(f"{operator} is not valid operator")
