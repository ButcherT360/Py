try:
    import json
    dictionary = {"Ihminen": "Human"}
    with open('kirjasto.json', 'r') as lue:
        dictionary = json.load(lue)
except:
  print("No dictionary found using default dictionary ")
#y = json.dumps(dictionary)
#print(y)
while True:
    s = input("Search for a word in the dictionary or quit by entering nothing ")

    if len(s) == 0:
        break

    elif s in dictionary:
        #print(s + " is in this dictionary")
        #for key, value in dictionary.items() :
        print(s + " = " + dictionary.get(s))

    else:
        new = input("This word is not found insert definition ")
        dictionary[s] = new

        #dictionary.update({s: new})
        print(dictionary)

with open('kirjasto.json', 'w') as tal:
    json.dump(dictionary, tal) 
