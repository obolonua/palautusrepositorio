import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = self.get_players()

    def get_players(self):
        response = requests.get(self.url).json()
        return [Player(p) for p in response]