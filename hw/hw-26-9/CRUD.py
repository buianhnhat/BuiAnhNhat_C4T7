print("This is you list! What do you want to do?")
ds = []
ip = input("Choose 1 action: C, R, U, D! ")
while True:
    while ip not in ["C", "R", "U", "D"]:
        print ("Invaild answer!!!")
        ip = input("Choose 1 action again: C, R, U, D! ")
    if ip=='C':
        new_item = input("What is your favorite thing? ")
        ds.append(new_item)
        ip = input("Choose 1 action again: C, R, U, D! ")
    if ip=='R':
        count = len(ds)
        if count==0:
            print ("Nothing!")
        else: 
            for i, item in enumerate(ds):
                    print(i+1, ".", item)
        ip = input('Choose 1 action again: C, R, U, D! ')
    if ip=='U':
        vt = input("Where do you want to replace? ")
        up = input("Update to? ")
        ds[vt]=up 
        ip = input("Choose 1 action again: C, R, U, D! ")
    if ip=='D':
        dele = int(input("Where do you want to delete? "))
        ds.pop(dele)
        ip = input("Choose 1 action again: C, R, U, D! ")