import ssl
import time
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
page_count=10000
base_url='https://m.piaotianzw.com/book_39768/12675326.html'
for x in range(page_count):
    #time.sleep(1)
    html = urlopen(base_url, context=ssl._create_unverified_context())
    html_url = urlopen(base_url, context=ssl._create_unverified_context())
    #print(type(data))
    soup = BeautifulSoup(html, "html.parser")
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out
    html_temp = html_url.read()
    #print(type(html))
    path_0=re.findall(b'<a id="pb_next" href="(.+?)">',html_temp)
    #print(type(path_0))
    #print(path_0)
    path_0_str=b''.join(path_0)
    path_0_str=path_0_str.decode()
    if path_0_str.find('/') != -1:
        path_split=re.split('/',path_0_str)
        #print (path_split)
        path_final=path_split[2]
        #print(type(path_final))
        #print(path_final)
        next_page='https://m.piaotianzw.com/book_39768/'+path_final
        # print(next_page)
        base_url=next_page
    else:
        next_page='https://m.piaotianzw.com/book_39768/'+path_0_str
        # print(next_page)
        base_url=next_page

# get text
    text = soup.get_text()
# break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    text=text.replace('关灯\n','')
    text=text.replace('护眼\n','')
    text=text.replace('字体：\n','')
    text=text.replace('大\n','')
    text=text.replace('中\n','')
    text=text.replace('小\n','')
    text=text.replace('首页\n','')
    text=text.replace('书架\n','')
    text=text.replace('加入书签\n','')
    text=text.replace('返回目录\n','')
    text=text.replace('上一章\n','')
    text=text.replace('下一章\n','')
    text=text.replace('目录\n','')
    text=text.replace('上一页\n','')
    text=text.replace('下一页\n','')
    text=text.replace('电脑版\n','')
    text=text.replace('我的书架','')
    # print(type(text))
    if text.rfind('点击下一页') == -1:
        final_text = re.sub(r'\b第+?中文网\n\b', '', text, re.MULTILINE)
        final_text = re.sub(r'\b第.+?\n\b', '', final_text, re.MULTILINE)
        # print('chapter_end')
        print(final_text,end='')

    else:
        text = text.replace('\n-->>本章未完，点击下一页继续阅读\n', '')
        text = text.replace('-->>本章未完，点击下一页继续阅读\n', '')
        text = text.replace('\n>本章未完，点击下一页继续阅读\n', '')
        final_text = re.sub(r'\b第.+?中文网\b', '', text, re.MULTILINE)
        # final_text = re.sub(r'\b第.+?\n\b', '', final_text, re.MULTILINE)
        final_text = re.sub(r'^\n', '', final_text)
        # print('continue')
        print(final_text)
