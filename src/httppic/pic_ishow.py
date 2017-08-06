# -*- coding:utf-8 -*-
# author yuzuo.yz 2017/7/25 21:23
import re
from hashlib import md5
from multiprocessing import Pool
from urllib import urlencode

import os
import requests
import json

from bs4 import BeautifulSoup

import pic_config as config
import pic_ishow_config


def get_html():

    index_param = ''
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }

    if pic_ishow_config.PAGE_INDEX == '' or pic_ishow_config.PAGE_INDEX == 1:
        pass
    else:
        index_param = '_' + pic_ishow_config.PAGE_INDEX

    url = 'http://www.tuku.la/taotu/IShow/index' + index_param + '.html'

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print response.request.url
            return response.text
    except Exception, e:
        print "http request error!", e
        return None


def build_url(url, endpoint):
    return "/".join([url, endpoint])


def get_art_detail(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.text
    except Exception, e:
        print "http request error!", e
        return None


def get_art_url(html):
    soup = BeautifulSoup(html, 'lxml')
    li_list = soup.find_all('li', class_='i_list list_n2')

    for li in li_list:
        art_url = li.a['href']
        yield art_url


def get_art_name_img(html):
    soup = BeautifulSoup(html, 'lxml')

    p = soup.find_all('p', style='text-align: center;')
    # 多个需要再次处理
    if len(p) == 1:
        next_href = p[0].a['href']
        img_url = p[0].a.img['src']
        print next_href, img_url


def get_img_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
    except Exception, e:
        print "http request error!", e
        return None


def download_img(url):
    content = get_img_content(url)
    if content:
        # md5转换，md5是hashlib包下
        file_name = md5(url).hexdigest() + ".jpg"
        local_name = config.DOWNLOAD_PATH + '/' + file_name
        if not os.path.exists(local_name):
            with open(local_name, 'wb') as f:
                print "download..."
                f.write(content)


def print_json(data):
    return json.dumps(json.loads(data), indent=4)


def main():
    i = 0
    html = get_html()
    art_url_list = get_art_url(html)
    for art_url in art_url_list:
        if i >= 5:
            break
        art_url = pic_ishow_config.DOMAIN + art_url
        print art_url
        detail_html = get_art_detail(art_url)
        get_art_name_img(detail_html)
        i = i + 1
    #     for img_url in get_art_name_img(detail_html):
    #         if img_url:
    #             print img_url
    #             download_img(img_url)


if __name__ == '__main__':
    main()
