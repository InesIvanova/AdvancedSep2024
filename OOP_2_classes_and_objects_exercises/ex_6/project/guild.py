from OOP_2_classes_and_objects_exercises.ex_6.project.player import Player

class Guild:
    def __init__(self, name: str) -> None:
        self.name = name
        self.players: list[Player] = []

    def assign_player(self, player: Player) -> str:
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        try:
            player = [p for p in self.players if p.name == player_name][0]
            self.players.remove(player)
            player.guild = "Unaffiliated"
            return f"Player {player.name} has been removed from the guild."
        except IndexError:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        result += "\n".join([p.player_info() for p in self.players])
        return result
