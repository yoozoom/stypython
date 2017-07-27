# -*- coding:utf-8 -*-
# author yuzuo.yz 2017/7/27 20:43

import numpy as np

def main():
    list1 = [1,2,3]
    print "start main"
    print list1

    print type(list1)

    npList = np.array(list1, dtype=np.int8)
    print type(npList)
    print npList

if __name__ == '__main__':
    main()