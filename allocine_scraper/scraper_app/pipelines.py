from sqlalchemy.orm import sessionmaker
from .models import Movies, db_connect, create_movies_table

class AllocineMoviesPipeline(object):
    'Allocine movies pipeline for storing scraped items in the database'
    def __init__(self):
        'Initializes database connection and sessionmaker, creates movies table'
        engine = db_connect()
        create_movies_table(engine)
        self.Session = sessionmaker(bind=engine)
        print("I'm in init in pipeline")

    def process_item(self, item, spider):
        'Save movies in db.This method is called for every item pipeline component.'
        print("I'm here")
        session = self.Session()
        movie = Movies(**item)
        session.add(movie)
        session.commit()
        return item