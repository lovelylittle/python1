#第一题
#自己仿照多建几个代理，访问一个网站，如果，有状态码不是200，尝试更换代理继续访问
#当所以代理都测试完毕之后，依旧无法访问，打印该网站爬取失败
#构建代理
import urllib.request
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
proxy_handle = ({'http':'http://112.85.169.72:9999'},{'http':'http://149.176.96.134:9999'},{'http':'http://163.204.243.28:9999'},{'http':'http://122.193.245.44:9999'},{'http':'http://182.34.32.185:9999'})
#choice
#处理代理
#proxy = urllib.request.ProxyHandler(proxy_handle)
#构建代理
for proxy_handle in proxy_handle:
    try:
        opener = urllib.request.build_opener(proxy_handle)
        response = opener.open(proxy_handle)
        if response.status != 200:
            print('更换代理继续访问')
        else:
            print('该网站爬取成功')
    except:
            print('该网站爬取失败')
            


#第二题
#爬取该网站
import urllib.request
url = 'http://www.17k.com./chapter/2933095/36699279.htm1'
response = urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)








