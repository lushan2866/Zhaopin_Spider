# -*- coding: utf-8 -*-
# @Date    : 2016-03-13 16:45:44
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

from urllib import request
from bs4 import BeautifulSoup
from url import url
import re


# find all jobs
def parseurl(html):

    # test
    # html = url()

    soup = BeautifulSoup(html)
    # table = soup.findAll('div', id='newlist_list_content_table')
    # url regular expression
    job_re = re.compile(r'http://jobs.zhaopin.com/\d*.htm')
    # 返回a标签的set类型
    jobtags = soup.findAll(href=job_re)
    jobs = []

    # 提取job url
    for link in jobtags:
        jobs.append(link.get('href'))

    # print(jobs)
    return jobs


def parsejob(joburl):

    # 读取页面并解码
    resp = request.urlopen(joburl).read().decode('utf-8')
    # 读取位bs类型
    soup = BeautifulSoup(resp)

    # 定义job字典
    job_info = {
        'name': '',
        'salary': '',
        'work_exp': '',
        'edu': '',
        'info': '',
        'company': '',
        'url': joburl
    }
    # 寻找顶部信息
    job_title = soup.find(attrs={'class': 'inner-left fl'})
    job_info['name'] = job_title.h1.string
    job_info['company'] = job_title.h2.a.string

    # 寻找中间格式内容
    job_attr = soup.find(attrs={'class': 'terminal-ul clearfix'})
    for li in job_attr.findAll('li'):
        if '月薪' in li.span.string:
            job_info['salary'] = li.strong.string
        if '工作经验' in li.span.string:
            job_info['work_exp'] = li.strong.string
        if '最低学历' in li.span.string:
            job_info['edu'] = li.strong.string

    # 寻找职位描述
    job_content = soup.find(attrs={'class': 'tab-inner-cont'})
    # 遍历所有子元素, 获取text内容
    # 使用 .stripped_strings 去除多余空白内容
    string = []
    for div in job_content.stripped_strings:
        string.append(div)
    job_info['info'] = '\n'.join(string)

# test
# parseurl()
# parsejob('http://jobs.zhaopin.com/157322224250047.htm?ssidkey=y&ss=201&ff=03')
