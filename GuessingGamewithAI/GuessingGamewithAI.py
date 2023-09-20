import random
luku = random.randrange(1, 100)
luku2 = 0
luku3 = 100
while True:

    arvaus = luku
    print("is the number " + str(arvaus))
    i = input("y/n?")
    if(i == "y"):
        print("got you!") 
        break
    elif( i == "n"):
        print("Is the number smaller than " + str(arvaus))
        b = input("y/n?")
        if(b == "y"):
                luku3 = random.randrange(1, luku)
                luku = luku3
        elif( b == "n"):
            luku2 = random.randrange(luku, 100)
            luku = luku2