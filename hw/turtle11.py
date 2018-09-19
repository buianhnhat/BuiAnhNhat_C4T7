from turtle import *
shape ("turtle")
speed(0)
k=50
j=90
for i in range (15):
    for i in range(4):
        for i in range(2):
            left (60)
            forward (k)
            left(60)
            forward (k)
            left(60)
        right(j)
    k=k+5
    j=j+1
    



mainloop()