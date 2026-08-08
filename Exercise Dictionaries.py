# Menu Program

menu = {"pizza": 3.00,
        "nachos": 55.00,
        "popcorn":525.00,
        "burger":100.00,
        "french fries":120.00,
        "coke": 80.00,
        "sprite":90.00,
        "chips":70.00}
cart=[]
total=0

print("---------MENU--------")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("---------------------")

while True:
    food=input("Select an item (q to quit):").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"total is: ${total:.2f}")