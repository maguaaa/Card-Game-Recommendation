import cache
import api
import decision_tree
from database import buildDatabase
from scraping import play

if __name__ == "__main__":

    cache.make_path()

    api.cache_games_json() # create './cache/games/cache_card_games.json'

    buildDatabase()

    decision_tree.tree_to_json() # create tree json file

    play()



