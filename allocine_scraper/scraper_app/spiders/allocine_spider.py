from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose
from scraper_app.items import AllocineMovies
import re
from w3lib.html import replace_escape_chars

class AllocineSpider(Spider):
    """Spider for regularly updated allocine.fr/films site"""
    name = "allocine"
    allowed_domains = ["allocine.fr"]
    start_urls = ["http://www.allocine.fr/films"]

    movies_list_xpath = "//div[@class='card entity-card entity-card-list cf']"
    item_fields = {
        'title': './/a[@class="meta-title-link"]/text()',
        'date': './/span[@class="date"]/text()',
        'duration': './/div[@class="meta-body-item meta-body-info"]/text()',
        'genre': './/*[re:match(@class, ".*==$")]/text()',
        'director': './/a[@class="blue-link"]/text()',
        'summary': './/div[@class="content-txt "]/text()'
    }
    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        Testing contracts:
        @url http://www.allocine.fr/films
        @returns items
        @scrapes title

        """
        selector = Selector(response)

        # iterate over movies
        for movie in selector.xpath(self.movies_list_xpath):
            loader = ItemLoader(AllocineMovies(), selector=movie)

            # define processors
            loader.default_input_processor = MapCompose(lambda x: x.strip(',').split(), replace_escape_chars)
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.items():
                loader.add_xpath(field, xpath)
            yield loader.load_item()