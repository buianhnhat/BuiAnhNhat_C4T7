#1
com = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30,
}

#2
print("Số lượng MACBOOK có trong kho:", com['MACBOOK'])

#3
print(" ")
com2 = input("Nhập hãng máy tính: ").upper()
print("Số lượng", com2, "có trong kho:", com[com2])

#4
com['TOSHIBA'] = 10

#5
com3 = input("Nhập hãng máy tính bạn muốn thêm: ").upper()
com31 = int(input("Số lượng: "))
com[com3] = com31
print(" ")

#6
com['DELL'] +=10
com['MACBOOK'] = 2

#7
for k, v in com.items():
    print(k, ':', v)

#8
tong=0
for k in com.values():
    tong+=k
print("Tổng số máy trong kho là", tong)

#9
com['FUJISU'] = 15
com['ALIENWARE'] = 5

#10

#11
pr = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 12000,
    'ASUS': 400,
    'ACER': 350,
    'TOSHIBA': 600,
    'FUJISU': 900,
    'ALIENWARE': 1000,
}

#12
print("Giá của 1 máy ASUS là", pr['ASUS'])
print(" ")

#13
c = input("Nhập hãng máy tính: ").upper()
print("Giá máy của hãng", c, "là", pr[c])
print(" ")

#14
print("Giá trị của đơn hàng là", pr['ASUS']*5)
print(" ")

#15
c = input("Nhập hãng máy tính: ").upper()
sl = int(input("Số lượng: "))
print("Giá trị của đơn hàng là", com[c]*sl)
print(" ")

#16
com[c] -= sl

#17
c2 = input("Nhập hãng và số lượng: ")
l = c2.split(":")
l[0] = l[0].upper()
com[l[0]] -= int(l[1])
for m, n in com.items():
    print(m, ':', n)

#18+19
print("PRICE")
for i in com.keys():
    gt = com[i]*pr[i]
    print(i, gt, sep=':')
print("TOTAL PRICE")
tong=0
for i in com.keys():
    tong += com[i]*pr[i]
print("TOTAL: ", tong)




