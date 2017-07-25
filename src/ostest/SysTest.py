# -*- coding:utf-8 -*-
# author yuzuo.yz 2017/7/25 19:39
import sys


def which_mod(mod):
    print mod, " is coming"
    if mod in sys.builtin_module_names:
        print "a default sys module"
    else:
        mod = __import__(mod)
        print mod.__file__

which_mod("os")
which_mod("sys")
which_mod("string")