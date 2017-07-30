# -*- coding:utf-8 -*-
# author yuzuo.yz 2017/7/30 17:20
from collections import Iterator, Iterable


def slice_list():
    # 生成数值集合
    list1 = range(100)

    print list1
    # 起始位置:终了位置:步长
    # -1表示倒数第一个
    print list1[:10]
    print list1[:-10]
    print list1[-10:]
    print list1[2:15]
    print list1[::3]


# 使用collections.Iterable判断是否能迭代
def test_iter():
    s1 = 'hell0'
    list1 = [1, 2, 3, 6]
    i = 123
    map1 = {'name': 'boduo', 'age': 21}

    print isinstance(s1, Iterable)
    print isinstance(list1, Iterable)
    print isinstance(i, Iterable)
    print isinstance(map1, Iterable)

    for item in s1:
        print item
    for item in list1:
        print item
    for item in map1:
        print item

    for item in map1.keys():
        print item
    for item in map1.values():
        print item
    for item in map1.items():
        print item
        print item[0]
        print item[1]
    # items返回列表.列表直接获取了所有的元素
    for k, v in map1.items():
        print k
        print v
    # iteritems返回迭代器.迭代器通过.next逐个获取元素
    for k, v in map1.iteritems():
        print k
        print v


def for_list():
    print [x for x in range(100) if x % 3 == 0]
    print [x * 2 for x in range(10)]


def test_tuple():
    # tuple无法添加新的元素，也无法修改不可变元素，比如str
    # 但是tuple可以修改里面引用对象的属性
    t = (['kang'], ['bodo', 'song'])
    print t
    t[0][0] = 'long'
    print t


def main():
    # slice_list()
    # test_iter()
    # for_list()
    test_tuple()

if __name__ == '__main__':
    main()
