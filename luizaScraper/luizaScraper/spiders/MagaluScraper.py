import scrapy
from luizaScraper.items import LuizascraperItem

class MagaluScraper(scrapy.Spider):
    name = 'MagaluScraper'
    start_urls = ['http://magazineluiza.com.br/selecao/ofertasdodia']

    def parse(self, response):
        products =  response.css("div#__next h3::attr(title)").extract()
        desc_products = LuizascraperItem(desc = products)
        yield desc_products