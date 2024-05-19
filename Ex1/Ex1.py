import json
import csv


def lireFichierJson(nomFichier):
    with open(nomFichier, "r") as f:
        donnees = json.load(f)
    return donnees


def ecrireFichierCsv(nomFichier, fichierJson):
    with open(nomFichier, "w", newline="") as f:
        ecrivainCsv = csv.writer(f)
        ecrivainCsv.writerow(["reel", "imaginaire"])
        for nbr in fichierJson:
            ecrivainCsv.writerow([nbr[0], nbr[1]])


fichierJson = "data.json"

fichierCsv = "data.csv"

lectureFichierJson = lireFichierJson(fichierJson)
ecrireFichierCsv(fichierCsv, lectureFichierJson)