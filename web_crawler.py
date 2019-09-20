import ssl
import time
import re
from bs4 import BeautifulSoup
import urllib.request


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
page_count = 100000
# base_url = 'https://m.piaotianzw.com/book_39768/20009610.html'
base_url = 'https://m.piaotianzw.com/book_39768/12675326.html'

for x in range(page_count):
    # time.sleep(1)
    req = urllib.request.Request(base_url)
    req.add_header = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0')
    html = urllib.request.urlopen(req, context=ssl._create_unverified_context()).read()
    write_to_file = open('./swzz.txt', 'ab')
    if base_url.find('htm') == -1:
        write_to_file.close()
        print('No more chapters, closing file... done!')
        break
    else:
        soup = BeautifulSoup(html, "html.parser")
        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()  # rip it out
        # get text
        text = soup.get_text()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines

        text = '\n'.join(chunk for chunk in chunks if chunk)
        text = text_replace(text, replace_text_dict_global)
        # file_context = text.encode()
        # filename_str = './' + str(x) + '.txt'
        # # print('filename:', filename_str)
        # file_handle = open(filename_str, 'wb')
        # file_handle.write(file_context)
        # file_handle.close()

        if text.find('继续阅读') != -1:
            text = text_replace(text, replace_text_dict_nextpage)
            text = re.sub(r'\b第.+?网\n', '', text, re.MULTILINE)
            # print(text, end='')
            file_context = text.encode()
            write_to_file.write(file_context)

        else:
            text = re.sub(r'\b第.+?\n', '', text, re.MULTILINE)
            text = re.sub(r'\b第.+?网\n', '', text, re.MULTILINE)
            file_context = text.encode()
            write_to_file.write(file_context)
            print('Insert new line')
            lr_insert='\n\n'
            file_context = lr_insert.encode()
            write_to_file.write(file_context)

    path_0 = re.findall(b'<a id="pb_next" href="(.+?)">', html)
    path_0_str = b''.join(path_0)
    path_0_str = path_0_str.decode()
    if path_0_str.find('/') != -1:
        path_split = re.split('/', path_0_str)
        path_final = path_split[2]
        next_page = 'https://m.piaotianzw.com/book_39768/' + path_final
        base_url = next_page
        print('Write ', path_final, ' chapter')
    else:
        next_page = 'https://m.piaotianzw.com/book_39768/' + path_0_str
        base_url = next_page
        print('Write ', path_0_str, ' chapter')
    time.sleep(2)
