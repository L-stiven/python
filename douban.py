# import requests
# from lxml import etree
# import json
#
# class DoubanSpider:
#
#     def __init__(self):
#         self.temp_url = 'https://movie.douban.com/top250?start={}'
#         self.headers={
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
#         }
#
#     def sendRequest(self,url):
#         headers = self.headers
#         respones = requests.get(url, headers=headers)
#         htmlStr = respones.content.decode()
#         ele = etree.HTML(htmlStr)
#         itemList = ele.xpath("//div[@class='item']")
#         return itemList
#
#     def savaData(self,content):
#         with open('douban.txt','a',encoding='utf-8') as f:
#             f.write(json.dumps(content,ensure_ascii=False))
#             f.write("\n")
#
#     # 主要逻辑
#     def run(self):
#         num = 0
#         a = 10
#         # 每次25条数据 循环10次
#         while a>0:
#             # 1开始运行的地址
#             start_url = self.temp_url.format(num)
#             # 发送请求，获取响应
#             print(start_url)
#             itemList = self.sendRequest(start_url)
#             movieInfo = {}
#             # 提取数据 遍历list
#             for item in itemList:
#                 movieInfo['title'] = item.xpath(".//div[@class='hd']/a/span[@class='title']/text()")[0]
#                 movieInfo['star'] = item.xpath(".//div[@class='bd']/p/text()")[0].replace(" ", "").replace("\n","")
#                 movieInfo['type'] = item.xpath(".//div[@class='bd']/p/text()")[1].replace(" ", "").replace("\n","").replace("\xa0", "")
#                 movieInfo['score'] = item.xpath(".//div[@class='star']/span[@class='rating_num']/text()")[0]
#                 movieInfo['comment'] = item.xpath(".//div[@class='star']/span/text()")[1]
#                 movieInfo['desc'] = item.xpath(".//p[@class='quote']/span/text()")[0]
#                 # 保存
#                 self.savaData(movieInfo)
#
#             # 构造下一页的url  循环2-5
#             num += 25
#             a -= 1
#
# if __name__ == '__main__':
#     douban = DoubanSpider()
#     douban.run()

print(["10月{}日".format(i) for i in range(1,10)])

