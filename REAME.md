# Free Football API

---

### The user-friendly interface to work with `Football data org API` 

- Contains all leagues that the source provides for a free plan. check ([competitions.py](data%2Fcompetitions%2Fcompetitions.py))
    - Available competitions:
      - FIFA World Cup

      - UEFA Champions League
      - UEFA Europa League
      - CONMEBOL Copa Libertadores

      - Bundesliga (Germany)
      - Eredivisie (Netherlands)
      - La Liga (Spain)
      - Ligue 1 (France)
      - Serie A (Brazil)
      - Championship (England)
      - Premier League (England)
      - Primeira Liga (Portugal)
      - Serie A (Italy)
      
- Will be extended to implement hands on solutions on all available methods provided by the Football data org API (check [api_source_urls.py](data%2Fcompetitions%2Fapi_source_urls.py))

# Features 

- Due to implementation, extending the competitions will be very easy. You just need to provide the credentials as follows, everything else will be automatically assigned. Example:
  ```python
  class MyNewCompetition(Competition):
    abbr = "CL"
    name = "UEFA Champions League"
    location = "Europe"
    ```


# Usage

1. Register an account at `football-data.org` and get an API token
2. In the project root create a `.env` file with the following structure:
   ```python
    api_key = 'my_api_key'
   ```
3. Ready to use.

---
It's a great API for your any kinds of apps, whether mobile, statistical, or games.

P.S. Check out the licence of `Football data org API` before implementing this into your project. 