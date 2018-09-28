fav = ["Esport", "LOL", "Code", "EDM", "MOBA", "Netflix", "Codefun"]
print (fav)
new = input("Add new fav: ")
fav.append(new)
print (*fav, sep=' | ')
print (fav[0].upper())
print (fav[-1].upper())
print (fav[-2].upper())
rp = input("Your fav movie? ")
fav[0] = rp
print (fav)
rp2 = input("Your fav book? ")
fav[-1] = rp2
print (fav)
vitri = int (input("Nhap vi tri? "))
nd = input("Thu ban muon doi? ")
fav[vitri] = nd
print (fav)
fav.pop(1)
print (fav)
fav.remove("Code")
xoa = int(input("Muon xoa cai nao? "))
fav.pop(xoa)
xoa2 = input("Muon xoa cai nao? ")
fav.remove(xoa2)
print(fav)
for i, item in enumerate(fav):
    print (i+1, ".", item.upper())
print("  ")
for i, item in enumerate(fav):
    if ('e' in item):
        print (i+1, ".", item)






