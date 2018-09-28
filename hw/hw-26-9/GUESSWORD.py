from random import randint 
from random import shuffle


ds = ['esport', 'music', 'game', 'lmht', 'hello', 'world', 'moba', 'players']
count = len(ds)
x = randint(0, count-1)
word = ds[x]
ds2=list(word)
shuffle(ds2)
for i in range (len(ds2)):
    print(ds2[i].upper())

while True:
    g = input("Guess what: ")
    if(g==word):
        print("True!!!")
        break
    else:
        print("False! Try again!")

