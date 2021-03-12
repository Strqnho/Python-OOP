class Guild:
    def __init__(self, name):
        self.name = name
        self.list_of_players = []

    def assign_player(self, player):
        if player.guild == 'Unaffiliated':
            player.guild = self.name
            self.list_of_players.append(player)
            return f'Welcome player {player.name} to the guild {self.name}'

        elif player.guild == self.name:
            return f'Player {player.name} is already in the guild.'

        else:
            return f'Player {player.name} is in another guild.'

    def kick_player(self, pl_name):
        try:
            filtered_player = [p for p in self.list_of_players if p.name == pl_name][0]
            filtered_player.guild = 'Unaffiliated'
            self.list_of_players.remove(filtered_player)
        except IndexError:
            return f'Player {pl_name} is not in the guild.'

    def guild_info(self):
        g_data = f'Guild: {self.name}\n'
        for p in self.list_of_players:
            g_data += f'{p.player_info()}\n'
        return g_data

