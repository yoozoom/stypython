# -*- coding:utf-8 -*-
# author yuzuo.yz 2017/7/27 20:43

import numpy as np


def main():
    list1 = [1, 2, 3]
    print "start main"
    print list1

    print type(list1)

    np_list = np.array(list1, dtype=np.int8)
    print type(np_list)
    print np_list

    # 2
    print np.zeros([2, 4])
    print np.ones([3, 5])

    # random
    print 'test random....'
    print np.random.rand()     # 0-1随机数
    print np.random.rand(10)    # 0-1 10个随机数
    print np.random.rand(2, 4)  # 2行4列随机数
    print np.random.randint(1, 10)  # 1-10中随机数
    print np.random.randint(1, 10, 5)   # 5个1-10中随机数
    print np.random.randn(2, 3)      # *dn参数表示维度， # 1-10中随机数正态分布的2,3-> 2行3列   2,3,4-> 2行3列4高
    print np.random.choice([1, 2, 3, 4], 4)    # a是array的意思。重数组中获取随机几个数字

    print np.random.beta(1, 10, 100)

    # array opt
    print "array opt"
    print np.arange(1, 100, 3)      # 等差数列。开始，结束，步长
    la1 = np.arange(1, 10, 2)      # 等差数列。开始，结束，步长
    print (np.arange(1, 100, 3).reshape([3, -1]))  # 将等差数列重组成3行X列.维la1度重组
    print "la1", la1
    print "exp:", np.exp(la1)
    print "log", np.log(la1)
    print "log2", np.log2(la1)
    print "log2", np.log2([1, 2, 3, 4, 5, 6, 7, 8])
    print "sqrt", np.sqrt(la1)  # 开方
    print "square", np.square(la1)  # 平方
    print "power", np.power(la1, 3)     # 3次方
    print "sin", np.sin(la1)
    print "cos", np.cos(la1)

    la2 = np.array([
                       [[1, 2, 3], [7, 8, 9]],
                        [[4, 5, 6], [10, 11, 12]]
                    ])

    print la2
    print "sum", la2.sum()
    print "max", la2.max()
    print "min", la2.min()

    print "sum", la2.sum(axis=0)
    print "max", la2.max(axis=0)
    print "min", la2.min(axis=0)

    print "sum", la2.sum(axis=1)
    print "max", la2.max(axis=1)
    print "min", la2.min(axis=1)

    print "sum", la2.sum(axis=2)
    print "max", la2.max(axis=2)
    print "min", la2.min(axis=2)

    la3 = np.array([1, 2, 3])
    la4 = np.array([4, 5, 6])

    print "+", la3 + la4
    print "-", la3 - la4
    print "x", la3 * la4
    print "/", la4 / la3
    print "xx", la4**la3

    la5 = np.array([[1, 2], [1, 1]])
    la6 = np.array([[1, 2], [1, 1]])

    print "dot", np.dot(la5, la6)    # 矩阵乘法
    print "concatenate", np.concatenate((la5, la6))
    print "concatenate0", np.concatenate((la5, la6), axis=0)
    print "concatenate1", np.concatenate((la5, la6), axis=1)
    print "vstack", np.vstack((la5, la6))
    print "hstack", np.hstack((la5, la6))
    print "split", np.split(la1, 5)         # 拆分集合，必须要能整除

if __name__ == '__main__':
    main()
else:
    print "import..."
