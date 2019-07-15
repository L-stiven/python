import requests
from lxml import etree
import json

class BaiKeSpirder:

    #初始化
    def __init__(self):
        self.url = "https://www.qiushibaike.com/text/page/{}/"

    #发送请求方法
    def sendRequest(self,url):
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
        }
        respones = requests.get(url,headers=headers)
        htmlStr = respones.content.decode()
        return htmlStr

    #获取数据并处理
    def get_dataList(self,htmlStr):
        ele = etree.HTML(htmlStr)
        contList = ele.xpath("//div[@id='content-left']/div")
        return contList

    #保存段子
    def savehahah(self,content_list):
        with open("baike.txt","a",encoding="utf-8") as f:
            f.write(json.dumps(content_list,ensure_ascii=False))
            f.write("\n")
        # print("保存成功...")

    #主要逻辑
    def run(self):
        for i in range(1,14):

            # 1确定开始路径
            star_url = self.url.format(i)
            print(star_url)
            # 2发起请求 获取响应
            htmlStr = self.sendRequest(star_url)

            # 3提取数据
            contList = self.get_dataList(htmlStr)

            for div in contList:
                item = {}
                item["userName"] = div.xpath(".//div[@class='author clearfix']/a/h2/text()")[0].strip() if len(div.xpath(".//div[@class='author clearfix']/a/h2/text()")) > 0 else \
                div.xpath(".//div[@class='author clearfix']/span/h2/text()")[0].strip()
                item["content"] = div.xpath(".//div[@class='content']/span/text()")
                item["content"] = [i.strip() for i in item["content"]]
                item["hotComment"] = div.xpath(".//div[@class='main-text']/text()")[0].strip() if len(div.xpath(".//div[@class='main-text']/text()")) > 0 else None
                # 4保存
                self.savehahah(item)

if __name__ == '__main__':
    qiushibaike = BaiKeSpirder()
    qiushibaike.run()

