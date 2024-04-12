import requests


class Parser:
    @staticmethod
    def get(url: str, headers: dict) -> requests.Response:
        return requests.get(url, headers=headers)


class FootballDataOrgParser:
    @staticmethod
    def get(url: str, api_token: str) -> requests.Response:
        headers = {'X-Auth-Token': api_token}

        return Parser.get(url=url, headers=headers)
