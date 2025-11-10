import requests
from player import Player

class PlayerReader:
    BASE_URL = "https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    def __init__(self, season):
        self.season = season
        self.players = self.get_players()

    def get_players(self):
        url = self.BASE_URL.format(season=self.season)
        response = requests.get(url).json()
        return [Player(p) for p in response]