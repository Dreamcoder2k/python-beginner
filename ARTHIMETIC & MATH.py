friends = 5
#friends = friends +1
#friends +=1
#friends = friends -2
#friends -=2
#friends = friends * 3
#friends *= 3
#friends = friends /2
#friends /=2
#friends = friends **2
#friends **=2
remainder = friends % 2
print(remainder)

x= 3.14
y= 4
z= 5

#result = round(x)
#result = abs(y)
#result = pow(4,3)
#result = max(x, y, z)
#result = min(x, y, z)
#print(result)



import math

radius= float(input('Enter the radius of a circle:'))
area = math.pi * pow(radius, 2)
circumference = 2 * math.pi *radius
print(f"The circumference is: {round(circumference, 2)} cm")
print(f"The area of the circle is : {round(area, 2)} cm")