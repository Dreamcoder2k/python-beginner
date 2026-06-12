# Logical Operators
# or
#and
#not

temp = 20
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print(f"The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")


temp = 25
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("it is Sunny")
elif temp <28 and is_sunny:
    print("It is cold")
    print("It is HOT")
elif 28 > temp >0 and is_sunny:
    print("It is Hot")
    print("It is really sunny")

