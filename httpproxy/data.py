# -*- coding: utf-8 -*-

"""
存储与更新数据
"""
import os

from configreset import logger

IP_FILE = 'proxy_ip_addresses'


def append(ip_addresses, ip_file=IP_FILE):
    """
    增加IP地址
    :param ip_file:
    :param ip_addresses:
    :return:

    >>> import logging
    >>> logger.setLevel(logging.DEBUG)
    >>> clear()
    >>> append(['127.0.0.1:80'])
    >>> append(['127.0.0.2:80'])
    >>> append(['127.0.0.3:80'])
    >>> append(['127.0.0.1:80'])
    >>> append(['127.0.0.2:80'])
    >>> append(['127.0.0.3:80'])
    >>> len(all_ips())
    3

    >>> clear()
    """
    data = all_ips(ip_file) or []
    for ip_address in ip_addresses:
        if ip_address not in data:
            data.append(ip_address)

    logger.debug(ip_file)

    with open(ip_file, 'wb') as f:
        f.write('\n'.join(data) or '')


def remove(ip_addresses, ip_file=IP_FILE):
    """
    删除IP地址
    :param ip_file:
    :param ip_addresses:
    :return:
    >>> clear()
    >>> append(['127.0.0.1:80'])
    >>> append(['127.0.0.2:80'])
    >>> append(['127.0.0.3:80'])
    >>> len(all_ips())
    3
    >>> remove(['127.0.0.1:80'])
    >>> all_ips()
    ['127.0.0.2:80', '127.0.0.3:80']

    >>> clear()
    """
    data = all_ips()
    for ip_address in ip_addresses:
        if ip_address in data:
            data.remove(ip_address)

    with open(ip_file, 'wb') as f:
        f.write('\n'.join(data))


def clear(ip_file=IP_FILE):
    """
    清除所有数据
    :return:
    >>> clear()
    >>> append(['127.0.0.1:80'])
    >>> len(all_ips())
    1
    >>> clear()
    >>> os.path.exists()
    False

    """
    if os.path.exists(ip_file):
        os.remove(ip_file)


def all_ips(ip_file=IP_FILE):
    """

    :param ip_file:
    :return:

    >>> clear()
    >>> all_ips()
    []

    >>> append(['127.0.0.1:80'])
    >>> append(['127.0.0.2:80'])
    >>> append(['127.0.0.3:80'])
    >>> len(all_ips())
    3

    >>> clear()

    """
    if os.path.exists(ip_file):
        with open(ip_file, 'rb') as f:
            data = f.read().split('\n')
    else:
        data = []
    return data
