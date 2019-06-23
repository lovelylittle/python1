# 第一题
import requests
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url)
HTML = response.text
URLS = HTML.split('\n')
lines = HTML.split('\n')
for url in URLS:
    response = requests.get(url)
    content = response.content
    name = url.split('/')[-1]
    #写入本地
    with open(name,'wb') as f:
        f.write(content)




#第二题
#百度搜素三个关键字，然后存入本地，分别以res1.txt,res2.txt.res3.txt
#把res1中所有带有http的与https的提取出来
import requests
url = 'http://www.baidu.com/s?'
def baidu(wds):
    count = 1
    for wd in wds:
        res = requests.get(url,params={'wd':wd})
        path = 'res%d.txt'%count
        with open(path,'w',encoding='utf8') as f:
            f.write(res.text)
        count += 1
if __name__ == "__main__":
    wds = ('开心','加油','泡泡')
    baidu(wds)
url = 'http://www.baidu.com/s?wd=开心'
response = requests.get(url)
HTML = response.text    #res1如何定义
URLS = HTML.split('\n')
lines = HTML.split('\n')
for i in lines:
    if 'http://' in i or 'https://' in i:  
#        print(i)
        url = i.split('"')[1]
#        print(url)
        if 'http://' in url or 'https://' in url:     
            URLS.append(url)
#            print(URLS)
for url in URLS:
    response = requests.get(url)
    content = response.content
    name = url.split('/')[-1]
    #写入本地
    with open(name,'wb') as f:
        f.write(content)


