import cache
import api
from database import buildDatabase
from scraping import final_recommendation

if __name__ == "__main__":

    cache.make_path()

    api.cache_games_json() # create './cache/games/cache_card_games.json'

    buildDatabase()

    final_recommendation()

