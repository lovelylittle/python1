#第一题
def function_little('wd')
{
    import urllib.request
    import urllib.parse
    data = urllib.parse.urlencode({'wd':'奋斗'})
    print(data)
    url = 'http://www.baidu.com/s?' + data
    response = urllib.request.urlopen(url)
    HTML = response.read().decode('utf8')
    print(HTML)
}


#第二题
def function_big('pw','acc')
{
    data = bytes(urllib.parse.urlencode({'pw':'123','acc':'456'}),enconding='utf8')
    url = 'http://httpbin.org/post'
    response = urllib.request.urlopen(url,data=data)
    result = response.read().decode('utf8')
    print(result)
}
