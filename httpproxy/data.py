# -*- coding: utf-8 -*-

"""
存储与更新数据
"""

from __future__ import unicode_literals

import os

from configreset import logger

from httpproxy.settings import DATA_DEFAULT_PROXY


def append(ip_addresses, ip_file):
    """
    增加IP地址
    :param ip_file:
    :param ip_addresses:
    :return:

    >>> import logging
    >>> logger.setLevel(logging.DEBUG)
    >>> DEFAULT_PROXY = None
    >>> ip_file = 'test'
    >>> clear(ip_file)
    >>> append(['127.0.0.1:80'] ,ip_file)
    >>> append([''] ,ip_file)
    >>> append(['127.0.0.2:80'] ,ip_file)
    >>> append(['127.0.0.3:80'] ,ip_file)
    >>> append(['127.0.0.1:80'] ,ip_file)
    >>> append(['127.0.0.2:80'] ,ip_file)
    >>> append(['127.0.0.3:80'] ,ip_file)
    >>> len(all_ips(ip_file))
    3
    >>> os.path.exists(ip_file)
    True
    >>> clear(ip_file)

    """

    if ip_addresses:
        data = list((set(all_ips(ip_file)) | set(ip_addresses)) - {''})
        logger.debug(data)
        with open(ip_file, 'w') as f:
            f.write('\n'.join(data))


def remove(ip_addresses, ip_file):
    """
    删除IP地址
    :param ip_file:
    :param ip_addresses:
    :return:
    >>> ip_file = 'test'
    >>> clear(ip_file)
    >>> append(['127.0.0.1:80'] ,ip_file)
    >>> append(['127.0.0.2:80'] ,ip_file)
    >>> append(['127.0.0.3:80'] ,ip_file)
    >>> len(all_ips(ip_file))
    3
    >>> remove(['127.0.0.1:80'] ,ip_file)
    >>> ip_data = all_ips(ip_file)
    >>> ip_data.sort()
    >>> ip_data
    ['127.0.0.2:80', '127.0.0.3:80']

    >>> clear(ip_file)
    """
    if ip_addresses:
        data = set(all_ips(ip_file))
        data = list(data - set(ip_addresses))
        with open(ip_file, 'w') as f:
            f.write('\n'.join(data))


def clear(ip_file):
    """
    清除所有数据
    :return:
    >>> ip_file = 'test'
    >>> clear(ip_file)
    >>> append(['127.0.0.1:80'] ,ip_file)
    >>> len(all_ips(ip_file))
    1
    >>> clear(ip_file)
    >>> os.path.exists(ip_file)
    False

    """
    if os.path.exists(ip_file):
        os.remove(ip_file)


def all_ips(ip_file):
    """

    :param ip_file:
    :return:

    >>> ip_file = 'test'
    >>> clear(ip_file)
    >>> all_ips(ip_file)
    []
    >>> append(['127.0.0.1:80'],ip_file)
    >>> append(['127.0.0.2:80'],ip_file)
    >>> append(['127.0.0.3:80'],ip_file)
    >>> len(all_ips(ip_file))
    3

    >>> clear(ip_file)

    """
    logger.debug(DATA_DEFAULT_PROXY)
    if os.path.exists(ip_file):
        with open(ip_file, 'r') as f:
            data = f.read().split('\n')
    else:
        data = [DATA_DEFAULT_PROXY] if DATA_DEFAULT_PROXY else []
    return data


if __name__ == "__main__":
    import doctest

    doctest.testmod()
