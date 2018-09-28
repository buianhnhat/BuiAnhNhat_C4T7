from random import shuffle

n = input("Enter your word: ")
ds = list(n)
count = len(ds)
shuffle(ds)
print("Jumbled word: ")
for i in range (count):
    print(ds[i].upper())