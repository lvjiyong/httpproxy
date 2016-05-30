# -*- coding: utf-8 -*-

"""
爬取数据
"""

from __future__ import unicode_literals

import re

import requests
from configreset import logger

from httpproxy.settings import HTTP_HEADER, PROXY, FETCH_TIMEOUT


def find(response):
    """
    获取内容中的ip地址与端口
    :param response:
    :return:
    >>> import logging
    >>> logger.setLevel(logging.DEBUG)
    >>> len(find(requests.get(url='http://proxy.goubanjia.com/', headers=HTTP_HEADER)))>0
    True

    """
    logger.debug(response)

    html = re.sub(re.compile('</td>', re.I | re.M), ':</td>', response.text)
    html = re.sub(re.compile('<.*?>|\s', re.I | re.M), '', html)
    logger.debug(html)

    pattern = re.compile('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})', re.I | re.M)
    findall = re.findall(pattern, html)
    findall = ['%s:%s' % (ip[0], ip[1]) for ip in findall]

    findall = list(set(findall))

    logger.debug(findall)

    return findall or []


def fetch(url, headers=HTTP_HEADER, timeout=FETCH_TIMEOUT, find_fun=find, proxy=PROXY):
    """
    从网址中获取ip地址
    :param proxy:
    :param find_fun:
    :param headers:
    :param url:
    :param timeout:
    :return:

    >>> fetch('http://www.baidu.com')
    []

    # >>> len(fetch('http://www.kuaidaili.com/'))>0
    # True
    >>> len(fetch('http://proxy.goubanjia.com/', proxy='172.16.10.100:3128'))>0
    True
    >>> len(fetch(url='http://proxy.goubanjia.com/', timeout=5))>0
    True


    """
    logger.debug(url)
    try:
        if proxy:
            proxy = {'http': 'http://%s' % proxy}
        response = requests.get(url=url, proxies=proxy, headers=headers, timeout=timeout)
        return find_fun(response)

    except Exception as e:
        logger.error(e)
    return []


if __name__ == "__main__":
    import doctest

    doctest.testmod()
