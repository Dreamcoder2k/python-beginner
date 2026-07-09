#format specifiers = {value:flags}

price1 = 3.14455
price2 = -987.98
price3 = 12.34

#print(f"price1 is ${price1:.2f}")
#print(f"price1 is ${price2:.2f}")
#print(f"price1 is ${price3:.2f}")

#print(f"price1 is ${price1:10}")
#print(f"price2 is ${price2:10}")
#print(f"price3 is ${price3:10}")
#gives 10 spaces

#print(f"price1 is ${price1:010}")
#print(f"price2 is ${price2:010}")
#print(f"price3 is ${price3:010}")


#print(f"price1 is ${price1:<10}")
#print(f"price2 is ${price2:<10}")
#print(f"price3 is ${price3:<10}")
#right justify

#print(f"price1 is ${price1:>10}")
#print(f"price2 is ${price2:>10}")
#print(f"price3 is ${price3:>10}")
#left justify

#print(f"price1 is ${price1:^10}")
#print(f"price2 is ${price2:^10}")
#print(f"price3 is ${price3:^10}")
#all the values will be centered

#print(f"price1 is ${price1:+}")
#print(f"price2 is ${price2:+}")
#print(f"price3 is ${price3:+}")
#if the values need + (positive symbol)

print(f"price1 is ${price1:+,.2f}")
print(f"price2 is ${price2:+,.2f}")
print(f"price3 is ${price3:+,.2f}")
# all the format specifiers