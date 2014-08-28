from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from imdb.items import ImdbItem
from scrapy.http import Request

class ImdbSpider(CrawlSpider):

    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['http://www.imdb.com/search/title?count=100&title_type=feature,tv_movie&ref_=nv_ch_mm_1']


    def start_requests(self):
        for i in range(0,1001):
            yield Request("http://www.imdb.com/search/title?at=0&count=100&sort=moviemeter,asc&start=" + str(100*i + 1) + "&title_type=feature,tv_movie", self.parse_movies)

    def parse_movies(self, response):
        movies_list = []
        for sel in response.xpath("//tr[@class='odd detailed' or @class='even detailed']"):
            movie = ImdbItem()
            movie['url'] = sel.xpath("td[@class='title']/a/@href").extract()
            movie['title'] = sel.xpath("td[@class='title']/a/text()").extract()
            movie['year'] = sel.xpath("td[@class='title']/span[@class='year_type']/text()").extract()
            movie['rating'] = sel.xpath("td[@class='title']/div[@class='user_rating']/div/span[@class='rating-rating']/span[@class='value']/text()").extract()
            movie['votes'] = sel.xpath("td[@class='title']/div[@class='user_rating']/div/@title").extract()
            movie['genre'] = sel.xpath("td[@class='title']/span[@class='genre']/a/text()").extract()
            movie['length'] = sel.xpath("td[@class='title']/span[@class='runtime']/text()").extract()
            movies_list.append(movie)
        return(movies_list)

