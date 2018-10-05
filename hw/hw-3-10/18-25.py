#18+19
fl = [
    {
        'Name': 'Huy',
        'Role': 'Waiter',
        'Hour': 12,
        'Salary per Hour($):': 0.8,
    },
    {
        'Name': 'Tung',
        'Role': 'Cook',
        'Hour': 24,
        'Salary per Hour($):': 1.5, 
    },
    {
        'Name': 'M.Duc',
        'Role': 'Manager',
        'Hour': 20,
        'Salary per Hour($):': 2,
    },
    {
        'Name': 'Don',
        'Role': 'Waiter',
        'Hour': 12,
        'Salary per Hour($):': 0.9, 
    },
    {
        'Name': 'H.Duc',
        'Role': 'Waiter',
        'Hour': 14,
        'Salary per Hour($):': 0.7,
    },
]

#20
print('Salary per Hour($):', fl[2]['Salary per Hour($):'])
print(" ")

#21
fl[0]['Name'] = 'Huyen'
fl[0]['Role'] = 'Waitress'
fl[0]['Hour'] = 14
fl[0]['Salary per Hour($):'] = 1
print(fl[0])
print(" ")

#22+23
del fl[4]
for i in range (4):
    print (fl[i])
print(" ")
print(" ")

#24
tong=0
for i in range (4):
    fl[i]['Salary per Month($):'] = fl[i]['Hour']*fl[i]['Salary per Hour($):']*30
    print (fl[i])
    tong+=fl[i]['Salary per Month($):']
print("The store need($)", tong, "to pay all the employees!")




