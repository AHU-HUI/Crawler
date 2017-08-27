import requests
import js2xml
from parsel import Selector

url = 'http://huaban.com/favorite//'
params = {
    'max': '',
    'limit': '10',
    'wfl': '1'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'application/json',
    'X-Request': 'JSON',
    'X-Requested-With': 'XMLHttpRequest'
}
'''
print("z.json", z.json())
print("z.json", id['pins'][0]['pin_id'])
'''


# 获取相册
def getpins():
    z = requests.get(url=url, params=params, headers=headers)
    id = z.json()
    for i in id['pins']:
        print(i['pin_id'])
    while True:
        last_pin_id = z.json()['pins'][-1]['pin_id']
        try:
            params['max'] = last_pin_id
            z = requests.get(url=url, params=params, headers=headers)
            for i in id['pins']:
                print(i['pin_id'])
                getimgsrc(i['pin_id'])

            last_pin_id = z.json()['pins'][-1]['pin_id']
        except:
            break


# 获取图片地址
def getimgsrc(pin_id):
    url = 'http://huaban.com/pins/%s/' % pin_id
    z = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
    sel = Selector(text=z.text)
    jscode = sel.xpath("//script[contains(., 'app.page = app.page')]/text()").extract_first()
    parsed_js = js2xml.parse(jscode)
    for i in parsed_js.xpath('//property[@name="pins"]//property[@name="key"]/string/text()'):
        print('http://img.hb.aicdn.com/' + i)
        downloadimg('http://img.hb.aicdn.com/' + i)


# 下载图片
def downloadimg(url):
    z = requests.get(url)
    imgname = url.split('/')[-1]
    with open('%s.jpg' % imgname, 'wb') as img:
        img.write(z.content)


if __name__ == '__main__':
    getpins()
