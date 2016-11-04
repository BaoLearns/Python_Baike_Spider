# coding:utf8
from urllib import request


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        # 获取html
        response = request.urlopen(url)
        # 判断抓取是否成功，当状态码是200表示成功
        if response.getcode() != 200:
            return None
        return response.read()