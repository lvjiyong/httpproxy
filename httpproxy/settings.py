# -*- coding: utf-8 -*-

# 默认ip地址
IP_FILE = 'proxy_ip_addresses'


# 默认HEADER
HTTP_HEADER = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,en-US;q=0.8,en;q=0.5,zh;q=0.3',
    'Accept-Encoding': 'gzip, deflate'
}

# 爬取网页的代理
PROXY = ''

# 爬取网页超时时间
FETCH_TIMEOUT = 5

# 默认PING超时时间
PING_TIMEOUT = 2

# 确认http代理是否能正常访问某网页时的超时时间
HTTP_CHECK_TIMEOUT = 3

# IP文件默认代理,创建IP文件时,将自动添加至每个文件中,可以为空
DATA_DEFAULT_PROXY = ''




