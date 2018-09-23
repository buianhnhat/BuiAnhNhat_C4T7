from random import randint

print ("Hello players!!! Do you want to check your mathematical level :V Let's play!")
while True:
    x = randint (0, 20)
    y = randint (0, 20)
    z = randint (21, 22)
    p = randint (-1, 1)
    k = x+y+p
    q = x-y+p
    if (z==21):
        print (x, "+", y, "=", k)
        kq = input ("(Y/N)? ")
        if (x+y==k):
            if (kq == "Y"):
                print ("True True True")
            else:
                print ("False - GAME OVER")
                break
        else:
            if (kq == "N"):
                print ("True True True")
            else:
                print ("False - GAME OVER!!!")
                break
    else:
        print (x, "-", y, "=", q)
        kq = input ("(Y/N)? ")
        if (x-y==q):
            if (kq == "Y"):
                print ("True True True")
            else:
                print ("False - GAME OVER")
                break
        else:
            if (kq == "N"):
                print ("True True True")
            else:
                print ("False - GAME OVER")
                break