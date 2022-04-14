import sqlite3
import cache

def buildDatabase():
    conn = sqlite3.connect('./database/db.sqlite')
    cur = conn.cursor()

    ### games_info
    CREATE_TABLE_GAMES = '''CREATE TABLE IF NOT EXISTS games
    (id INT NOT NULL PRIMARY KEY, name TEXT NOT NULL, slug TEXT, released TEXT,
    rating REAL, metacritic INT, 
    ratings_count INT, reviews_count INT, added INT)'''
    cur.execute(CREATE_TABLE_GAMES)

    INSERT_TABLE_GAMES = '''INSERT OR REPLACE INTO games
    VALUES (?,?,?,?,?,?,?,?,?)
    '''

    ### games_tags
    CREATE_TABLE_GAMES_TAGS = '''CREATE TABLE IF NOT EXISTS games_tags
    (id INT NOT NULL, name TEXT NOT NULL, slug TEXT, tag_id INT NOT NULL)
    '''
    cur.execute(CREATE_TABLE_GAMES_TAGS)
    INSERT_TABLE_GAMES_TAGS = '''INSERT OR REPLACE INTO games_tags
    VALUES (?,?,?,?)
    '''

    ### games_platforms
    CREATE_TABLE_GAMES_PLATFORMS = '''CREATE TABLE IF NOT EXISTS games_platforms
    (id INT NOT NULL, name TEXT NOT NULL, slug TEXT, platform_id INT NOT NULL)'''
    cur.execute(CREATE_TABLE_GAMES_PLATFORMS)

    INSERT_TABLE_GAMES_PLATFORMS = '''INSERT OR REPLACE INTO games_platforms
    VALUES (?,?,?,?)
    '''

    ### tags
    CREATE_TABLE_TAGS = '''CREATE TABLE IF NOT EXISTS tags
    (id INT NOT NULL PRIMARY KEY, name TEXT NOT NULL, 
    language TEXT, games_count INT)'''
    cur.execute(CREATE_TABLE_TAGS)

    INSERT_TABLE_TAGS = '''INSERT OR REPLACE INTO tags
    VALUES (?,?,?,?)
    '''

    ### platforms
    CREATE_TABLE_PLATFORMS = '''CREATE TABLE IF NOT EXISTS platforms
    (id INT NOT NULL PRIMARY KEY, name TEXT NOT NULL)'''
    cur.execute(CREATE_TABLE_PLATFORMS)

    INSERT_TABLE_PLATFORMS = '''INSERT OR REPLACE INTO platforms
    VALUES (?,?)
    '''

    games = cache.open_cache('/Users/changli/Desktop/SI 507/cache_card_games.json') # games is a list

    ### part1: platforms
    platforms = []
    for x in games:
        if x.get('parent_platforms'):
            for p in x['parent_platforms']:
                platforms.append([p['platform']['id'], p['platform']['name']])
        else:
            pass
    _platforms = []
    for insert_data in platforms:
        if insert_data not in _platforms:
            _platforms.append(insert_data)
            cur.execute(INSERT_TABLE_PLATFORMS, insert_data)
    print("[DATABASE]->insert:              [YES]-> '" + 'platforms' + "'")
    ### part1: platforms
    conn.commit()

    ### part2: tags
    tags = []
    for x in games:
        if x.get('tags'):
            for p in x['tags']:
                tags.append([p['id'],p['name'],p['language'],p['games_count']])
        else:
            pass
    _tags = [] # remove the duplicates
    for insert_data in tags:
        if insert_data not in _tags:
            _tags.append(insert_data)
            cur.execute(INSERT_TABLE_TAGS, insert_data)
    print("[DATABASE]->insert:              [YES]-> '" + 'tags' + "'")
    ### part2: tags
    conn.commit()

    ### part3: games_tags
    for x in games:
        if x.get('tags'):
            for i in x['tags']:
                if i['language'] == 'eng':
                    # print(x['name'], i['name'])
                    insert_data = [x['id'], x['name'], x['slug'], i['id']]
                    cur.execute(INSERT_TABLE_GAMES_TAGS,insert_data)
                else:
                    pass
        else:
            pass
    print("[DATABASE]->insert:              [YES]-> '" + 'games_tags' + "'")
    ### part3: games_tags
    conn.commit()

    ### part4: games_platforms
    for x in games:
        if x.get('parent_platforms'):
            for i in x['parent_platforms']:
                    insert_data = [x['id'], x['name'], x['slug'], i['platform']['id']]
                    cur.execute(INSERT_TABLE_GAMES_PLATFORMS, insert_data)
        else:
            pass
    print("[DATABASE]->insert:              [YES]-> '" + 'games_platforms' + "'")
    ### part4: games_platforms
    conn.commit()


    ### part5: games
    for x in games:
        if x.get('id') and x.get('name'):
            insert_data = [
                x.get('id'),
                x.get('name'),
                x.get('slug'),
                x.get('released'),
                x.get('rating'),
                x.get('metacritic'),
                x.get('ratings_count'),
                x.get('reviews_count'),
                x.get('added')
            ]
            cur.execute(INSERT_TABLE_GAMES, insert_data)
        else:
            pass
    print("[DATABASE]->insert:              [YES]-> '" + 'games' + "'")
    ### part5: games
    conn.commit()
    conn.close()