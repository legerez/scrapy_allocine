from scrapy.item import Item, Field

class AllocineMovies(Item):
    """Allocine container (dictionary-like object) for scraped movie data"""
    title = Field()
    date = Field()
    duration = Field()
    genre = Field()
    director = Field()
    summary = Field()
