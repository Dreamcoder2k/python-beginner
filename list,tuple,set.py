# collection = single "variable used to store multiple values
# list =[]
# set = {}
# Tuple=()

dream_country =("chennai","china","japan","south korea","bejing","china")


print(dir(dream_country))
print(help(dream_country))
print(len(dream_country))
print("kerala"in dream_country)

#set
dream_country.add("thanjavur")
dream_country.remove("chennai")
print(dream_country)
dream_country[0] = "kerala"
for country in dream_country:
    #print(country)


dream_country.append("kerala")
dream_country.remove("chennai")
dream_country.insert(0, "shenzen")
dream_country.sort()
dream_country.reverse()
dream_country.clear()
print(dream_country.index("bejing"))
print(dream_country.count("south korea"))
print(dream_country)


for country in dream_country:
    print(country)



