from settings import ApiToken
from data import LaLiga
from src.parser import FootballDataOrgParser

api_token = ApiToken.reveal_token()
url = LaLiga.matches_url

response = FootballDataOrgParser.get(url=url, api_token=api_token)
result = response.json()

if __name__ == '__main__':
    from pprint import pprint
    pprint(result)
