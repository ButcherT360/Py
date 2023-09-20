import random  #tuodaan import funktio

i = 0
list = [] # lista
while i < 1: #while loop
    #print("empty string")
    inp = input("Enter name ") #syötä nimi
    if len(inp) == 0: # jos inputin pituus on 0 loppuu ohjelma tässä vois olla myös että i++ tai joku i = 1 niin breakkais looppi.
           break
    else:
         list.append(inp)  #lisätään listaan
         s = sorted(list)  #Sorted funktiolla voi tehdä myös list.sort(list)
         print("Ordered ALPHABETHICALLY")
         print(*s, sep = "\n")    # * kertomerkki tekee jotain että ei tule bräkettejä.. ja sep = on miten erotellaan.
         print("Ordered RANDOMLY")
         random.shuffle(list)  #random funktiolla random järjestys
         print(*list, sep = "\n")