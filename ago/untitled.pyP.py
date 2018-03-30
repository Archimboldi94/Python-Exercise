

# use  'list' and 'tupe'


classmates = ['Michael', 'Bob', 'Tracy']

print('Hello %s' % classmates[0])

print('Hello %s Hi %s' % (classmates[0], classmates[1]))

print('Hello %s' % classmates[-1])

classmates.append('Adam')

print(classmates)

s = ['python', 'java', ['asp', 'php'], 'scheme']

print(len(s))

s2 = s[2]

print(s[2])

print(s2[0])

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]


print(L[0][0])
print(L[1][1])
print(L[2][2])
#
# age = input('brith:')
# age = int(age)
#
# if age > 2000:
#     print ('00hou')
# else:
#     print ('00qian')

sum = 0

for x in range(101):
    sum = sum + x
    print(sum)
    # run with other lines code
print(sum)

# --------------
