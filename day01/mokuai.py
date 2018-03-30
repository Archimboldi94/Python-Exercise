
import sys
import io
print(sys.version)  # 系统版本
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 支持中文


class mouth(object):
    """docstring for [object Object]."""

    def eat(arg):
        print('eat', arg)


def drink(arg):
    print('drink', arg)


#__name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。
# 这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
if __name__ == '__main__':
    drink('water -- 我在里面')
