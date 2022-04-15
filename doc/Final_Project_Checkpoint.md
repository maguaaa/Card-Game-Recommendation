# Project Code
- https://github.com/maguaaa/Card-Game-Recommendation

# Data Sources
## **Web API you haven’t used before that requires API key or HTTP Basic authorization ✣ (4pts)**
1. **Origin** :  [Documentation](https://api.rawg.io/docs/#tag/games) `GET https://api.rawg.io/api/games?genres=card Request`

2. **Format**: json

3. **Data accessing and caching**: Use API key and cache data as json files.

4. **Summary of data**
  - 4268 records retrieved
  <img src="./images/Screen Shot 2022-04-14 at 8.08.06 PM.png" alt="Screen Shot 2022-04-14 at 8.08.06 PM" style="zoom: 20%;" />
  
  - description of data
    
    - important fields:
    - "id": int, id of each game
    - "name": string, name of each game
    - "slug": string, lower case string connected by '-' between words
    - "rating": float, rating of each game 
    - "meatacritic": int, rating by Metacritic
    - "ratings_counts": int, the amount of ratings
    - "reviews_counts": int, the amount of reviews
    - "released": string, the date each game released at, (time format: %Y-%m-%d)
    - "parent_platforms": string, the parent platform of each game
    


