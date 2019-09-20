import re
import requests
from lxml.html import document_fromstring
from termcolor import colored

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

replace_symbol_dict = {'-->>': ''}
ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
headers = {'user-agent': ua}
base_url = 'https://m.piaotianzw.com/book_39768/12675326.html'
x = 0

while True:
    r = requests.get(base_url, headers=headers)
    r.encoding = r.apparent_encoding
    doc = document_fromstring(r.text)
    # print(doc.xpath("//body[@id='nr_body']//h1")[0].text_content(),base_url)
    title = remove_space_line(doc.xpath("//body[@id='nr_body']//h1")[0].text_content())
    content = remove_space_line(doc.xpath("//div[@id='nr']//div")[0].text_content())
    # print(doc.xpath("//div[@id='nr1']//center"))
    write_to_file = open('./swzz.txt', 'ab')
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
            if x == 0:
                # color_title = colored(title, 'red', attrs=['reverse', 'blink'])
                # print(color_title)
                add_title_fw()
                x += 1

            file_context = content.encode()
            write_to_file.write(file_context)
            context_return = '\n\n\n\n'
            file_context_return = context_return.encode()
            write_to_file.write(file_context_return)
            # print(content)
            # print()
        # print(title+' : '+base_url)
        # print(text,base_url)
        # print(doc.xpath("//td[@class='next']//a")[1].get('href'))
        if '/' in doc.xpath("//td[@class='next']//a")[1].get('href'):
            base_url = 'https://m.piaotianzw.com' + doc.xpath("//td[@class='next']//a")[1].get('href')
        else:
            base_url = 'https://m.piaotianzw.com/book_39768/' + doc.xpath("//td[@class='next']//a")[1].get('href')
