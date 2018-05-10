# encoding=utf-8
class A(object):
    name = 'robin'


class B:
    age = 18


class C(A, B):
    sex = 'male'

print C.name, C.age, C.sex

# 查看多继承的执行顺序
print C.__mro__


'''
robin 18 male
(<class '__main__.C'>, <class '__main__.A'>, <type 'object'>, <class __main__.B at 0x101c13bb0>)
'''