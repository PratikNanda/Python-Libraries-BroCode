import pandas as pd

pokemons = {1: "Bulbasaur",
            2: "Ivysaur",
            3: "Vensaur",
            4: "Charmander",
            5: "Charmeleon",
            6: "Charizard"}

series = pd.Series(pokemons)

print(series)