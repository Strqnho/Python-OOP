class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            return 'This pokemon is already caught'
        self.pokemon.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name):
        if pokemon_name in self.pokemon:
            self.pokemon.remove(pokemon_name)
            return f'You have released {pokemon_name}'
        else:
            return 'Pokemon is not caught'

    def trainer_data(self):
        t_data = f'Pokemon Trainer {self.name}' \
               f'Pokemon Count {len(self.pokemon)}\n'
        for p in self.pokemon:
            t_data += f'- {p.pokemon_details()}\n'
        return t_data
