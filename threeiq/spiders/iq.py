import scrapy
from scrapy.selector import Selector
from selenium import webdriver
import time
from ..items import ThreeiqItem
#the code that actually pushes scraped data to Google Sheets lies in pipelines.py


class IqSpider(scrapy.Spider):
    name = 'iq'
    allowed_domains = ['ru.tradingview.com']
    start_urls = ['https://ru.tradingview.com/symbols/BCHUSD']

    def __init__(self):

        driver = webdriver.Chrome()
        driver.get("https://ru.tradingview.com/symbols/BCHUSD")
        time.sleep(2)
        self.html = driver.page_source


    def parse(self, response):
        resp = Selector(text=self.html)
        cash = ThreeiqItem()
        cash['Cashname'] = resp.xpath('//div[@class="tab-1APbKTGT tabSelected-b0SDOkCy"]/div[@class = "tabTitle-qQlkPW5Y"]/text()').get()
        cash['Cashvalue'] = resp.xpath('//div[@class="tab-1APbKTGT tabSelected-b0SDOkCy"]/div[@class = "tabValue-3iOTI9jm"]/text()').get()
        yield cash

