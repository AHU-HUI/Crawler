# encoding: utf-8
import codecs
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = codecs.open('output.html', 'w', encoding='utf-8')
        fout.write("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />")
        fout.write("<html>")
        fout.write("<body>")

        fout.write("<table border='1' cellpadding='16' cellspacing='1' bgcolor='#BBFFFF'>")
        i = 1
        for data in self.datas:
            # print data
            for each in data:
                print(each)
            fout.write("<tr>")
            fout.write("<td><CENTER>%s</CENTER></td>" % data['title'])
            fout.write("<td font-family=\"Microsoft YaHei\" >%s</td>" % (data['summary']))
            fout.write("<td><a href=%s target=\"_blank\">%s</a></td>"%(data['url'],data['url']))
            print(i)
            i = i + 1
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()