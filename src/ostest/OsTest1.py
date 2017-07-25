# -*- coding:utf-8 -*-
# author yuzuo.yz 2017/7/25 19:12

import os

print os.getcwd()
# window -> nt   linux -> posix
print os.name
# return a list include file and path name
print os.listdir("d:/")

print os.system("dir")