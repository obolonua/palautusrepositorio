class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.nationality = dict['nationality']
    
    def __str__(self):
        teams = ", ".join(self.team) if isinstance(self.team, list) else self.team
        return f"{self.name} team {teams}  goals {self.goals} assists {self.assists}"