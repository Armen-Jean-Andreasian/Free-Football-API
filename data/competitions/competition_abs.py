from abc import ABC
from data.competitions.api_source_urls import CompetitionsCore


class AbstractCompetition(ABC):
    """
    Available competitions
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
    """

    abbr: str
    name: str
    location: str

    competition_url: str
    matches_url: str

    def __init_subclass__(cls, **kwargs):
        """Dynamically assigning competition_url and matches_url for subclasses"""
        super().__init_subclass__(**kwargs)
        cls.competition_url = CompetitionsCore.get_competition_url(abbr=cls.abbr)
        cls.matches_url = CompetitionsCore.get_matches_url(abbr=cls.abbr)
