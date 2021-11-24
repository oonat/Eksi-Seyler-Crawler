import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..items import Entry
from datetime import datetime
import locale

class EntrySpider(CrawlSpider):
    """ 
    Crawls the entries written under Eksi Seyler topics and writes them into an SQLite DB.
    """

    name = 'entry_spider'
    allowed_domains = ['seyler.eksisozluk.com']
    start_urls = ['https://seyler.eksisozluk.com']

    locale.setlocale(locale.LC_ALL, 'tr_TR.utf-8')

    rules = (

        # Extract links
        Rule(LinkExtractor(allow=('-')), callback='parse', follow=True),

        # Follow links
        Rule(LinkExtractor(allow=('\w*'))),
    )


    def parse(self, response):

        title = response.css('h1#title::text').get().strip()
        category = response.css('div.meta-category > a::text').get().strip()
        read_stat, share_stat = [i.strip() for i in response.css('div.meta-stats > b::text').getall()]
        date = response.css('span.meta-date::text').get()
        date = datetime.strptime(date.strip(), '%d %B %Y')

        entry_list = []

        for selector in response.css('div[id^=component]'):
            entry_list.append(' '.join(selector.css('*::text').getall()).strip())

        meta = response.css('div.content-seperator > a::attr(href)').getall()
        meta = [data.split('/')[-1] for data in meta]

        for i in range(len(entry_list)):
            item = Entry()
            item['nick'] = meta[2 * i]
            item['entry_id'] = int(meta[2 * i + 1])
            item['title'] = title
            item['entry_text'] = entry_list[i]
            item['date'] = date
            item['category'] = category
            item['read_stat'] = read_stat
            item['share_stat'] = share_stat
            yield item


