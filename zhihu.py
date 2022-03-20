import requests
import json


# 获取数据
def Get_json(url, headers):
    req = requests.get(url=url, headers=headers).json()
    return req


# 处理数据
def screen_url(req):
    data = json.dumps(req, indent=1,ensure_ascii=False)  # 输出到json文件
    f = open('favorite.json', 'w+',encoding="utf-8",newline='\n')
    f.write(data)
    req = req.get('data')
    list = []
    for index in range(5):
        urlDict = {}
        urlDict['title'] = (req[index]['title'])  # 存储收藏夹名称
        # 存储收藏夹对应内容连接，为了下一次使用该链接进行抓包，修改关键字
        urlDict['url'] = req[index]['url'].replace("api.zhihu.com/collections",
                                                   "www.zhihu.com/api/v4/collections") + "/items?offset=0&limit=20"
        list.append(urlDict)
    return list


def screen_content(list):
    list1 = []

    for index in range(5):
        list_url = []
        str1 = list[index]['url']  # 前面抓取的收藏夹对应链接
        list_all = Get_json(str1, headers).get('data')  # 使用收藏夹链接
        data = json.dumps(list_all, indent=1,ensure_ascii=False)  # 循环输出到json文件
        f = open(list[index]['title'] + '.json', 'w+',encoding="utf-8", newline='\n')
        f.write(data)
        # 循环查找收藏夹内对应的标题和链接
        for url in range(6):
            conDict = {}
            # 因为有些内容的标题在question中，所以要简单判断一下
            if 'question' in list_all[url]['content']:
                conDict['title'] = list_all[url]['content']['question']['title']
            else:
                conDict['title'] = list_all[url]['content']['title']
            conDict['url'] = list_all[url]['content']['url']
            list_url.append(conDict)
        list1.append(list_url)
    return list1


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

    list = screen_url(Get_json(url, headers))
    list1 = screen_content(list)
    # 循环输出需要的内容
    for i in range(5):
        print(list[i]['title'])
        for j in range(6):
            print(list1[i][j]['title'])
            print(list1[i][j]['url'])
