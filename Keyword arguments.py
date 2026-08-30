# Keyword Arguments = order doesn't matter, an argument is preceded by identifier

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country= 91, area= 91, first=12134, last=23233)

print(phone_num)