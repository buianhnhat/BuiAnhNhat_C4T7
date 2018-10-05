di = {
    'HELLO': 'Xin chao!',
    'HI': ''' Giong
    voi hello''',
    'ZERO': 0,
    'ONE': 1,
    'TWO': 2,
}
f = input("Find what? ").upper()
while True:

    if f in di:
        print(f, 'nghia la', di[f])
        f = input("Find what? ").upper()
    elif f=='NO':
        print("Goodbye")
        break
    else:
        print("Your word not in my dictionary! ")
        print("Do you want to add new word?")
        ans = input("Y/N? ").lower()
        if ans=='y':
            up = input("Update nghia? ")
            di[f]=up
            print("Updated!")
            f = input("Find what again? ").upper()
        elif ans=='n':
            f = input("Find what again? ").upper()
