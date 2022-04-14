import sqlite3
import pandas as pd


def query_to_dataframe(decision_dict, user_choice):
    """match user choice to the decision tree and query relevant information

    Parameters
    ----------
    decision_dict: dictionary
        key: string of boolean path, value: muti-line string of sql query

    user_choice: string
        only composed of '1' or '0', four character

    Returns
    -------
    res: pd.DataFrame (1-5 rows)
    """
    conn = sqlite3.connect('./database/db.sqlite')
    cur = conn.cursor()

    try:
        query = decision_dict[user_choice]
    except KeyError:
        print("User choice is out of range and doesn't match the decision tree.")

    df = pd.read_sql_query(query, conn)[0:5] #initial recommendation table
    return df


def getKeyword(res):
    """get keyword from the initial recommendation for scraping the relevant games

    Parameters
    ----------
    res: pd.DataFrame
        the initial recommendation table

    Returns
    -------
    keyword: str
    """
    res["popular"] = res['ratings_count'] + res['reviews_count'] + res['added']
    res = res.sort_values(by='popular',ascending=False)
    kwlst = res.iloc[0]['slug'].split('-') ## a list of keywords
    keyword = max(kwlst, key=len)
    return keyword




