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

user.sort(key=str.lower)
print(user)

nums = [4,56,78,1,6]
print(type(nums))
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

numscopy= nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(nums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1,"amsterdam",True])
print(mylist)

# tuples
mytuple = tuple(('ayan', 42, True))

anothertuple = (1,2,3,4,5,7,8,2,2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('amsterdam')
newtuple = tuple(newlist)
print(newtuple)
 
(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))
print("This is the last line in the python")

