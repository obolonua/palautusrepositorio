import unittest

from player import Player
from statistics_service import StatisticsService


class StubPlayerReader:
    def __init__(self, players):
        self._players = players

    def get_players(self):
        return self._players


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        players = [
            Player("Mikko Rantanen", "DAL", 32, 56),
            Player("Sebastian Aho", "CAR", 29, 45),
            Player("Aleksander Barkov", "FLA", 20, 51),
            Player("Roope Hintz", "DAL", 28, 39),
        ]

        self.stats = StatisticsService(StubPlayerReader(players))

    def test_search_loytaa_pelaajan_nimen_osalla(self):
        player = self.stats.search("Rantanen")

        self.assertEqual(player.name, "Mikko Rantanen")

    def test_search_palauttaa_none_kun_pelaajaa_ei_loydy(self):
        player = self.stats.search("Teemu Selanne")

        self.assertIsNone(player)

    def test_team_palauttaa_vain_halutun_joukkueen_pelaajat(self):
        players = self.stats.team("DAL")

        self.assertEqual(
            [player.name for player in players],
            ["Mikko Rantanen", "Roope Hintz"],
        )

    def test_team_palauttaa_tuntemattomalla_joukkueella_tyhjan_listan(self):
        players = self.stats.team("EDM")

        self.assertEqual(players, [])

    def test_top_palauttaa_pelaajat_pistejarjestyksessa(self):
        players = self.stats.top(3)

        self.assertEqual(
            [player.name for player in players],
            ["Mikko Rantanen", "Sebastian Aho", "Aleksander Barkov"],
        )

    def test_top_palauttaa_pyydetyn_maaran_pelaajia(self):
        players = self.stats.top(2)

        self.assertEqual(len(players), 2)
