#for loops = execute a code a fixed number of times
from itertools import count

for x in range(1,100):
    if x == 89:
        break
    else:
        print(x)