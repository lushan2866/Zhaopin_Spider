# -*- coding: utf-8 -*-
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

'''
http://sou.zhaopin.com/jobs/searchresult.ashx?jl='%E5%8C%97%E4%BA%AC'&kw='%E9%94%80%E5%94%AE'&p=1&isadv=0
'''
from urllib import parse, request


def url():
    # Base url
    init_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx'

    # Dictionary fo query parameters
    parms = {
        'jl': '北京',
        'kw': '编辑',
        'page': 1
    }

    # Encoding the query string
    querystring = parse.urlencode(parms)

    # Make a POST request and read the response
    u = request.urlopen(init_url + '?' + querystring)
    resp = u.read().decode('utf-8')

    return resp

# test

# print(init_url)
# print(querystring)
# print(resp)
