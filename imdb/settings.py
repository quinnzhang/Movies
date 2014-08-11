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

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'imdb.middlewares.ProxyMiddleware': 100,
}

PROXIES = [{'ip_port': '204.130.130.197:8080'},
           {'ip_port': '23.19.133.100:7808'},
           {'ip_port': '204.12.235.23:8089'},
           {'ip_port': '8.225.195.209:8080'},
           {'ip_port': '66.85.131.18:8089'},
           {'ip_port': '216.189.101.102:7808'},
           {'ip_port': '23.19.133.100:8089'},
           {'ip_port': '209.203.212.4:3128'},
           {'ip_port': '66.85.131.18:7808'}]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'imdb (+http://www.yourdomain.com)'
