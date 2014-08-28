# -*- coding: utf-8 -*-

# Scrapy settings for imdb project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'imdb'

SPIDER_MODULES = ['imdb.spiders']
NEWSPIDER_MODULE = 'imdb.spiders'

AUTOTHROTTLE_ENABLED = False
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#    'imdb.middlewares.ProxyMiddleware': 100,
#}

#PROXIES = [{'ip_port': '155.94.170.171:13228', 'user_pass': 'psyche_haha:scrapescrape'},
#           {'ip_port': '155.94.170.183:13228', 'user_pass': 'psyche_haha:scrapescrape'},
#           {'ip_port': '155.94.170.205:13228', 'user_pass': 'psyche_haha:scrapescrape'},
#           {'ip_port': '155.94.170.230:13228', 'user_pass': 'psyche_haha:scrapescrape'},
#           {'ip_port': '155.94.170.254:13228', 'user_pass': 'psyche_haha:scrapescrape'},
#           {'ip_port': '155.94.211.70:13228', 'user_pass': 'psyche_haha:scrapescrape'},
#           {'ip_port': '155.94.211.59:13228', 'user_pass': 'psyche_haha:scrapescrape'},
#           {'ip_port': '155.94.211.47:13228', 'user_pass': 'psyche_haha:scrapescrape'},
#           {'ip_port': '155.94.211.12:13228', 'user_pass': 'psyche_haha:scrapescrape'},
#           {'ip_port': '155.94.211.6:13228', 'user_pass': 'psyche_haha:scrapescrape'}]
#AUTOTHROTTLE_ENABLED = True
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'imdb (+http://www.yourdomain.com)'
