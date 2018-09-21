from random import randint

n = int(input("Hello players, want to chanllenge the computer??? Type your number: "))
i = 0
z = 100
y = 0
x = 0
while x!=n:
    x = randint(y, z)
    print ("The computer guess: ", x)
    i +=1
    if n==x:
        print (" THE COMPUTER GUESSED TRUE NUMBER!!! YOU LOSE!")
        break
    else: 
        ans=input("Lower or higher??? ")
        while ans not in ["lower", "Lower", "Higher", "higher"]:
            print("Please let the computer know, stop CHEATING =((")
            ans=input("Lower or higher??? ")
        if ans in ["lower", "Lower"]:
            z=x-1
        if ans in ["higher", "Higher"]:
            y=x+1
    if i==8:
        print ("THE COUMPUTER CAN'T GUESS TRUE NUMBER!!! YOU WIN =))")
        break
    
