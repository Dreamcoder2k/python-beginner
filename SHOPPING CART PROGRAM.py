#EXERCISE 2 SHOPPING CART PROGRAM
item = input("What item would you like to buy:")
price = float(input("what is the price?:"))
quantity =int(input("How many would you like?:"))
total = int(price * quantity)

print(f"you bought {quantity} x {item}/s")
print(f"your total is ${total}")