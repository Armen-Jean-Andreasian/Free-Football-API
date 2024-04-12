from data.competitions.competition_abs import AbstractCompetition


class FifaWorldCup(AbstractCompetition):
    abbr = "WC"
    name = "FIFA World Cup"
    location = "Worldwide"


class UefaChampionsLeague(AbstractCompetition):
    abbr = "CL"
    name = "UEFA Champions League"
    location = "Europe"


class UefaEuropaLeague(AbstractCompetition):
    abbr = "EC"
    name = "UEFA Europa League"
    location = "Europe"


class ComnebolCopaLibertadores(AbstractCompetition):
    abbr = "CLI"
    name = "CONMEBOL Copa Libertadores"
    location = "South America"


class SerieABrz(AbstractCompetition):
    abbr = "BSA"
    name = "Serie A"
    location = "Brazil"


class PremierLeagueEng(AbstractCompetition):
    abbr = "PL"
    name = "Premier League"
    location = "England"


class ChampionshipEng(AbstractCompetition):
    abbr = "ELC"
    name = "Championship"
    location = "England"


class Ligue1Fra(AbstractCompetition):
    abbr = "FL1"
    name = "Ligue 1"
    location = "France"


class Bundesliga1(AbstractCompetition):
    abbr = "BL1"
    name = "Bundesliga"
    location = "Germany"


class SerieAIta(AbstractCompetition):
    abbr = "SA"
    name = "Serie A"
    location = "Italy"


class Eredivisie(AbstractCompetition):
    abbr = "DED"
    name = "Eredivisie"
    location = "Netherlands"


class LigaPortugal(AbstractCompetition):
    abbr = "PPL"
    name = "LigaPortugal"
    location = "Portugal"


class LaLiga(AbstractCompetition):
    abbr = "PD"
    name = "La Liga"
    location = "Spain"
