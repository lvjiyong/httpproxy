# -*- coding: utf-8 -*-

"""
缓存数据
"""

from __future__ import unicode_literals

import random

from configreset import logger

from httpproxy import data
from httpproxy.settings import IP_FILE

ALL_IP_ADDRESS = {}


def all_ip(ip_file=IP_FILE):
    """
    获取指定文件的所有ip
    :param ip_file:
    :return:
    >>> all_ip()
    []
    >>> append_ips(['127.0.0.1:80'])
    >>> append_ips(['127.0.0.1:81'])
    >>> ip_data = all_ip()
    >>> ip_data.sort()
    >>> [str(ip) for ip in ip_data]
    ['127.0.0.1:80', '127.0.0.1:81']

    >>> ip_test = 'ip_test'
    >>> all_ip(ip_test)
    []
    >>> append_ips(['127.0.0.1:80'], ip_test)
    >>> append_ips(['127.0.0.1:82'], ip_test)
    >>> ip_data = all_ip(ip_test)
    >>> ip_data.sort()
    >>> [str(ip) for ip in ip_data]
    ['127.0.0.1:80', '127.0.0.1:82']
    >>> clear_ip()
    >>> clear_ip(ip_test)
    """

    global ALL_IP_ADDRESS
    if ip_file not in ALL_IP_ADDRESS:
        ALL_IP_ADDRESS[ip_file] = data.all_ips(ip_file)
    return ALL_IP_ADDRESS[ip_file]


def append_ips(ips, ip_file=IP_FILE):
    """
    增加IP至指定文件
    :param ips:
    :param ip_file:
    :return:
    >>> all_ip()
    []
    >>> append_ips(['127.0.0.1:80'])
    >>> append_ips(['127.0.0.1:81'])
    >>> len(all_ip())
    2
    >>> clear_ip()
    """
    _clear_ips_cache(ip_file)
    data.append(ips, ip_file)


def remove_ips(ips, ip_file=IP_FILE):
    """
    从指定文件中移除IP
    :param ips:
    :param ip_file:
    :return:
    >>> all_ip()
    []
    >>> append_ips(['127.0.0.1:80'])
    >>> append_ips(['127.0.0.1:81'])
    >>> len(all_ip())
    2
    >>> remove_ips(['127.0.0.1:80'])
    >>> [str(ip) for ip in all_ip()]
    ['127.0.0.1:81']
    >>> clear_ip()

    """

    _clear_ips_cache(ip_file)
    data.remove(ips, ip_file)
    if not all_ip(ip_file):
        clear_ip(ip_file)


def clear_ip(ip_file=IP_FILE):
    """
    清除IP文件
    :param ip_file:
    :return:
    """
    _clear_ips_cache(ip_file)
    data.clear(ip_file)


def rand_ip(ip_file=IP_FILE):
    """
    随机获取一个IP
    :return:

    >>> import logging
    >>> logger.setLevel(logging.DEBUG)
    >>> clear_ip()
    >>> rand_ip()
    >>> append_ips(['127.0.0.1:80'])
    >>> append_ips(['127.0.0.2:80'])
    >>> append_ips(['127.0.0.3:80'])
    >>> '127.0.0' in rand_ip()
    True
    >>> clear_ip()

    """
    ips = all_ip(ip_file)
    logger.debug(ips)
    if ips:
        return random.choice(ips)


def _clear_ips_cache(ip_file=IP_FILE):
    """
    清除缓存
    :param ip_file:
    :return:
    """
    global ALL_IP_ADDRESS
    if ip_file in ALL_IP_ADDRESS:
        del ALL_IP_ADDRESS[ip_file]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
