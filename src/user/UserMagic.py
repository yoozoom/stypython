# -*- coding:utf-8 -*-
# author yuzuo.yz 2017/7/28 19:45

# 注意导入模块的关系
import UserVo
from UserVo import hello_user as hu


class UserMagic2(object):
    def __init__(self, age):
        self.age = age


class UserMagic(object):
    def __init__(self, age):
        self.age = age

    def __add__(self, other):
        return self.age + other.age

    def __eq__(self, other):
        if isinstance(other, UserMagic):
            return self.age == other.age
        else:
            raise Exception("error type, other is not UserMagic type")

    def __str__(self):
        return "i am %s years old. %s" % (self.age, "haha")


def main():
    u1 = UserMagic(10)
    u2 = UserMagic(12)

    u3 = UserMagic2(22)

    print type(u1)
    print type(u2)
    print type(u3)

    print u1
    print dir(u1)
    print len(dir(u1))

    print u1 == u2
    print u1 + u2
    try:
        print u1 == u3
    except Exception, e:
        print e

    # 使用模块.类名 来使用其他文档定义的类
    uvo = UserVo.UserVo("a", 1)

    try:
        print u1 == uvo
    except Exception, e:
        print e

    UserVo.hello_user()
    hu()

if __name__ == '__main__':
    main()
