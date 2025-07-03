user = ['ayan','john','alex']

data = ['ayan', 42 , True]

epmtylist = []
print("ayan" in epmtylist)

print(user[0])
print(user[-2])

print(user.index('alex'))

print(user[0:2])
print(user[1:])
print(user[-3:-1])

print(len(data))

user.append('jack')
print(user)

user += ['tina']
print(user)

user.extend(['robert','jim'])
print(user)

# user.extend(data)
# print(user)

user.insert(0,'peter')
print(user)

user[2:2] = ['eddie','alex']
print(user)

user[1:3] = ['robert','jpg']
print(user)

user.remove('peter')
print(user)

print(user.pop())
print(user)

del user[0]
print(user)

# del data
data.clear()
print(data)

user[1:2] = ['ayan']
user.sort()
print(user)






