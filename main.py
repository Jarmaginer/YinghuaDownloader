import os
from urllib.request import Request, quote, unquote, urlopen
import urllib
import re
try:from bs4 import BeautifulSoup
except:os.system('pip install BeautifulSoup4')
try:from selenium import webdriver
except:os.system('pip install selenium')
import sys


title = 0
urls = []

vedioid = input("请输入樱花动漫id(例如http://www.yhdm.io/v/4423-1.html的id为4423)：")
start = int(input("开始下载的集数:"))
end = int(input("要下到的集数:"))
try:
        try:
                driver=webdriver.Chrome()
        except:
                driver=webdriver.Edge()
except:
        print("请先安装Chrome")

for i in range(start,end+1):
        htmlurl = "http://www.yhdm.io/v/"+str(vedioid)+"-"+str(i)+".html"

        driver.get(htmlurl)
        try:data = driver.page_source
        except:
                print("浏览器返回错误")
                os.system('pause')
                exit()
        
        soup = BeautifulSoup(data, 'lxml')

        targetcontext = re.findall(r"data-vid=.*mp4",str(soup))
        fcontext = "".join(targetcontext)
        a = re.findall(r'vid=http.*',fcontext)
        b = "".join(a)
        c = b.replace("vid=","")
        context = c.replace("$mp4","")
        if context == "":
                print("第"+str(i)+"集爬取失败")
        else:
                urls.append(context)
                print("第"+str(i)+"集爬取成功，url="+context)

driver.close()

def huidiao(block_num, block_size, total_size):
    sys.stdout.write('\r>> 正在下载第%s集 %.1f%%' % (str(title),
                     float(block_num * block_size) / float(total_size) * 100.0))
    sys.stdout.flush()


print("爬取完毕，开始下载")
for i in urls:
        title += 1
        aurl = unquote("".join(i), encoding='utf-8')
        try:urllib.request.urlretrieve(aurl, str(title) +".mp4" ,huidiao)
        except:print("\n第"+str(title)+"集下载失败"," 请求url="+aurl)


print("下载完成,任意键退出本程序")
os.system('pause')

