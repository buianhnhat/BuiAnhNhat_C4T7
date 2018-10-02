# #1
print("#1")
print("Here your list of numbers: ")
ds = [1, 6, -23, 65, 2]
for i, item in enumerate(ds):
    print (i+1, ".", item)
add = int(input("Enter new number: "))
ds.append(add)
print("Here your new list: ")
for i, item in enumerate(ds):
    print (i+1, ".", item)
kt = int(input("Type a number: "))
i=0
count = len(ds)
while i<count:
    if(kt==ds[i]):
        print("Found, position", i+1, ".")
        break
    else:
        i+=1
if(i==count):
    print("Not found the number!")

#2
print(" ")
print(" ")
print(" ")
print("#2")
print("Here your list of numbers: ")
ds = [1, 6, -23, 65, 2]
print(*ds, sep=', ')
#C1
sm = sum(ds)
print("Sum of all numbers:", sm)
#C2
sm = 0
i  = 0
count = len(ds)
while i<count:
    sm = sm+ds[i]
    i+=1
print("Sum of all numbers:", sm)
print(" ")
print(" ")
print(" ")

#3 
print("#3")
lst = input('Enter a list of numbers, separated by ‘ ‘: ').split()
lst = list(map(lambda x: int(x) if x.isdigit() else 0, lst))
sm = sum(lst)
print("Sum of all numbers:", sm)
print(" ")
print(" ")
print(" ")

#4
print("#4")
ev=[]
ds = [1, 6, 232, 65, 2, 9, 43, 88, 10]
print("List: ", *ds, sep=' ')
for i in range (len(ds)):
    if(ds[i]%2==0):
        ev.append(ds[i])
print("All even numbers:", *ev, sep=' ') 
print(" ")
print(" ")
print(" ")

#5
print("#5")
dss = input('Enter a list of numbers, separated by ‘ ‘: ').split()
dss = list(map(lambda x: int(x) if x.isdigit() else 0, dss))
ev=[]
for i in range (len(dss)):
    if(dss[i]%2==0):
        ev.append(dss[i])
print("All even numbers from entered list:", *ev, sep=' ') 

