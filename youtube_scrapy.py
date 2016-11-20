# $ scrapy runspider youtube_scrapy_crawler.py

import scrapy
import csv

class Youtube(scrapy.Spider):
    name = 'youtube_crawler'
    start_urls = ['https://www.youtube.com/results?search_query=']


    def parse(self, response):
    	query = raw_input()
    	query.replace(' ', '+')
    	scrapy.Request(response.urljoin(query))
        next_page = response.css('ol.item-section h3.yt-lockup-title > a ::attr(href)').extract_first()
        if next_page:
            a = scrapy.Request(response.urljoin(next_page), callback=self.parse_item(response, query))


    def parse_item(self, response, query):
    	subs = response.css("span.yt-subscription-button-subscriber-count-branded-horizontal.yt-subscriber-count ::attr(aria-label)").extract_first()
    	self.write_to_csv(query, subs)
    	return {'subscription': subs}

    def write_to_csv(self, query, value):
    	with open('subscription.csv', 'wb') as csvfile:
    		writer = csv.writer(csvfile, delimiter=',')
    		writer.writerow([query, value])
