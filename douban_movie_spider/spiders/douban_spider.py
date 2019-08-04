#coding=utf-8
from scrapy import Request
from scrapy.spiders import Spider
from douban_movie_spider.items import DoubanMovieSpiderItem

class DoubanMovieTop250Spider(Spider):
    name = 'douban_movie_top250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://book.douban.com/top250?icn=index-book250-all'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = DoubanMovieSpiderItem()
        books = response.xpath('//div[@class="indent"]/table')
        for book in books:
            item['ranking'] = book.xpath('.//div[@class="pic"]/em/text()').extract()[0]
            item['movie_name'] = book.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = book.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            item['score_num'] = book.xpath('.//div[@class="star"]/span/text()').re(ur'(\d+)人评价')[0]
            yield item
