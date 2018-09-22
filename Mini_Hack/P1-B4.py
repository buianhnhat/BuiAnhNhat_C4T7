from turtle import*
shape("turtle")
n = int(input("Nhập bán kính hình tròn: "))
speed(0)

forward (n)
for i in range (360):
    forward(3)
    left(1)


mainloop()
