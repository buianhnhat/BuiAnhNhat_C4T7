#1
print('#1')
max1=0
min1=1000000000000
ten = ['ST', 'BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
ds = [150300, 247100, 333300, 266800, 420900, 318000]
for i in range(len(ds)):
    if ds[i]>max1:
        max1=ds[i]
        vtm=i
    if ds[i]<min1:
        min1=ds[i]
        vtm2=i
print("Biggest:", ten[vtm], "with", max1, "people")
print("Smallest:", ten[vtm2], "with", min1, "people")

#2
print('#2')
dt = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
mddc = []
for i in range(len(dt)):
    mddc.append(ds[i]/dt[i])
    print(ten[i], ":", mddc[i], "nguoi/km")

#3
tmdc=0
print('#3')
for i in range(len(dt)):
    tmdc+=mddc[i]
print("Mat do dan cu TB =", tmdc/len(dt), "nguoi/km")



