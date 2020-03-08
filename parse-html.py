import requests
import io
import sys
from bs4 import BeautifulSoup


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# r = requests.get("https://www.baidu.com");
# print(r.status_code)
# webHtml = r.text
## 先直接从本地获取
file = open('./test.html', 'r');
webHtml = file.read()
# print(webHtml)


# print(r.text)

parseHtmlSoup = BeautifulSoup(webHtml, 'lxml');
# print(parseHtmlSoup.a)
alist = parseHtmlSoup.find_all('a')
scriptList = parseHtmlSoup.find_all('script')
hrefList = [];
for scriptTag in scriptList:
    temp = scriptTag.attrs
    if 'href' in temp.keys():
        hrefList.append(temp['href'])

cssList = parseHtmlSoup.find_all('css')
for cssTag in cssList:
    temp = cssTag.attrs
    if 'link' in temp.keys():
        hrefList.append(temp['link']);
# print(alist[0]);
# print(alist[0].attrs);

# for a in alist:
    # b = a.attrs
    # hrefList.append(b['href'])
    # print(b['href'])
    # asoup = BeautifulSoup(a, 'lxml');
    # print(a.href)
print(hrefList);
# allScript = parseHtmlSoup.find_all('script')
# for scriptHtml in allScript:
#     print(scriptHtml)

