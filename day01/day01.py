
import sys
import io
print(sys.version)  # 系统版本
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 支持中文

###
a = ['hellow', 'world', 1, 2, 3, 4]

print ('a:', a)

print ('a.lenth:', len(a))

print ('Slice切片:', a[0:3])


def saySome(people: int, wold: int):
    print(people + wold)


# saySome('kj', 'haha')
saySome(1, 20)

c, b = 1, 2
print(c, b)


def oneToHunder():
    allCount = 0
    for value in range(101):
        allCount = allCount + 1
        print ('allCount:', allCount)


# oneToHunder()


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print('fib:', b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fib(10)


# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break


# map

def f(x):
    return x * x


r = map(f, range(1, 11))

print ('list(r):', list(r))

from functools import reduce


def add(x, y):
    return x + y


r = reduce(add, [1, 3, 5])
print('r', r)

s = sorted([36, 5, -12, 9, -21], key=abs)
print('s:', s)
