base_url = input('Input a url:')
# base_url = 'https://m.xbiquge.cc/book_23793/15039526.html'
# base_url = base_url.split("/")
print(base_url)

print(base_url.split('/')[0]+'//'+base_url.split('/')[2])
print(base_url.split('/')[0]+'//'+base_url.split('/')[2]+'/'+base_url.split('/')[3]+'/')
