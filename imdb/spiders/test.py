from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
 
class TestSpider(CrawlSpider):
    name = "test"
    domain_name = "whatismyip.com"
    # The following url is subject to change, you can get the last updated one from here :
    # http://www.whatismyip.com/faq/automation.asp
    start_urls = ["http://www.whatismyip.com/"]
 
    def parse(self, response):
    	set1 = response.xpath("//div[@class='the-ip']/label/text()").extract()
    	set2 = response.xpath("//div[@class='the-ip']/span/text()").extract()
        print set2
        print set1