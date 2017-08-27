# encoding: utf-8
from url_manager import UrlManager
from html_downloader import HtmlDownloader
from html_parser import HtmlParser
from html_outputer import HtmlOutputer


class SpiderMain(object):
    def __init__(self):
        self.urls = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.outputer = HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()  # 获取新url
                html_cont = self.downloader.download(new_url)  # 下载url内容
                new_urls, new_data = self.parser.parse(new_url, html_cont)  # 解析url内容
                self.urls.add_new_urls(new_urls)  # 将解析到的新url存入url管理器
                self.outputer.collect_data(new_data)  # 收集解析到的数据
                if count == 200:
                    break
                count = count + 1
            except:
                print("craw failed")
        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/%E5%93%B2%E5%AD%A6"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
