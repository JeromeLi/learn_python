import re
# from termcolor import colored
# import backoff
from os import path, system, name, kill, getpid
from time import sleep
import requests
# from requests.exceptions import HTTPError
from lxml.html import document_fromstring


def remove_space_line(x):
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in x.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    y = '\n'.join(chunk for chunk in chunks if chunk)
    return y


def text_replace(string, substitutions):
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: substitutions[match.group(0)], string)


def add_title_fw():
    file_title = title.encode()
    write_to_file.write(file_title)
    title_return = '\n\n'
    file_title_return = title_return.encode()
    write_to_file.write(file_title_return)


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def nomore_page_close(y):
    if 'htm' not in y:
        write_to_file.close()
        print('No more chapter, stop to send request!')


replace_symbol_dict = {'-->>': ''}
ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
headers = {'user-agent': ua}
# base_url = 'https://m.piaotianzw.com/book_39768/12675326.html'
# base_url = 'https://m.xbiquge.cc/book_5019/3181318.html'
# base_url = 'https://m.xbiquge.cc/book_50449/33189706.html'
# base_url = 'https://m.xbiquge.cc/book_23793/15039526.html'
base_url = input('Input a url:')
x = 0
# Determine if the file name exists
for n in range(5):
    clear()
    global file_name
    file_name = input('Input a filename:')
    if not path.exists(file_name):
        break
    else:
        if n == 4:
            print('Are you kidding me?')
            print('Program is terminating.....')
            sleep(2)
            kill(getpid(), 9)
        print('The file name is existed! Please input another file name.')
        sleep(2)

while True:
    try:
        r = requests.get(base_url, headers=headers, timeout=10)
    except (requests.ConnectionError,
            requests.RequestException,
            requests.HTTPError,
            requests.Timeout,
            requests.TooManyRedirects):
        print('Connection Error! ReConnecting......')
        continue
    # r = requests_retry_session().get(base_url, headers=headers)
    # r = requests_retry_session().get('https://m.xbiquge.cc/book_5019/3181318.html')
    # print(r.status_code)
    # while r.status_code != 200:
    #     print('Time out! Retry......')
    #     sleep(3)
    #     r = requests.get(base_url, headers=headers)
    #     if r.status_code == 200:
    #         break
        # print(r.status_code)
    # break
    r.encoding = r.apparent_encoding
    doc = document_fromstring(r.text)
    # print(doc.xpath("//body[@id='nr_body']//h1")[0].text_content(),base_url)
    # title = remove_space_line(doc.xpath("//body[@id='nr_body']//h1")[0].text_content())
    title = remove_space_line(doc.xpath("//*[@id='nr_title']")[0].text_content())
    # content = remove_space_line(doc.xpath("//div[@id='nr']//div")[0].text_content())
    content = remove_space_line(doc.xpath("//*[@id='nr1']")[0].text_content())
    # print(doc.xpath("//div[@id='nr1']//center"))
    write_to_file = open(file_name, 'ab')
    if base_url.find('htm') == -1:
        write_to_file.close()
        print('No more chapters, closing file... done!')
        break
    else:
        if doc.xpath("//div[@id='nr1']//center"):
            next_click_text = remove_space_line(doc.xpath("//div[@id='nr1']//center")[0].text_content())
            # print(next_click_text)
            content = text_replace(content, {next_click_text: ''})
            content = text_replace(content, replace_symbol_dict)
            # print('Write Next Chapter!')
            add_title_fw()
            content = content[:-1]
            file_context = content.encode()
            write_to_file.write(file_context)
            # color_title = colored(title, 'red', attrs=['reverse', 'blink'])
            # color_content = colored(content, 'green')
            # print(color_title)
            # print()
            # print(content[:-1], end='')

        else:
            # if x == 0:
            #     # color_title = colored(title, 'red', attrs=['reverse', 'blink'])
            #     # print(color_title)
            #     add_title_fw()
            #     x += 1
            add_title_fw()
            file_context = content.encode()
            write_to_file.write(file_context)
            context_return = '\n\n\n\n'
            file_context_return = context_return.encode()
            write_to_file.write(file_context_return)
            # print(content)
            # print()
        print(title+' : '+base_url)
        # sleep(2)
        # print(text,base_url)
        # print(doc.xpath("//td[@class='next']//a")[1].get('href'))
        # if '/' in doc.xpath("//td[@class='next']//a")[1].get('href'):
        if '/' in doc.xpath("//*[@id='pb_next']")[0].get('href'):
            url_temp = base_url.split('/')[0] + '//' + base_url.split('/')[2]
            # base_url = 'https://m.xbiquge.cc' + doc.xpath("//td[@class='next']//a")[1].get('href')
            # base_url = url_temp + doc.xpath("//td[@class='next']//a")[1].get('href')
            base_url = url_temp + doc.xpath("//*[@id='pb_next']")[0].get('href')
            nomore_page_close(base_url)
        else:
            url_temp = base_url.split('/')[0]+'//'+base_url.split('/')[2]+'/'+base_url.split('/')[3]+'/'
            # base_url = 'https://m.xbiquge.cc/book_23793/' + doc.xpath("//td[@class='next']//a")[1].get('href')
            # base_url = url_temp + doc.xpath("//td[@class='next']//a")[1].get('href')
            base_url = url_temp + doc.xpath("//*[@id='pb_next']")[0].get('href')
            nomore_page_close(base_url)