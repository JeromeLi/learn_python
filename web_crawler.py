import ssl
import time
import re
from bs4 import BeautifulSoup
import urllib.request
import copy


def text_replace(string, substitutions):
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: substitutions[match.group(0)], string)


replace_text_dict_global = {'关灯\n': '', '护眼\n': '', '字体：\n': '', '大\n': '', '中\n': '', '小\n': '', '首页\n': '',
                            '书架\n': '',
                            '加入书签\n': '', '返回目录\n': '', '上一章\n': '', '下一章\n': '', '目录\n': '', '上一页\n': '', '下一页\n': '',
                            '电脑版\n': '', '我的书架': ''}
replace_text_dict_nextpage = {'\n-->>本章未完，点击下一页继续阅读\n': '', '-->>本章未完，点击下一页继续阅读\n': '',
                              '\n>本章未完，点击下一页继续阅读\n': '', '>本章未完，点击下一页继续阅读\n': ''}
page_count = 10
base_url = 'https://m.piaotianzw.com/book_39768/37619656.html'

for x in range(page_count):
    # time.sleep(1)
    req = urllib.request.Request(base_url)
    req.add_header = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0')
    html = urllib.request.urlopen(req, context=ssl._create_unverified_context()).read()
    # print(type(html))
    #
    # print('write html context')
    # fhandle = open('./origin.html', 'wb')
    # fhandle.write(html)
    # fhandle.close()
    # break
    # html_url = copy.deepcopy(html)
    # print('write deepcopy context')
    # fhandle = open('./deepcopy.html', 'wb')
    # fhandle.write(html_url)
    # fhandle.close()
    path_0 = re.findall(b'<a id="pb_next" href="(.+?)">', html)
    # print(type(path_0))
    # print(path_0)
    path_0_str = b''.join(path_0)
    path_0_str = path_0_str.decode()
    if path_0_str.find('/') != -1:
        path_split = re.split('/', path_0_str)
        # print (path_split)
        path_final = path_split[2]
        # print(type(path_final))
        # print(path_final)
        next_page = 'https://m.piaotianzw.com/book_39768/' + path_final
        # print(next_page)
        base_url = next_page
    else:
        next_page = 'https://m.piaotianzw.com/book_39768/' + path_0_str
        # print(next_page)
        base_url = next_page

    # print('write deepcopy context after path process')
    # fhandle = open('./deepcopy_path.html', 'wb')
    # fhandle.write(html_url)
    # fhandle.close()

    soup = BeautifulSoup(html, "html.parser")
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out
    # html_temp = html_url.read()
    # print(type(html))
    # print('write html context after soup process')
    # fhandle = open('./origin_soup.html', 'wb')
    # fhandle.write(html)
    # fhandle.close()

    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines

    text = '\n'.join(chunk for chunk in chunks if chunk)
    text = text_replace(text, replace_text_dict_global)
    file_context = text.encode()
    filename_str = './' + str(x) + '.txt'
    # print('filename:', filename_str)
    file_handle = open(filename_str, 'wb')
    file_handle.write(file_context)
    file_handle.close()
    # text = text.replace('关灯\n', '')
    # text = text.replace('护眼\n', '')
    # text = text.replace('字体：\n', '')
    # text = text.replace('大\n', '')
    # text = text.replace('中\n', '')
    # text = text.replace('小\n', '')
    # text = text.replace('首页\n', '')
    # text = text.replace('书架\n', '')
    # text = text.replace('加入书签\n', '')
    # text = text.replace('返回目录\n', '')
    # text = text.replace('上一章\n', '')
    # text = text.replace('下一章\n', '')
    # text = text.replace('目录\n', '')
    # text = text.replace('上一页\n', '')
    # text = text.replace('下一页\n', '')
    # text = text.replace('电脑版\n', '')
    # text = text.replace('我的书架', ''), '\n-->>本章未完，点击下一页继续阅读\n': '', '-->>本章未完，点击下一页继续阅读\n': '',
    #                      '\n>本章未完，点击下一页继续阅读\n': '', '>本章未完，点击下一页继续阅读\n': ''
    # print(type(text))
    if text.find('继续阅读') != -1:
        text = text_replace(text, replace_text_dict_nextpage)
        text = re.sub(r'\b第.+?网\n\b', '', text, re.MULTILINE)
        # print('chapter_end')
        print(text, end='')
    else:
        text = re.sub(r'\b第.+?网\n\b', '', text, re.MULTILINE)
        text = re.sub(r'\b第.+?\n\b', '', text, re.MULTILINE)
        # text = text.replace('\n-->>本章未完，点击下一页继续阅读\n', '')
        # text = text.replace('-->>本章未完，点击下一页继续阅读\n', '')
        # text = text.replace('\n>本章未完，点击下一页继续阅读\n', '')
        # text = text.replace('>本章未完，点击下一页继续阅读\n', '')

        # final_text = re.sub(r'\b第.+?\n\b', '', final_text, re.MULTILINE)
        # final_text = re.sub(r'^\n', '', final_text)
        # print('continue')
        print(text)