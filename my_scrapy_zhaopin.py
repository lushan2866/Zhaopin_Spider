#编程目标：按照一定关键字对智联的岗位进行分析，量化。

__author__ = 'Ls'
# -*- coding:utf-8 -*-
import urllib,urllib.request,urllib.parse,re,time
page= '1'
sou_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%BC%96%E8%BE%91&p='+page+'&isadv=0'
visited=[]
job_url=[]

#######通过request获取网页原始内容######
def read_html(url):
    print('正在抓取网页')
    try:
        x = urllib.request.urlopen(url).read().decode('utf-8')
    except Exception as e:
        print('抓取错误，输入错误代码，再次尝试')
        print(e)
        time.sleep(3)
        x = urllib.request.urlopen(url).read().decode('utf-8')
    return x

#######利用正则表达式获取抓取网址的，并判断是否已经爬取过######
def find_out(the_read_url):
    linkre = re.compile('http://jobs.zhaopin.com/.\d*?.htm')# 正则表达式，需要每次不同时候都调整
    #x=linkre.findall(the_read_url)
    #return x
    for x in linkre.findall(the_read_url):
        if  x not in visited:
         job_url.append(x)
         print('加入队列 --->  ' + x)

#######利用正则表达式获取职位名称、职位信息等######
def find_job():

find_out(read_html(sou_url))
print(job_url)



