# coding:utf8


class UrlManager(object):
    def __init__(self):
        # 保存还未爬取的url
        self.new_urls = set()
        # 保存已经爬取的url
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None or len(url) == 0:
            return
        # 添加
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        # 添加一些url
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        # 判断是否还有未爬取的url
        return len(self.new_urls) != 0

    def get_new_url(self):
        # 获取一个未爬取的url
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
