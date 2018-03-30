
import sys
import io
import os
print(sys.version)  # 系统版本
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 支持中文

#--------打开文件
### 在atom中获取的地址跟终端的不一样 / os.path.abspath('.') ####
addressStr = os.path.abspath('.') + '/day02/test.txt'
print('addressStr:', addressStr)
os.path.join('/Users/kongjian/Desktop/py', 'testdir')

f = open(addressStr, 'r')

#--------修改文件
# 排它锁 非排它锁 ???
# r = open('/Users/kongjian/Desktop/py/day02/test.txt', 'r')
# w = open('/Users/kongjian/Desktop/py/day02/test.txt', 'w')
# print('test.txt:', r.read())
# w.writelines(["11111222", "3333333333"])
# w.close()
# print('test.txt2:', r.read())
# a = open("/Users/kongjian/Desktop/py/day02/test.txt", "a")
# a.writelines(["oooooo", "kkkkk"])
# a.close()

#--------添加删除文件夹
# 添加目录
#os.mkdir('%s/haha' % os.path.abspath('.'))
# 删除目录
#os.rmdir('%s/haha' % os.path.abspath('.'))

#--------
