#coding=utf-8
import re
import json
import requests
import time
from bs4 import BeautifulSoup
from qiniu import Auth
from utility import QiniuTool, clean_html, content_word_count
from get_news_list import ListReader


class TencentCrawler():
    def __init__(self):
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        # self.qiniutool = QiniuTool()
        self.forbidden_imgs = ['http://mat1.gtimg.com/finance/cj/2.png',
                               'http://inews.gtimg.com/newsapp_match/0/365444796/0',
                               'http://img1.gtimg.com/stock/pics/hv1/208/178/2179/141735073.png',
                               'http://img1.gtimg.com/stock/pics/hv1/51/163/2177/141601041.jpg']    # 腾讯logo图
        self.trusted_media = [u'腾讯财经',u'腾讯证券',u'腾讯娱乐',u'腾讯体育',u'腾讯汽车']


    def get_news_info(self,url):
        if ('v.qq.com' in url): # 视频新闻直接丢弃
            return None

        try:
            response = requests.get(url=url, headers=self.headers)
        except:
            return None

        # gb2312编码转utf-8
        if(re.findall('meta.+?charset=.*?gb2312"', response.text)):
            html = response.content.decode('gb2312', 'ignore')
            print "html:::1::::",html
        else:
            html = response.content.decode('utf-8', 'ignore')
            print "html:::2::::", html
        soup = BeautifulSoup(html, "lxml")

        # 获取新闻频道
        try:
            channel = re.findall('site_cname:\'(.+?)\'', html, flags=re.S)[0]
        except:
            channel = ''

        # 获取新闻来源
        try:
            source = soup.find(name='span',attrs={'bosszone':'jgname'}).get_text()
            # 来源及频道过滤
            # if(source not in self.trusted_media and u'新闻' not in channel and u'数码' not in channel
            #    and u'体育' not in channel and u'时尚' not in channel):
            #     return None
        except Exception as e:
            print(e)
            return None

        try:
            real_media_source = soup.find(name='span',class_='a_source').find(name='a').get_text()
        except:
            real_media_source = '腾讯网'

        # 获取标题
        try:
            title = re.findall('title:\'(.+?)\',',html,flags=re.S)[0]
            title = re.sub('&nbsp;',' ',title)
            title = re.sub('&amp;','&',title)
        except:
            return None

        # 获取新闻发布日期
        try:
            pub_date = soup.find(name='span',class_='a_time').get_text()
        except:
            pub_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))

        # 获取正文内容
        try:
            content = soup.find_all(name='div', id='Cnt-Main-Article-QQ')[0].prettify()
            print "内容：：：",content
        except:
            return None
        soup = BeautifulSoup(content, "html.parser")
        print "---------------------------"
        print "内容：：：", soup
        gallery_tag = soup.find(name='div',class_='gallery',id='Gallery')
        if(gallery_tag is not None):    # 包含图集类新闻直接丢弃
            return None

        # 去除特殊标签
        script_tags = soup.find_all(name='script')
        [script_tag.decompose() for script_tag in script_tags]
        style_tags = soup.find_all(name='style')
        [style_tag.decompose() for style_tag in style_tags]
        try:
            soup.find(name='div',class_='rv-root-v2 rv-js-root').decompose()                    # video tag
            soup.find(name='div',class_='mbArticleSharePic                    ').decompose()    # share tag
            soup.find(name='div',id='cmenu').decompose()                                        # menu tag
            a_tags = soup.find_all(name='a')
            [a_tag.decompose() for a_tag in a_tags if 'href' in a_tag.attrs.keys() and 'v.qq.com' in a_tag['href']]
        except:
            pass

        # 处理图片
        img_tags = soup.find_all(name='img')
        cover_url = []
        for img_tag in img_tags:
            if (img_tag.parent.name == 'a'): # 去除带超链接的推广图
                img_tag.decompose()
                continue
            if(img_tag['src'] in self.forbidden_imgs):
                img_tag.decompose() # 去logo图
                continue

            try:
                # 获取图片后缀
                extension = img_tag['src'][img_tag['src'].rfind('.'):]
                if(len(extension) > 4):
                    extension = '.jpg'
            except:
                extension = '.jpg'

            # new_img_name = self.qiniutool.get_string_md5(img_tag['src']) + extension    # 上传图片
            # new_img_url = self.qiniutool.qiniu_sync(img_tag['src'],new_img_name)
            # # if(new_img_url):
            # #     if (len(cover_url) == 0 and 'gif' not in img_tag['src']): # 插入封面图
            # #         cover_url.append(new_img_url)
            # #     img_tag['src'] = new_img_url
            # #     attrs = [attr for attr in img_tag.attrs.keys()]
            # #     for attr in attrs:
            # #         if(attr != 'src'):
            # #             del img_tag[attr]
            # else:
            #     continue

        # 去除特殊html格式
        content = soup.prettify()
        content = re.sub(r'<!-- 相关视频 -->.+?<!-- /相关视频 -->', '', content, flags=re.S)
        content = re.sub('<!--\[if !IE\]><!-->.+?\[endif\]-->', '', content, flags=re.S)
        content = clean_html(content)
        # chu="（出自：%s）"  % real_media_source .decode("utf-8")
        # content = content +chu
        print "-----------------------------"
        print "内容：：：", content
        print "-------------------------------------"
        # cover_url、tags字段转JSON格式
        summary = title
        tags = json.dumps({'TAGS': []})
        cover_url = json.dumps({'S': cover_url})

        # 封装news并返回
        news = {'title': title, 'content': content, 'pub_date': pub_date, 'tags': tags, 'url': url,
                'cover_url': cover_url, 'summary': summary}
        return news



if __name__ == '__main__':
    # list_reader = ListReader()
    # tencent_crawler = TencentCrawler()
    # scrape_and_save('腾讯网', tencent_crawler, list_reader)
    url = 'http://tech.qq.com/a/20170508/026301.htm'
    url = 'http://sports.qq.com/a/20160323/015419.htm'
    crawler = TencentCrawler()
    news = crawler.get_news_info(url)
    if news is None:
        print 1
    else :print 2
    print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx----------------------"
    print(news['content'])



