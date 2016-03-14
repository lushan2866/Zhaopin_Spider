# -*- coding: utf-8 -*-
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

from urllib import parse, request

# 将搜索关键字转码为对应url链接
'''
eg:
http://sou.zhaopin.com/jobs/searchresult.ashx?jl='%E5%8C%97%E4%BA%AC'&kw='%E9%94%80%E5%94%AE'&p=1&isadv=0
'''


def url(city, job, page):

    # Base url
    init_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx'

    # Dictionary fo query parameters
    parms = {
        'jl': '',  # city
        'kw': '',  # job
        'page': 1     # page
    }

    # init
    parms.update({
                 'jl': city,
                 'kw': job,
                 'page': page
                 })

    # Encoding the query string
    querystring = parse.urlencode(parms)

    # Make a POST request and read the response
    u = request.urlopen(init_url + '?' + querystring)

    return u

# test
# print(querystring)
# print(resp)
