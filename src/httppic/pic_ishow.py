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


# 入口页面请求
def get_html():

    index_param = ''
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }

    if pic_ishow_config.PAGE_INDEX == '' or pic_ishow_config.PAGE_INDEX == 1:
        pass
    else:
        index_param = '_' + pic_ishow_config.PAGE_INDEX

    # ishow
    # url = 'http://www.tuku.la/taotu/IShow/index' + index_param + '.html'

    # legbaby
    # url = 'http://www.tuku.la/siwa/legbaby/index_2.html'

    # aiss
    url = 'http://www.tuku.la/siwa/aiss/index' + index_param + '.html'

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


# 请求详情页内容
def get_art_detail(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.text
    except Exception, e:
        print "http request error!", e
        return None


# 获取列表页面中进入详情页的地址集合
def get_art_url(html):
    soup = BeautifulSoup(html, 'lxml')
    li_list = soup.find_all('li', class_='i_list list_n2')

    for li in li_list:
        art_url = li.a['href']
        yield art_url


# 获取详情页中的图片
def get_art_name_img(html):
    soup = BeautifulSoup(html, 'lxml')

    img = soup.select("img[border='000']")
    if img:
        origin_img_src = img[0]['src']
        img_src = pic_ishow_config.DOMAIN + origin_img_src
        download_img(img_src)
        a = img[0].parent
        if a and a.has_attr('href'):
            origin_href = a['href']
            if origin_href.endswith("html"):
                next_href = pic_ishow_config.DOMAIN + origin_href
                detail_html = get_art_detail(next_href)
                get_art_name_img(detail_html)


# 请求图片
def get_img_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
    except Exception, e:
        print "http request error!", e
        return None


# 下载图片
def download_img(url):
    content = get_img_content(url)
    if content:
        # md5转换，md5是hashlib包下
        file_name = md5(url).hexdigest() + ".jpg"
        local_name = pic_ishow_config.DOWNLOAD_PATH + '/' + file_name
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
        # if i >= 5:
        #     break
        # if i < 15:
        #     i = i + 1
        #     continue
        art_url = pic_ishow_config.DOMAIN + art_url
        print i, ":", art_url
        detail_html = get_art_detail(art_url)
        get_art_name_img(detail_html)
        i = i + 1


if __name__ == '__main__':
    main()
