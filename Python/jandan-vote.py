import requests


'''
不知道脚本是否能用..
因为即便我在用浏览器进行正常投票操作时, 刷新后投票数还是和原来一样

'''



h = {
'Host' : 'jandan.net',
'Referer' : 'http://jandan.net/pic',
'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36 ',
'Accept-Encoding' : 'gzip,deflate,sdch',
'Connection' : 'keep-alive',
'X-Requested-With' : 'XMLHttpRequest',
'Accept-Language' : 'zh-CN,zh;q=0.8'
}



url = 'http://jandan.net/wp-admin/?acv_ajax=true&option=0&ID=2127901'



for one in range(25):
    r = requests.get(url, headers=h)
    print (r.text)
    




'''
# 这个脚本会返回请求头
test_url = 'http://localhost/!/Output-All-Request-Header.php'
r = requests.get(test_url, headers=h)
print (r.text)
'''





















