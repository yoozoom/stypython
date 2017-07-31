# -*- coding:utf-8 -*-
# author yuzuo.yz 2017/7/31 16:14
# from mod1 import TpJop
import mod1 as mod1
from mod1 import TpJop

from sub.sub1 import SubVo


def main():
    tp = mod1.TpJop('name')
    print tp
    tp.do_add()

    tp = TpJop('name2')
    print tp
    tp.do_add()

    print mod1.TP_TEST

    mod1.add_tp()

    s = SubVo('sub1')
    print s.name

if __name__ == '__main__':
    main()
