# Sarvesh Gupta
# Integer Sort program
# 9/18/2019

import random

unordered = list(range(10))
ordered = []
random.shuffle(unordered)
i = 0;
print(unordered)

while len(unordered) > 0:
    lowest = unordered[0]
    for i in unordered:
        if i < lowest:
            lowest = i
    ordered.append(lowest)
    unordered.remove(lowest)

print(ordered)
    

