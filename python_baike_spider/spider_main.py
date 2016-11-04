# coding:utf8
from python_baike_spider import html_downloader
from python_baike_spider import html_outputer
from python_baike_spider import html_parser
from python_baike_spider import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.number = 1000      # 爬取多少个记录

    def craw(self, url):
        count = 1
        self.urls.add_new_url(url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %sth: %s' % (count, new_url))
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == self.number:
                    break
                count += 1
            except Exception as e:
                print('There has error: %s' % e)
        self.outputer.output_html()


if __name__ == '__main__':
    # 开始的url
    url = 'http://baike.baidu.com/view/21087.htm'
    # 初始化
    obj_spider = SpiderMain()
    # 运行
    obj_spider.craw(url)