import json
import csv


def lireFichierJson(nomFichier):  # Charge le fichier Json pour permettre la lecture
    with open(nomFichier, "r") as f:
        donnees = json.load(f)
    return donnees


def ecrireFichierCsv(nomFichier, fichierJson):   # Prend comme paramètre le fichier json et écrit ligne par ligne les nombres
    with open(nomFichier, "w", newline="") as f:
        ecrivainCsv = csv.writer(f)
        ecrivainCsv.writerow(["reel", "imaginaire"])
        for nbr in fichierJson:
            ecrivainCsv.writerow([nbr[0], nbr[1]])


if __name__ == "__main__":   # main programme
    fichierJson = "data.json"

    fichierCsv = "data.csv"

    lectureFichierJson = lireFichierJson(fichierJson)
    ecrireFichierCsv(fichierCsv, lectureFichierJson)