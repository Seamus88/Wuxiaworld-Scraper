# -*- coding: utf-8 -*-
import scrapy


class WuxiabotSpider(scrapy.Spider):
    name = 'wuxiabot'
    allowed_domains = ['www.wuxiaworld.com']
    #Input whatever link you want to start from into start_urls on Wuxiaworld
    #Multiple links can be added with , after each one.
    start_urls = ['https://www.wuxiaworld.com/novel/child-of-light/col-volume-5-chapter-9/']

    def parse(self, response):
    	SET_SELECTOR = '//div[@class="p-15"]'
    	for story in response.xpath(SET_SELECTOR):
            #Selects the Title
    		TITLE_SELECTOR = 'div h4 ::text'
            #Selects the Story paragraph by paragraph
    		STORY_SELECTOR = 'div p span ::text'
    		yield {
    		'title': story.css(TITLE_SELECTOR).extract_first(), 
    		'story': story.css(STORY_SELECTOR).extract()
    		}
        #Selects the next button
    	NEXT_PAGE_SELECTOR = '//li[@class="next"]//a/@href'
    	next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()
    	if next_page:
    		yield scrapy.Request(
    			response.urljoin(next_page),
    			callback=self.parse
    		)


