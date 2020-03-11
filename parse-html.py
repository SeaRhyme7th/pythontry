import requests
import io
import sys
from bs4 import BeautifulSoup
import requests

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

curlUrl = 'http://vis-free.10jqka.com.cn/billboard/indexV3.html#/index';
allContent = requests.get(curlUrl);
webHtml = allContent.text;

parseHtmlSoup = BeautifulSoup(webHtml, 'lxml');
# print(parseHtmlSoup.a)
alist = parseHtmlSoup.find_all('a')
scriptList = parseHtmlSoup.find_all('script')
hrefList = [];
for scriptTag in scriptList:
    temp = scriptTag.attrs
    if 'src' in temp.keys():
        hrefList.append(temp['src'])
cssList = parseHtmlSoup.find_all('link')
for cssTag in cssList:
    temp = cssTag.attrs
    if 'href' in temp.keys():
        hrefList.append(temp['href']);


staticResourceFileName = "./tmp.txt";
staticResourceFile = open(staticResourceFileName, "w");

# start our request for these resource
filePath = {};
requestList = [];
for urlList in hrefList:
    staticResourceFile.write(urlList + "\n")
    # print(urlList.split("//", -1));
    urlParts = urlList.split("//", -1)
    if len(urlParts[0]) == 0 :
        urlList = "http:" + urlList
    # print(urlList)
    res = requests.get(urlList)
    if res.status_code == 200 :
        # print(urlList)
        resourceTxt = res.text
        if '?' in urlList :
            #http://s.thsi.cn/cb?/js/common/cefapi/1.5.4/cefApi.min.js;/js/common/b2c/ta/ta.min.js;/js/jsmodule/acme/1.1/acme.js;/js/datav/charts/0.4.15/d3_charts.js
            splitUrlList = urlList.split('?', -1);
            for partUrl in splitUrlList[1].split(";", -1):
                noHttpProtocol = splitUrlList[0].split("//", -1);# 去掉//以及协议头
                others = noHttpProtocol[1].split('/', -1);
                domain = noHttpProtocol[0] + "//" + others[0];
                completeUrl = domain + partUrl
                # find path in linux
                if "s.thsi.cn" in domain:
                    filePath[completeUrl] = "/var/www/s/html" + partUrl
                if "i.this.cn" in domain:
                    filePath[completeUrl] = "/var/www/i/html" + partUrl
                requestList.append(completeUrl)
                # print(completeUrl + "\n")
            # don't know how to do
            fileName = 'tmp';
        else :
            requestList.append(urlList);
            continue;

            # fileName = splitUrl.pop
            # print(fileName)
        # resourceFile = open(fileName, 'w');
        # print(resourceTxt, resourceFile);
        # resourceFile.close();
staticResourceFile.close();

## write to file
for sourceUrl in requestList:
    res = requests.get(sourceUrl)
    if res.status_code == 200:
            splitUrl = sourceUrl.split('/', -1);
            if len(splitUrl) > 0 :
                fileName = "./tmp/" + splitUrl[-1]
                print(fileName)
                resourceFile = open(fileName, 'w');
                resourceFile.write(res.text)
print(requestList)
print(filePath)
# print(alist[0]);
# print(alist[0].attrs);

# for a in alist:
    # b = a.attrs
    # hrefList.append(b['href'])
    # print(b['href'])
    # asoup = BeautifulSoup(a, 'lxml');
    # print(a.href)
# print(hrefList);
# allScript = parseHtmlSoup.find_all('script')
# for scriptHtml in allScript:
#     print(scriptHtml)

