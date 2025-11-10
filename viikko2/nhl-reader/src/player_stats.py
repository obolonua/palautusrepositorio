from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.players = reader.players

    def top_scorers_by_nationality(self, nationality):
        filtered = [p for p in self.players if p.nationality == nationality]
        filtered.sort(key=lambda p: p.points, reverse=True)
        return filtered