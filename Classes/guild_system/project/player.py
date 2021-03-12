class Player:
    def __init__(self, name, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills.keys():
            self.skills[skill_name] = mana_cost
        else:
            return 'Skill already added'

    def player_info(self):
        p_data = f'Name: {self.name}\n' \
                 f'Guild: {self.guild}\n' \
                 f'HP: {self.hp}\n' \
                 f'MP: {self.mp}\n'
        for skill, mana in self.skills.items():
            p_data += f'==={skill} - {mana}\n'

        return p_data

# player = Player('ivo', 50, 50)
# player.add_skill('mana', 10)
# player.add_skill('new', 100)
# print(player.player_info())