# -*- coding:utf-8 -*-
# author yuzuo.yz 2017/7/31 17:38


def get_d_list(lst):
    for i in lst:
        if i % 2 == 0:
            yield i


def get_next_1():
    print "1...."
    yield 11
    print '2....'
    yield 22


def main():
    list1 = range(20)
    for i, v in enumerate(list1):
        print v, ":", i

    a = get_d_list(list1)
    print a.next()
    print '====================='
    for x in a:
        print x

    b = get_next_1()
    print b.next()
    print b.next()
    print b.next()


if __name__ == '__main__':
    main()
