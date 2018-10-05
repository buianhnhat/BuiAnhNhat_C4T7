#1+2+3
diction = {
    "name": "Bui Anh Nhat",
    "age": "15",
}

#4+5
movie = {
    'name': 'Naruto',
    'season': 2,
    'description': 'A movie about a ninja!'
}
movie['So ngoai truyen'] = '7 phan'
print(movie)

#6
add = input("Nhap them thong tin: ")
add2 = input("Thong tin: ")
movie[add] = add2
print("Name: ", movie['name'])
print("Description: ", movie['description'])

#7+8
movie = {}
add = input("Nhap them thong tin: ")
add2 = input("Thong tin: ")
movie[add] = add2
add = input("Nhap them thong tin: ")
add2 = input("Thong tin: ")
movie[add] = add2

#9+10
up = input("Update more des: ")
movie['more_description'] = up
print('more description: ', movie['more_description'])

#11+12
del movie['more_description']
print(movie)
d = input("What do you want to del? ")
del movie[d]
print(movie)
