import scrapy
from douban.items import DoubanItem


class MainSpider(scrapy.Spider):
    name = "main"
    # allowed_domains = ["www.baidu.com"]
    start_urls = ["https://movie.douban.com/top250?start=0&filter="]
    num = 0

    def parse(self, response):
        li_list = response.xpath('//ol[@class="grid_view"]/li')
        for li in li_list:
            item = DoubanItem()
            item['title'] = li.xpath('.//div[@class="hd"]/a/span[@class="title"]/text()').extract_first()
            item['author'] = \
                li.xpath('.//div[@class="bd"]/p/text()').extract()[0].strip().split('导演: ')[1].split(' ')[0]
            item['year'] = li.xpath('.//div[@class="bd"]/p/text()').extract()[1].strip().split('/')[0].strip()
            if '(' in item['year']:
                item['year'] = int(item['year'].split('(')[0])
            else:
                item['year'] = int(item['year'])
            item['country'] = li.xpath('.//div[@class="bd"]/p/text()').extract()[1].strip().split('/')[1].split(' ')[
                0].strip()
            item['type'] = li.xpath('.//div[@class="bd"]/p/text()').extract()[1].strip().split('/')[2].split(' ')[
                0].strip()
            item['score'] = float(li.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract_first())
            yield item
        if self.num < 100:
            self.num += 25
            yield scrapy.Request(url=f'https://movie.douban.com/top250?start={self.num}&filter=', callback=self.parse)
