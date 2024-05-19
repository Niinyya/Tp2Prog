import csv


def pokemonCsv(nomFichier):
    # stockage des pokemons
    pokemonDict = {}
    with open(nomFichier, newline='') as f:
        leacteurCsv = csv.reader(f)
        for ligne in leacteurCsv:
            # print(ligne)
            nom = ligne[0]  # garde le nom du pokemon
            stats = list(map(int, ligne[1:]))   # garde les stats du pokemon
            pokemonDict[nom] = stats    # écrit les stats du pokemon dans un dict avec le nom comme key
    return pokemonDict


if __name__ == '__main__':
    pokemon = pokemonCsv("pokemon.csv")
    for nom, stats in pokemon.items():
        print(f"{nom}: {stats}")


    # test pour vérification

    # print(isinstance(pokemon, dict))
    # print(isinstance(pokemon["Pikachu"], list))
    # print(isinstance(pokemon["Pikachu"][0], int))
