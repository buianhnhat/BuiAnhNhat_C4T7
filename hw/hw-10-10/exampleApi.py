import requests
r = requests.get("https://jsonplaceholder.typicode.com/users", auth=('user', 'pass'))
lst = r.json()
i =-1
idl =input("Enter username: ")
while True:
    i+=1
    if  idl.title() in lst[i]["username"]:
        print (lst[i])
        break
