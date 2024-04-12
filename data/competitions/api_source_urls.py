class CompetitionsCore:
    """
    Available interface
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

    competition_url = "https://api.football-data.org/v4/competitions/{abbr}/"
    matches_url = "https://api.football-data.org/v4/competitions/{abbr}/matches"

    @classmethod
    def get_competition_url(cls, abbr):
        return cls.competition_url.format(abbr=abbr)

    @classmethod
    def get_matches_url(cls, abbr):
        return cls.matches_url.format(abbr=abbr)