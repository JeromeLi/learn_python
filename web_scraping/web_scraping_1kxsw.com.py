import re
# from termcolor import colored
# import backoff
from os import path, system, name, kill, getpid
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from lxml.cssselect import etree, CSSSelector
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
# base_url = 'https://www.yeziwx.com/xiaoshuo/xiuluoshenzu/4859876.html'
# base_url = 'https://www.yeziwx.com/xiaoshuo/xiuluoshenzu/4863721.html'
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

# fireFoxOptions = webdriver.FirefoxOptions()
# fireFoxOptions.set_headless()
# brower = webdriver.Firefox(firefox_options=fireFoxOptions)
# brower.get('https://www.yeziwx.com/xiaoshuo/xiuluoshenzu/4859876.html')
# print(brower.page_source)

# instantiate a chrome options object so you can set the size and headless preference
savetofile = open(file_name, 'ab')

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36")
# prefs = {
# 'profile.default_content_setting_values': {
# 'images': 2,    # Disable Image load
# # 'javascript': 2 ##Disable JS
# }
# }
# chrome_options.add_experimental_option("prefs", prefs)
# chrome_options.add_argument("--headless") 
browser = webdriver.Chrome(options=chrome_options)
# browser.implicitly_wait(5) # Operation, get element waiting time
# browser.set_page_load_timeout(15) # page loading timeout 
browser.set_page_load_timeout(30)
# chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=chrome_options, executable_path='/usr/local/bin/chromedriver')
driver.get(base_url)
# lucky_button = driver.find_element_by_css_selector("[name=btnI]")
# lucky_button.click()


while True:
    
    if '上一' in driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/nav/ul").text:
        page_xpath = "/html/body/div[3]/div/div[3]/nav/ul/li[3]/a"
    else:
        page_xpath = "/html/body/div[3]/div/div[3]/nav/ul/li[2]/a"
    # result = EC.alert_is_present()(driver)
    print(driver.current_url, driver.title)
    try:
        next_page = driver.find_element_by_xpath(page_xpath+"[contains(text(),'下一')]")
    except:
        print('No more chapters, closing file... done!')
        savetofile.close()
        driver.close()
        driver.quit()
        break
    # else:
    #     print(type(next_page))
    #     print(next_page)
    #     driver.close()
    #     driver.quit()
    #     break
    #     if result:
    #         print (result.text)
    #         result.accept()
    #         print('No more chapters, closing file... done!')
    #         savetofile.close()
    #         driver.close()
    #         driver.quit()
    #         break
    else:
        print(driver.current_url, driver.title)
        html_title_str = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/h3/strong").text
        html_str = driver.find_element_by_xpath("//*[@id='contentText']").text
        if '(2)' in html_title_str:
            # text_byte = bytes(html_title_str,'utf-8')
            # savetofile.write(text_byte)
            # add_return = '\n\n'
            # add_return_byte = bytes(add_return, 'utf-8')
            # savetofile.write(add_return_byte)
            text_byte = bytes(html_str,'utf-8')
            savetofile.write(text_byte)
            add_return = '\n\n\n'
            add_return_byte = bytes(add_return, 'utf-8')
            savetofile.write(add_return_byte)
        else:
            html_str = text_replace(html_str, {'本章未完，点击“下一页”继续阅读':''})
            text_byte = bytes(html_title_str,'utf-8')
            savetofile.write(text_byte)
            add_return = '\n\n'
            add_return_byte = bytes(add_return, 'utf-8')
            savetofile.write(add_return_byte)
            html_str = html_str.rstrip('\n')
            text_byte = bytes(html_str,'utf-8')
            savetofile.write(text_byte)
        print ("continue...")
        driver.find_element_by_xpath(page_xpath+"[contains(text(),'下一')]").click()
        # base_url = driver.current_url
        # driver.close()

quit()

