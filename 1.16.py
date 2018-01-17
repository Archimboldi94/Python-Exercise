import math


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(2, 4))
print(power(2))


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('kongjian', '18', '23', 'guangzhou')
enroll('Adam', 'M', city='Tianjin')


# def add_end(L=[]):
#     L.append('END')
#     print(L)
#     return L

def add_end(L=None):
    if L is None:
        L = []
        print('haha')
    L.append('END')
    print(L)
    return L


add_end()
add_end()
add_end()

# def calc(*numbers, x=2):
#     sum = 0
#     for n in numbers:
#         sum = sum + pow(n, x)
#     print(sum)
#     return sum
#
#
# calc(1, 2, 3, x=3)


def person(name, age, **kw):
    if 'city' in kw:
        # city
        print('have \'city\'')
        pass
    if 'job' in kw:
        #
        print('have \'job\'')
        pass
    print('name:', name, 'age:', age, 'other:', kw)


extra = {'city': 'Beijing', 'job': 'Engineer'}

person('kj', '23', city=extra['city'], job=extra['job'])
person('kj', '23', **extra)
#


def fact(n):
    if n == 1:
        return 1
    # print(n * fact(n - 1)) why?
    return n * fact(n - 1)


a = fact(5)
print(a)

# :


def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(4, 'A', 'B', 'C')


nublist = []
n = 1
while n <= 99:
    nublist.append(n)
    n = n + 2  # if no this line . the code will keep runing
print(nublist)


L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[1:3])  # no include 'index3'
print(L[-2:-1])
print(L[:3])
print(L[-3:])

haha = 'haha'
hehe = haha
haha = 'dada'
print(hehe)

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

print(max(nublist))
print(min(nublist))

#[1x1, 2x2, 3x3, ..., 10x10]

coollist = [x * x for x in range(1, 11)]
print(coollist)
coollist = [x * x for x in range(1, 11) if x % 2 == 0]
print(coollist)

print('----sanjiao-----')

qq1, qq2 = [0, 1, 3, 3, 1], [1, 3, 3, 1, 0]
qq = zip(qq1, qq2)
print(qq)
for dede in qq:
    print(sum(dede))

print('------sanjiao------')


def triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]
        print(a)


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 8:
        break


L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
LL = [i + 1 for i in L]
print('LL =', LL)
