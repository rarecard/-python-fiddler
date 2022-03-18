import requests

if __name__ == '__main__':
    # 头部信息，用来模拟浏览器发送请求
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip;q=1.0, compress;q=0.5',
        'Accept-Language': 'zh-Hans-CN;q=1.0',
        'User-Agent': 'Pupumall/2.9.0;iOS 14.4;D7CC2F22-7AA0-47B9-991E-44B33EA43CE6',
        'Connection': 'Keep-Alive',
        'Host': 'j1.pupuapi.com'
    }
    # json文件路径
    url = "https://j1.pupuapi.com/client/product/storeproduct/detail/7c1208da-907a-4391-9901-35a60096a3f9/b15e1173-1b43-4eb2-8055-b78cb4d3a033"
    # 存储json内容输出
    req = requests.get(url=url,headers=headers).json()
    print(req)
