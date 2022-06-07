import bs4
import urllib.request, urllib.error
import xlrd
import re
import sqlite3

def main():
    baseurl = "http://movie.douban.com/top250?start="
    dataList = getData(baseurl)
    savepath = "./"
    saveData(savepath)

    askURL("http://movie.douban.com/top250?start=0")

def getData(baseurl):
    dataList = []
    for i in range(0,10):
        url = baseurl + str(i*25)
        html = askURL(url)

    return dataList

#得到指定一个url的网页内容
def askURL(url):
    head ={
        "User-Agent":
    "Mozilla / 5.0(Windows NT 10.0; Win64; x64;rv: 98.0) Gecko / 20100101 Firefox / 98.0"
    }
    requests = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(requests)
        html = response.read().decode("utf-8")

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html
#保存数据
def saveData(savepath):
    print()

if __name__ == '__main__':
    main()