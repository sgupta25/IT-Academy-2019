# Sarvesh Gupta
# Dice Roll
# 9/4/2019

import random
a = int(1)


while a > 0:
    x = random.randint(1,6)
    x = int(x)
    y = random.randint(1,6)
    y = int(y)
    total = int(x + y)
    pS = ""

    if total == 2:
        pS = "Snake Eyes"

    elif total == 3:
        pS = "Ace Caught A Deuce"
    
    elif total == 5:
        pS = "Little Phoebe"

    elif total == 9:
        pS = "Nina from Pasadena"

    elif total == 12:
        pS = "Boxcars"
    

    elif x == 2 and y == 2:
        pS = "Little Joe from Kokomo"

    elif x == 3 and y == 3:
        pS = "Jimmy Hicks from the Sticks"

    elif x == 4 and y == 4:
        pS = "Eighter from Decatur"

    elif x == 5 and y == 5:
        pS = "Puppy Paws"
    

    elif x == 6 and y == 1:
        pS = "Six Ace"

    elif x == 6 and y == 5:
        pS = "Six Five no Jive"

    elif x == 1 and y == 6:
        pS = "Six Ace"

    elif x == 5 and y == 6:
        pS = "Six Five no Jive"
        
    a = 0
    print (x,",",y,"\n", pS)
    q = input("Would you like to roll again? Type 1 to repeat ")
    
    if int(q) == 1:
        a = 1
    
    
    
    
