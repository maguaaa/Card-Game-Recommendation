import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from decision_tree import buildDecisionTree
import sql_query
from user_interface import collect_answer_str
import secrets

def get_pagination(link,game,head):
    param = {
        'term': game,
        'page': 1,
    }

    req = requests.get(link, headers=head, params=param)
    soup = BeautifulSoup(req.content, 'html.parser')
    page_item = soup.find('div', 'search_pagination_right').find_all('a')

    try:
        total_item = int(page_item[4].getText())
    except Exception:
        pass
        try:
            total_item = int(page_item[3].getText())
        except Exception:
            pass
            try:
                total_item = int(page_item[2].getText())
            except Exception:
                pass
                try:
                    total_item = int(page_item[1].getText())
                except Exception:
                    pass
                    try:
                        total_item = int(page_item[0].getText())
                    except Exception:
                        pass
    return total_item


def scrap(link,game,head):
    count = 0
    data_list = []
    
    url=link
    game=game
    head=head


    for j in range(1, get_pagination(url,game,head)+1):
        if count == 100:
            break
        else:
            pass

        param = {
            'term': game,
            'page': j,
        }
        req = requests.get(link, params=param, headers=head)
        soup = BeautifulSoup(req.content, 'html.parser')

        content = soup.find('div', {'id': 'search_resultsRows'}).find_all('a')

        for i in content:
            url = i['href']
            title = i.find('div', 'col search_name ellipsis').getText().strip().replace('\n', ' ')

            try:
                price = i.find('div', 'col search_price responsive_secondrow').getText().strip()
            except Exception:
                price = 'discount from ' + i.find('span', {'style': 'color: #888888;'}).getText() + ' to ' + i.find('div', 'col search_price discounted responsive_secondrow').find('br').next_sibling.strip() + f" ({i.find('div', 'col search_discount responsive_secondrow').text.replace('-', '').strip()})"
            if price == '':
                price = 'none'

            release = i.find('div', 'col search_released responsive_secondrow').getText()
            try:
                release = datetime.strftime(datetime.strptime(release,'%b %d, %Y'),'%Y-%m-%d')
            except ValueError:
                pass
            except release == '':
                release = 'none'

            data = {
                'title': title,
                'price': price,
                'release': release,
                'link': url
            }
            data_list.append(data)

            count += 1
            print(f'【{count}】 {title} || {release} || {price} || {url}')
            if count == 100:
                break
            else:
                pass


    with open(f'resultfile/json_data_{game}.json', 'w+') as outfile:
        json.dump(data_list, outfile)

    print('Successful scraping! All data saved!')


def final_recommendation():
    """use scraping to give at most 100 recommendations

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    decision_dict = buildDecisionTree()
    user_choice = collect_answer_str()
    df_res = sql_query.query_to_dataframe(decision_dict,user_choice)
    keyword = sql_query.getKeyword(df_res)
    url = 'https://store.steampowered.com/search/results'
    head = {'cookie': secrets.sessionid}
    scrap(url,keyword,head)

