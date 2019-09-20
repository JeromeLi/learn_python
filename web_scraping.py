import requests
from lxml import etree

ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
headers = {'user-agent': ua}
base_url = 'https://m.piaotianzw.com/book_39768/12675326.html'
r = requests.get(base_url, headers=headers)
r.encoding = r.apparent_encoding
print(type(r.text))
root = etree.XML('''r.text''')
print(root.xpath('/html/body/div/div[3]/div'))