# html = etree.HTML(html_str)
# print(type(html))
# capture the screen
# driver.get_screenshot_as_file("capture.png")
# html = document_fromstring(driver.page_source)
# # print(html)
# print('\n\n\n\n')
# selector = etree.parse(html, etree.HTMLParser())
# print(selector)
# content_text =  html.xpath("//*[@id='htmlContent']")
# content_text = html.xpath("/html/body/div[2]/div[2]/div[2]/p[2]")
# content_text =  html.xpath("//*")
# # result = etree.tostring(content_text)
# print(type(content_text))
# print(len(content_text))
# print (str(content_text)[1:-1])
# print(content_text[0])
# for text in content_text:
#     print(text)

# # print(content_text[0])
# quit

# while True:
#     try:
#         r = requests.get(base_url, headers=headers, timeout=10)
#     except (requests.ConnectionError,
#             requests.RequestException,
#             requests.HTTPError,
#             requests.Timeout,
#             requests.TooManyRedirects):
#         print('Connection Error! ReConnecting......')
#         continue
#     # r = requests_retry_session().get(base_url, headers=headers)
#     # r = requests_retry_session().get('https://m.xbiquge.cc/book_5019/3181318.html')
#     # print(r.status_code)
#     # while r.status_code != 200:
#     #     print('Time out! Retry......')
#     #     sleep(3)
#     #     r = requests.get(base_url, headers=headers)
#     #     if r.status_code == 200:
#     #         break
#         # print(r.status_code)
#     # break
#     r.encoding = r.apparent_encoding
#     doc = document_fromstring(r.text)
#     # print(doc.xpath("//body[@id='nr_body']//h1")[0].text_content(),base_url)
#     title = remove_space_line(doc.xpath("/html/body/div[2]/div[2]/div[2]/p[1]")[0].text_content())
#     content = remove_space_line(doc.xpath("//*[@id='htmlContent']")[0].text_content())
#     # print(doc.xpath("//div[@id='nr1']//center"))
#     print('title:', title)
#     write_to_file = open(file_name, 'ab')
#     if base_url.find('htm') == -1:
#         write_to_file.close()
#         print('No more chapters, closing file... done!')
#         break
#     else:
#         if doc.xpath("//div[@id='nr1']//center"):
#             next_click_text = remove_space_line(doc.xpath("//div[@id='nr1']//center")[0].text_content())
#             # print(next_click_text)
#             content = text_replace(content, {next_click_text: ''})
#             content = text_replace(content, replace_symbol_dict)
#             # print('Write Next Chapter!')
#             add_title_fw()
#             content = content[:-1]
#             file_context = content.encode()
#             write_to_file.write(file_context)
#             # color_title = colored(title, 'red', attrs=['reverse', 'blink'])
#             # color_content = colored(content, 'green')
#             # print(color_title)
#             # print()
#             # print(content[:-1], end='')

#         else:
#             if x == 0:
#                 # color_title = colored(title, 'red', attrs=['reverse', 'blink'])
#                 # print(color_title)
#                 add_title_fw()
#                 x += 1

#             file_context = content.encode()
#             write_to_file.write(file_context)
#             context_return = '\n\n\n\n'
#             file_context_return = context_return.encode()
#             write_to_file.write(file_context_return)
#             # print(content)
#             # print()
#         print(title+' : '+base_url)
#         # sleep(2)
#         # print(text,base_url)
#         # print(doc.xpath("//td[@class='next']//a")[1].get('href'))
#         if '/' in doc.xpath("//td[@class='next']//a")[1].get('href'):
#             url_temp = base_url.split('/')[0] + '//' + base_url.split('/')[2]
#             # base_url = 'https://m.xbiquge.cc' + doc.xpath("//td[@class='next']//a")[1].get('href')
#             base_url = url_temp + doc.xpath("//td[@class='next']//a")[1].get('href')
#             nomore_page_close(base_url)
#         else:
#             url_temp = base_url.split('/')[0]+'//'+base_url.split('/')[2]+'/'+base_url.split('/')[3]+'/'
#             # base_url = 'https://m.xbiquge.cc/book_23793/' + doc.xpath("//td[@class='next']//a")[1].get('href')
#             base_url = url_temp + doc.xpath("//td[@class='next']//a")[1].get('href')
#             nomore_page_close(base_url)