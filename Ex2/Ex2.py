import csv


def pokemonCsv(nomFichier):
    pokemonDict = {}
    with open(nomFichier, newline='') as f:
        leacteurCsv = csv.reader(f)
        for ligne in leacteurCsv:
            # print(ligne)
            nom = ligne[0]
            stats = list(map(int, ligne[1:]))
            pokemonDict[nom] = stats
    return pokemonDict


if __name__ == '__main__':
    pokemon = pokemonCsv("pokemon.csv")
    for nom, stats in pokemon.items():
        print(f"{nom}: {stats}")

    # print(isinstance(pokemon, dict))
    # print(isinstance(pokemon["Pikachu"], list))
    # print(isinstance(pokemon["Pikachu"][0], int))
