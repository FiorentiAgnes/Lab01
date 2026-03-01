import random

#CLASSE DOMANDA
class Domanda:
    def __init__(self, testo, livello, corretta, errate):
        self.testo = testo
        self.livello = int(livello)
        self.corretta = corretta
        self.errate = errate #lisat di risposte errate

    def opzioni(self): #lista con tutte le risposte
        opzioni= [self.corretta] + self.errate
        random.shuffle(opzioni)
        return opzioni

#CLASSE GIOCO
class Gioco:
    def __init__(self, domande):
        self.domande = domande
        self.livello_attuale=0
        self.punteggio=0
        self.finita = False

    def get_prossima_domanda(self): #domanda del livello attuale
        possibili= [d for d in self.domande if d.livello == self.livello_attuale]
        if not possibili:
            return None
        return random.choice(possibili)

    def verifica_risposta(self, domanda, scelta, opzioni):
        risposta=opzioni[scelta - 1] # indice nella lista da 0 a 3
        if risposta == domanda.corretta:
            self.punteggio+=1
            self.livello_attuale+=1
            livelli_rimanenti = [d for d in self.domande if d.livello==self.livello_attuale]
            if not livelli_rimanenti:
                self.finita = True
            return True
        else:
            self.finita = True
            return False

#CLASSE PLAYER
class Player:
    def __init__(self, nickname, punteggio):
        self.nickname = nickname
        self.punteggio=int(punteggio)

    def __str__(self): #stampa
        return f"{self.nickname} {self.punteggio}"

#LETTURA FILE
#struttura file: 6 righe da leggere + una vuota
elenco_domande= []
try:
    with open('domande.txt', 'r') as file:
        righe=[linea.strip() for linea in file if linea.strip()] #legge righe non vuote
    #bisogna raggruppare la lista a 6 a 6
    for i in range(0, len(righe), 6):
        testo = righe[i]
        livello= righe[i+1]
        corretta= righe[i+2]
        errate=[righe[i+3], righe[i+4], righe[i+5]]
        nuova_domanda=Domanda(testo, livello, corretta, errate)
        elenco_domande.append(nuova_domanda)
except FileNotFoundError:
    print("FIle non trovato")

#SCRITTURA FILE
def salva_punti(nuovo_giocatore):
    classifica=[]
    #lettura file e dati già esistenti
    try:
        with open("punti.txt", "r") as f:
            for riga in f:
                parti = riga.strip().split()
                if len(parti) >= 2:
                    classifica.append(Player(parti[0], parti[1]))
    except FileNotFoundError:
        print("FIle non trovato")
    classifica.append(nuovo_giocatore)
    classifica.sort(key=lambda p: p.punteggio, reverse=True) #ordinamento
    with open("punti.txt", "w") as f:
        for p in classifica:
            f.write(str(p) + "\n")

#PARTITA
gioco= Gioco(elenco_domande)
print("TRIVIA GAME")

while not gioco.finita:
    domanda_corrente= gioco.get_prossima_domanda()

    if domanda_corrente is None:
        print("Domande terminate")
        break

    opzioni=domanda_corrente.opzioni()

    print(f"\nLivello {gioco.livello_attuale} {domanda_corrente.testo}")
    for i in range(len(opzioni)):
        print(f" {i+1}. {opzioni[i]}")

    try:
        scelta = int(input("Inserisci la risposta (1-4):"))
        if gioco.verifica_risposta(domanda_corrente, scelta, opzioni):
            print("Risposta corretta!")
        else:
            print(f"Risposta sbagliata! La risposta corretta era: {domanda_corrente.corretta}")
    except (ValueError, IndexError):
        print("Inserimento non valido!")
        gioco.finita = True
print(f"\nHai totalizzato {gioco.punteggio} punti")
nickname = input("Inserisci il tuo nickname: ")
nuovo_p = Player(nickname, gioco.punteggio)
salva_punti(nuovo_p)
print("Risultato salvato in classifica")