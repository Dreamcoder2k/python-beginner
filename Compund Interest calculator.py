#compound interest calculator

principal = 0
rate = 0
time = 0


while True:
    principal= float(input("Enter principal amount: "))
    if principal < 0:
        print("Enter the principal amount less than  0")
    else:
        break
while True:
    rate = float(input("Enter rate amount: "))
    if rate < 0:
        print("Enter the rate amount less than  0")
    else:
        break
while True:
    time= int(input("Enter time amount: "))
    if principal < 0:
        print("Enter the time amount less than 0")
    else:
        break

total= principal * pow((1 + rate/100),time)
print(f"Balance after {time} year/s: ${total:.2f}")









