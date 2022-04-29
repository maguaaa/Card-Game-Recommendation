
import json
import os

def open_cache(CACHE_FILENAME):
    ''' opens the cache file if it exists and loads the JSON into
    a dictionary, which it then returns.
    if the cache file doesn't exist, creates a new cache dictionary
    Parameters
    ----------
    None
    Returns
    -------
    The opened cache
    '''
    try:
        cache_file = open(CACHE_FILENAME, 'r')
        cache_contents = cache_file.read()
        cache_dict = json.loads(cache_contents)
        cache_file.close()
    except:
        cache_dict = {}
    return cache_dict

def save_cache(cache_dict, cache_filename):
    ''' saves the current state of the cache to disk
    Parameters
    ----------
    cache_dict: dict
        The dictionary to save
    Returns
    -------
    None
    '''
    dumped_json_cache = json.dumps(cache_dict)
    fw = open(cache_filename,"w")
    fw.write(dumped_json_cache)
    fw.close()


def make_path():
    if not os.path.exists(r'./cache/games'):
        os.makedirs(r'./cache/games')
    print("[CACHE]->make_path:              [YES]-> './cache/games'")

    if not os.path.exists(r'./cache/tree'):
        os.makedirs(r'./cache/tree')
    print("[CACHE]->make_path:              [YES]-> './cache/tree'")

    if not os.path.exists(r'./cache/scraping'):
        os.makedirs(r'./cache/scraping')
    print("[CACHE]->make_path:              [YES]-> './cache/scraping")

    if not os.path.exists(r'./cache/user_log'):
        os.makedirs(r'./cache/user_log')
    print("[CACHE]->make_path:              [YES]-> './cache/user_log'")

    if not os.path.exists(r'./database'):
        os.makedirs(r'./database')
    print("[CACHE]->make_path:              [YES]-> './cache/database'")
