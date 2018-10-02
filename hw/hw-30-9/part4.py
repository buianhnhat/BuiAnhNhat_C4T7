#1
hs = [45, 67, 56, 78]
print ("High score: ")
for i, item in enumerate(hs):
    print (i+1, ".", item)

#2
nh = int(input("Enter your new high score: "))
hs.append(nh)
print ("High score(Updated): ")
for i, item in enumerate(hs):
    print (i+1, ".", item)

#3
print(" ")
print(" ")
hs = [45, 67, 56, 78]
nh = int(input("Enter your new high score: "))
hs.append(nh)
max1=0
z=0
dsm=[]
for j in range(5):
    for i in range(len(hs)):
        if hs[i]>max1:
            max1=hs[i]
            vtm=i
    dsm.append(max1)
    hs.pop(vtm)
    max1=0
print ("High score(Updated): ")
for i, item in enumerate(dsm):
    print (i+1, ".", item)


#4
print(" ")
print(" ")
hs = [dsm[0], dsm[1], dsm[2], dsm[3], dsm[4]]
nh = int(input("Enter your new high score: "))
hs.append(nh)
max1=0
z=0
dsm=[]
for j in range(5):
    for i in range(len(hs)):
        if hs[i]>max1:
            max1=hs[i]
            vtm=i
    dsm.append(max1)
    hs.pop(vtm)
    max1=0
print ("High score(Updated): ")
for i, item in enumerate(dsm):
    print (i+1, ".", item)

