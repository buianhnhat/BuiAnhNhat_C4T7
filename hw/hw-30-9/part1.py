#1+2
print("Here is your list:")
ds = ["blue", "red", "green"]
print(*ds, sep=', ',)
#3
add = input("What color do you want to add? ")
ds.append(add)
print("Here is your new list:")
for i, item in enumerate(ds):
    print (i+1, ".", item)
#4
vitri = int(input("Enter position: "))
while True:
    if(vitri>4 or vitri<1):
        vitri = int(input("Enter position AGAIN, IDIOT: "))
    else:
        print("Color at position", vitri, ":", ds[vitri-1])
        break

#5
xoa1= input("Number or Letter? ")
if (xoa1=="Number"):
    xoa = int(input("Item to delete: "))
    while True:
        if(xoa<1 or xoa>4):
            xoa = int(input("Type item to delete AGAIN: "))
        else:
            ds.pop(xoa-1)
            print("Here is your new list:")
            for i, item in enumerate(ds):
                print (i+1, ".", item)
            break
if (xoa1=="Letter"):
    xoa = input("Item to delete: ")
    while True:
        if(xoa not in ds):
            xoa = input("Type item to delete AGAIN: ")
        else:
            ds.remove(xoa)
            print("Here is your new list:")
            for i, item in enumerate(ds):
                print (i+1, ".", item)
            break
#6
from turtle import*


pencolor("blue")
forward(50)
pencolor("red")
forward(50)
pencolor("green")
forward(50)

mainloop()

