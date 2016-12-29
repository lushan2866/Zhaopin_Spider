#编程目标：按照一定关键字对智联的岗位进行分析，量化。

__author__ = 'Ls'
# -*- coding:utf-8 -*-
import urllib,urllib.request,urllib.parse,re,time

#######前期赋值######
page= '1'
sou_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%BC%96%E8%BE%91&p='+page+'&isadv=0'
visited=[]
job_url=[]

#######通过request获取网页原始内容，输入url,返回网页内容######
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

#######利用正则表达式获取抓取网址的，并判断是否已经爬取过，输入url内容，返回岗位-url######
def find_out(the_read_url):
    linkre = re.compile('http://jobs.zhaopin.com/.\d*?.htm')# 正则表达式，需要每次不同时候都调整
    #x=linkre.findall(the_read_url)
    #return x
    for x in linkre.findall(the_read_url):
        if  x not in visited:
         job_url.append(x)
         print('加入队列 --->  ' + x)

#######利用正则表达式获取职位名称、职位信息等,输入url_context,返回多项信息######
def find_job(url_context):
    linkre1=re.compile('(?<=<h1>).*?(?=</h1>)')# 正则表达式，需要每次不同时候都调整，此次是职位名称
    linkre2=re.compile('(?<=<li><span>职位月薪：</span><strong>).*?(?=</strong></li>)')# 正则表达式，需要每次不同时候都调整，此次是职位月薪
    linkre3=re.compile('(?<=<li><span>工作经验：</span><strong>).*?(?=</strong></li>)')# 正则表达式，需要每次不同时候都调整，此次是工作经验
    linkre4=re.compile('(?<=<li><span>最低学历：</span><strong>).*?(?=</strong></li>)')# 正则表达式，需要每次不同时候都调整，此次是最低学历
    linkre5=re.compile('''(?<=<!-- SWSStringCutStart -->).*?\s
                        .*?\s
                        (?=<!-- SWSStringCutEnd -->)''') #正则表达式，需要每次不同时候都调整，此次是职位描述
    linkre6=re.compile('(?<=var Str_CompName = ").*?(?=")')# 正则表达式，需要每次不同时候都调整，此次是公司名称
    linkre7=re.compile('(?<=<link rel="canonical" href=")http://jobs.zhaopin.com/.*?.htm(?=")') #正则表达式，需要每次不同时候都调整，此次是岗位链接
    job_name =linkre1.findall(url_context)
    the_salary = linkre2.findall(url_context)
    the_work_ex=linkre3.findall(url_context)
    the_edu=linkre4.findall(url_context)
    the_job_ifo=linkre5.findall(url_context)
    the_company=linkre6.findall(url_context)
    the_job_url=linkre7.findall(url_context)
    return (job_name,the_salary,the_work_ex,the_edu,the_job_ifo,the_company,the_job_url)

test_url= 'http://jobs.zhaopin.com/144793568250001.htm'

print(find_job(read_html(test_url)))


find_out(read_html(sou_url))
print(job_url)



