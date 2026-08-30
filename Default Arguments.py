# Default Arguments = A default value for certain parameters
# if we don't enter any value for that particular parameter argument uses default values

import time

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!!")

count(30,15)
