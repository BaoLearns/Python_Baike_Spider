# coding:utf8


class HtmlOutputer(object):
    def __init__(self):
        # 保存抓取的数据
        self.datas = []
        # 输出文件名
        self.filename = 'output.html'

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fd = open(self.filename, 'w')
        fd.write("<html>")
        fd.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")
        fd.write("<body>")
        fd.write("<table>")
        fd.write("<tr>")
        fd.write("<td>ORDER</td>")
        fd.write("<td>URL</td>")
        fd.write("<td>TITLE</td>")
        fd.write("<td>SUMMARY</td>")
        fd.write("</tr>")
        count = 1
        for data in self.datas:
            fd.write("<tr>")
            fd.write("<td>%s</td>" % count)
            fd.write("<td>%s</td>" % data['url'])
            fd.write("<td>%s</td>" % data['title'])
            fd.write("<td>%s</td>" % data['summary'])
            fd.write("</tr>")
            count += 1
        fd.write("</table>")
        fd.write("</body>")
        fd.write("</html>")
        fd.close()