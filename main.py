import random

class Domanda:
    testo: str
    livello: int
    rispCorretta: str
    rispErrata1: str
    rispErrata2: str


    def __init__(self, testo, livello, rispCorretta, rispErrata1, rispErrata2):
        self.testo = testo
        self.livello = livello
        self.rispCorretta = rispCorretta
        self.rispErrata1 = rispErrata1
        self.rispErrata2 = rispErrata2

elenco_domande= []
with open('domande.txt', 'r') as file:
    for linea in file:
        dati = linea.strip().split('\n')
        dTemp = Domanda(dati[0], dati[1], dati[2], dati[3], dati[4])
        elenco_domande.append(dTemp)

    livelloAttuale=0
    scelta= random.choice[(d for d in elenco_domande if d.livello == livelloAttuale)]
    testo=scelta.testo


    print("Livello" + livelloAttuale +")" + scelta.testo + "\n"
          )



