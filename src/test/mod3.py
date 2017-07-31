# -*- coding:utf-8 -*-
# author yuzuo.yz 2017/7/31 16:24

# 增加搜索模块路径的方法。给sys.path加上..，增加一个当前目录的上级目录的搜索
# sys.path是搜索模块路径列表。类似java的classpath
import sys
sys.path.append('..')
import testpackage.mod1 as mod1


def main():
    tp = mod1.TpJop('name')
    print tp.name


if __name__ == '__main__':
    main()
