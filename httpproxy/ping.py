# -*- coding: utf-8 -*-

"""
检查数据
"""
from __future__ import unicode_literals

import re
import socket

import requests
from configreset import logger

from httpproxy.settings import PING_TIMEOUT, HTTP_CHECK_TIMEOUT


def http_check(url, match, proxy, headers=None, timeout=HTTP_CHECK_TIMEOUT):
    """
    确认是否可正常访问远程http网站

    :param headers:
    :param url:
    :param match:
    :param proxy:
    :param timeout:
    :return:

    >>> import logging
    >>> logger.setLevel(logging.DEBUG)
    >>> _url = 'http://1212.ip138.com/ic.asp'
    >>> _match = '172.16.102.213'
    >>> _proxy = '172.16.10.100:3128'
    >>> http_check(url=_url, match=_match, proxy=_proxy).status_code
    200
    """
    try:
        if proxy:
            proxy = {'http': 'http://%s' % proxy}
        logger.debug(proxy)
        response = requests.get(url=url, proxies=proxy, headers=headers, timeout=timeout)
        logger.debug(match in response.text)
        if re.search(re.compile(match), response.text):
            return response
    except Exception as e:
        logger.error(e)
        return None


def ping(ip_address, port, timeout=1):
    """
    ping ip_address及端口，如果返回0，则表示没有错误，接口可用
    :param ip_address:
    :param port:
    :param timeout:
    :return:

    >>> ping('220.181.57.217',80)
    0
    >>> ping('220.181.57.210',80)
    35

    """
    status = 35
    try:
        logger.debug('ping %s:%s' % (ip_address, port))
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cs.settimeout(float(timeout))
        address = (str(ip_address), int(port))
        status = cs.connect_ex(address)
        cs.close()

        logger.debug('ping %s:%s, status:%s' % (ip_address, port, status))

        return status
    except Exception as e:
        logger.error('ping %s:%s, status:%s:%s' % (ip_address, port, status, e))
        return 1


def pings(ip_addresses, timeout=PING_TIMEOUT):
    """
    twisted批量ping地址与端口
    :param ip_addresses:
    :param timeout:
    :return:

    >>> ip_addresses = ['220.181.57.217:80','127.1.0.1:80']
    >>> pings(ip_addresses)
    ['220.181.57.217:80']
    """
    pinged_addresses = []
    for ip in ip_addresses:
        ip_data = ip.split(':')
        result = ping(ip_data[0], ip_data[1], timeout)
        if result == 0:
            pinged_addresses.append(ip)

    return pinged_addresses


if __name__ == "__main__":
    import doctest

    doctest.testmod()
