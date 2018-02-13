import time
import re
import sys
import re

import requests
import xlrd
from bs4 import BeautifulSoup
import json

headers = {'Referer': 'http://www.toutiao.com/',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
                            (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
          }

data_dir = 'tiyu/'

base_url = 'http://sports.163.com/special/00051CB5/tj09{page_num}.html'

tianjing = []
for i in range(1, 100):
    page_num = ''
    if i > 1:
        i_bit = len(str(i))
        page_num = '0' * (2 - i_bit) + str(i)
        page_num = '_'+ page_num
    url = base_url.format(page_num=page_num)
    
    response = requests.get(url=url, headers=headers)
    if not response:
        continue
    print("第 " + str(i) + " 页:", url)
    
    soup = BeautifulSoup(response.text, "lxml")
    news_list = soup.select('div[class="new_list"] div[class="news_item"] h3 > a')
    # print(news_list)
    for news in news_list:
        title = news.get_text()
        href = news.get("href")
        print(title, href)
        
        response_detail = requests.get(url=href, headers=headers)
        soup_detail = BeautifulSoup(response_detail.text, "lxml")
        for style in soup_detail.findAll('style'):
            style.decompose()
        for script in soup_detail.findAll('script'):
            script.decompose()
        
        content = soup_detail.select('div[class="post_content_main"] > div[class="post_body"] > div[class="post_text"] > p')
        content = [tag.get_text(strip=True) for tag in content]
        content = [text for text in content if text]
        content_str = "".join(content)
        content_str = re.sub(r'[\n\t\r]', r'', content_str)
        if not content_str:
            continue
        title_content = title + " " + content_str + "\n"
        tianjing.append(title_content)
        time.sleep(1)

    print("\n")

with open(data_dir + 'tianjing.txt', 'w', encoding='utf-8') as f:
    f.writelines(tianjing)
