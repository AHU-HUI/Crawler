# encoding: utf-8
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):  # 向管理器添加一个新url
        if not url:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):  # 向管理器批量添加url
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):  # 判断管理器是否存在待爬取url
        return len(self.new_urls) != 0

    def get_new_url(self):  # 从url管理器获取url
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        print('crawer:',new_url)
        return new_url
