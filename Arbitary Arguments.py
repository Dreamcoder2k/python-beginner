# Arbitrary Arguments is *args and **Kwargs
#allow pass multiple arguments non-key arguments
#allow pass multiple keyword arguments


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')},{kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    
    print(f"{kwargs.get('city')},{kwargs.get('state')},{kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street = "123, fake st",
               pobox="#1001",
               city="chennai",
               state="tamilnadu",
               zip="608732")

