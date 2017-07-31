# -*- coding:utf-8 -*-
# author yuzuo.yz 2017/7/31 16:09

TP_TEST = 1
TP_STR = "MOD1"


def add_tp():
    print 'this is mod1'


class TpJop(object):
    def __init__(self, name):
        self.name = name

    def do_add(self):
        print self.name, ' is adding'
