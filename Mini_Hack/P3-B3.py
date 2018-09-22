n = int(input("Nhập tháng: "))
if (n in [1, 3, 5, 7, 8, 10, 12 ]):
    print ("Tháng này có 31 ngày!")
elif(n == 2):
    print ("Tháng này có 28 hoặc 29 ngày!")
else:
    print ("Tháng này có 30 ngày!")