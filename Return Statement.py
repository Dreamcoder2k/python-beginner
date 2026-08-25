# Return Statement whenever I call the function it will return some data

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("rachel", "kanmani")
print(full_name)
