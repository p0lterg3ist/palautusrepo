import unittest

from player import Player
from statistics_service import StatisticsService


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_player(self):
        player = self.stats.search("Semenko")

        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Semenko")

    def test_search_returns_none_when_player_is_not_found(self):
        self.assertIsNone(self.stats.search("Not a player"))

    def test_team_returns_players_from_that_team(self):
        players = self.stats.team("EDM")

        self.assertEqual(
            [player.name for player in players],
            ["Semenko", "Kurri", "Gretzky"],
        )

    def test_team_returns_empty_list_when_team_has_no_players(self):
        self.assertEqual(self.stats.team("XXX"), [])

    def test_top_returns_requested_number_of_players(self):
        players = self.stats.top(2)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux"],
        )

    def test_top_returns_empty_list_when_zero_requested(self):
        self.assertEqual(self.stats.top(0), [])


if __name__ == "__main__":
    unittest.main()
