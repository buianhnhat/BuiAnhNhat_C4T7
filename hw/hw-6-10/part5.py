from random import randint
nv = {
    'Name' : 'Light',
    'Age' : 17,
    'Strength' : 8,
    'Defense' : 10,
    'HP' : 100,
    'Backpack' : ['Shield', 'Bread Loaf'],
    'Gold' : 100,
    'Level' : 2,
}
nv['Gold'] += 50
nv['Backpack'].append('FlintStone')
nv['Pocket'] = ['MonsterDex', 'Flashlight']
skill=[
    {
        'Name' : 'Tackle',
        'Minimum level' : 1,
        'Damage' : 5,
        'Hit rate' : 0.3
    },
    {
        'Name' : 'Quick Attack',
        'Minimum level' : 2,
        'Damage' : 3,
        'Hit rate' : 0.5
    },
    {
        'Name' : 'Strong Kick',
        'Minimum level' : 4,
        'Damage' : 7,
        'Hit rate' : 0.2
    }
]
print('SKILLS')
for i in range(len(skill)):
    print('Skill:', i + 1, sep=' ')
    print(skill[i]['Name'])

print("It's time to COMBAT!!!")
while True:
    a = input('Choose a skill: ')    
    if a == '1':
        if skill[0]['Minimum level'] <= nv['Level']:
            x= randint(0, 1)
            if x <= skill[0]['Hit rate']:
                print('You dealed ', skill[0]['Damage'], 'damage' )
            else:
                print('You missed')
        else:
            print("You don't have enough level!")
    elif a == '2':
        if skill[1]['Minimum level'] <= nv['Level']:
            x= randint(0, 1)
            if x <= skill[1]['Hit rate']:
                print('You dealed ', skill[1]['Damage'], 'damage' )
            else:
                print('You missed')
        else:
            print("You don't have enough level!")
    elif a == '3':
        if skill[2]['Minimum level'] <= nv['Level']:
            x= randint(0, 1)
            if x <= skill[2]['Hit rate']:
                print('You dealed ', skill[2]['Damage'], 'damage' )
            else:
                print('You missed')
        else:
            print("You don't have enough level!")
    else:
        print('Wrong skill!!!')