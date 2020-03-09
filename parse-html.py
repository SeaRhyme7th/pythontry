import requests
import io
import sys
from bs4 import BeautifulSoup
import requests

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# r = requests.get("https://www.baidu.com");
# print(r.status_code)
# webHtml = r.text
## 先直接从本地获取
# file = open('./test.html', 'r');
# webHtml = file.read()
# print(webHtml)
curlUrl = 'https://www.huya.com/688';
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


### 可以先将需要存储的js和css的资源存放到当前的目录中

staticResourceFileName = "./tmp.txt";
staticResourceFile = open(staticResourceFileName, "w");

# start our request for these resource
for urlList in hrefList:
    staticResourceFile.write(urlList + "\n")
    # 先解析下应该保存的文件的名字
    res = requests.get(urlList)
    if res.status_code == 200 :
        resourceTxt = res.text
        if '?' in urlList :
            # 暂时不知道咋搞
            fileName = 'tmp';
        else :
            splitUrl = urlList.split('/', -1);
            if len(splitUrl) > 0 :
                data = requests.get(urlList)
                fileName = splitUrl[-1]
                resourceFile = open(fileName, 'w');
                resourceFile.write(data.text)
            # fileName = splitUrl.pop
            # print(fileName)
        # resourceFile = open(fileName, 'w');
        # print(resourceTxt, resourceFile);
        # resourceFile.close();
staticResourceFile.close();

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

