BOT_NAME = "allocine"
SPIDER_MODULES = ['scraper_app.spiders']
DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': 'almanook',
    'database': 'allocine_scrape'
}
ITEM_PIPELINES = {'scraper_app.pipelines.AllocineMoviesPipeline':100}