# -*- coding:utf-8 -*-
# author yuzuo.yz 2017/7/25 21:23
from urllib import urlencode

from pip._vendor import requests
from pip._vendor.requests.exceptions import RequestException


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
    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.text
        return None
    except RequestException, e:
        print "error!", e
    return None


def main():
    html = get_html()
    print html


if __name__ == '__main__':
    main();
