# -*- coding:utf-8 -*-
# author yuzuo.yz 2017/7/25 21:23
from urllib import urlencode

import requests


def get_html():
    data = {
        'offset': 0,
        'format': 'json',
        'keyword': '美女',
        'autoload': 'true',
        'count': 20,
        'cur_tab': 3
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    # try:
    response = requests.get(url)

    if response.status_code == 200:
        # c = response.json()['count'] 可以直接获取json中的数据
        # c = response.json()['count']
        # print "test count", c
        return response.text
    response.text
    # except , e:
    #     print "error!", e
    # return None


def main():
    html = get_html()
    print html


if __name__ == '__main__':
    main()
