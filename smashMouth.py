class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __repr__(self):
        return f"{self.name} ({self.position})"

class NFLTeam:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def __repr__(self):
        return f"Team: {self.team_name}\nPlayers:\n" + "\n".join(str(player) for player in self.players)

player1 = Player("Joe Montana", "QB")
player2 = Player("Barry Sanders", "RB")
player3 = Player("Jerry Rice", "WR")
player4 = Player("Graham Gano", "K")

team = NFLTeam("Smashmouth Football")
team.add_player(player1)
team.add_player(player2)
team.add_player(player3)
team.add_player(player4)

print(team)
