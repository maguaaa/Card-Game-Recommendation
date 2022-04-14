
import requests
import secrets
import json
import cache


## request all Card games
def rawg_all_games(url, games_list=[]):
    """Request all game pages and cache

    Parameters
    ----------
    url: url
    games_list: default empty list

    Returns
    -------
    games_list: list
    """
    while True:
        if not 'key=' in url:
            params = {"key":secrets.api_key}
            response = requests.get(url, params)
        else:
            response = requests.get(url)
        result = response.json()
        games_list += result["results"]
        next_url = result["next"]
        print(next_url)
        print(len(games_list), f'{int(len(games_list)/20)} page(s) done')

        if next_url is None:
            return games_list

        # elif '&page=3' in next_url: # for test, to stop after page 2
        #     return games_list

        else:
            print('***recursion***')
            url = next_url

def cache_games_json():
    games_list = rawg_all_games("https://api.rawg.io/api/games?genres=card")
    cache.save_cache(games_list, './cache/games/cache_card_games.json')


# games_list = rawg_all_games("https://api.rawg.io/api/games?genres=card")
# cache.save_cache(games_list, 'cache_card_games.json')



#dict_keys(['id', 'slug', 'name', 'released', 'tba', 'background_image', 
# 'rating', 'rating_top', 'ratings', 'ratings_count', 
# 'reviews_text_count', 'added', 'added_by_status', 
# 'metacritic', 'playtime', 'suggestions_count', 'updated', 
# 'user_game', 'reviews_count', 'saturated_color', 'dominant_color', 
# 'platforms', 'parent_platforms', 'genres', 
# 'stores', 'clip', 'tags', 'esrb_rating', 'short_screenshots'])




