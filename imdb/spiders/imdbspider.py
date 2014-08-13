from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from imdb.items import ImdbItem


class ImdbSpider(CrawlSpider):

    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['http://www.imdb.com/search/title?count=100&title_type=feature&ref_=nv_ch_mm_1']
    rules = (
        # follow the next page link
        Rule(LinkExtractor(allow=['/search/title\?at=0&count=100&sort=moviemeter,asc&start+'])),

        # find all movie links and parse
        Rule(LinkExtractor(allow=['/title/tt\d+/']), callback='parse_movie')
        )
        

    def parse_movie(self, response):
        movie = ImdbItem()

        # put url into list
        url_list = []
        url_list.append(response.url)

        movie['url'] = url_list
        movie['title'] = response.xpath("//h1/span[@class='itemprop']/text()").extract()
        movie['year'] = response.xpath("//h1/span[@class='nobr']/a/text()").extract()
        movie['rating'] = response.xpath("//div[@class='titlePageSprite star-box-giga-star']/text()").extract()
        movie['genre'] = response.xpath("//div[@class='infobar']/a/span[@class='itemprop']/text()").extract()

        return movie
