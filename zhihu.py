import requests
import time
import random
import json


# 获取数据
def Get_json(url, headers):
    req = requests.get(url=url, headers=headers).json().get('data')
    return req


# 处理数据
def screen_url(req):
    list = []
    for index in range(5):
        urlDict = {}
        urlDict['title'] = (req[index]['title'])
        urlDict['url'] = req[index]['url'].replace("api.zhihu.com/collections",
                                                   "www.zhihu.com/api/v4/collections") + "/items?offset=0&limit=20"
        list.append(urlDict)
    return list


if __name__ == '__main__':
    headers = {
        'Accept': '* / *',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'x-requested-with': 'x-requested-with',
        'Connection': 'keep-alive',
        'Host': 'www.zhihu.com'
    }
    url = "https://www.zhihu.com/api/v4/people/fei-chai-xi-xie-gui-29/collections?include=data%5B*%5D.updated_time%2Canswer_count%2Cfollower_count%2Ccreator%2Cdescription%2Cis_following%2Ccomment_count%2Ccreated_time%3Bdata%5B*%5D.creator.vip_info&offset=0&limit=20"
    req = requests.get(url=url, headers=headers).json().get('data')
    list1 = []
    list2=[]
    list = screen_url(Get_json(url, headers))

    for index in range(5):
        list_url = []
        str1 = list[index]['url']
        list_all = Get_json(str1, headers)
        for url in range(6):
            if 'question' in list_all[url]['content']:
                list_url.append(list_all[url]['content']['question']['title'])
            else:
                list_url.append(list_all[url]['content']['title'])
        list2.append(list_url)

    for index in range(5):
        list_url = []
        str1 = list[index]['url']
        list_all = Get_json(str1, headers)
        for url in range(6):
            list_url.append(list_all[url]['content']['url'])
        list1.append(list_url)

    # str1 = list[0]['url']
    # str2 = str1.replace("api.zhihu.com/collections", "www.zhihu.com/api/v4/collections")
    # test = Get_json(str1, headers)
    # # l=json.loads(req)
    # print(test[1]['content']['url'])
    for index in range(5):
        print("------------------分界线----------------")
        print(list[index]['title'])
        for i in range(6):
            print(list2[index][i])
            print(list1[index][i])
