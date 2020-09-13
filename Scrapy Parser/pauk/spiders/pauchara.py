import scrapy
from datatime import datetime


class IMDbSpyder(scrapy.Spider):
    name = 'pauk'
    start_urls = ['https://www.imdb.com/search/title/?genres=thriller&explore=title_type,'
                  'genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e0da8c98-35e8-4ebd-8e86-e7d39c92730c&pf_rd_r'
                  '=F7XV4XEPWA2NAE1CN8BT&pf_rd_s=center-2&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr2_i_3', ]

    def parse(self, response):
        SET_SELECTOR = '//div[@class="lister-item mode-advanced"]'
        for i in response.xpath(SET_SELECTOR):
            yield {
                'title': i.xpath('.//h3/a/text()').extract_first(),

            }

    def __init__(self, name=None, **kwargs):
        self.start_time = datetime.now()

    def closed(self, response):
        self.ending_time = datetime.datetime.now()
        duration = self.ending_time - self.starting_time
        print(duration)



