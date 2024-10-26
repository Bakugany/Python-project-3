import json
import random

### Zapisywanie danych do pliku json ###
def zapisz_dane(nazwa_pliku):
    dane = {
        "Model": random.choice(['A', 'B', 'C']),
        "Wynik": random.randrange(0, 1000),
        "Czas":  str(random.randrange(0, 1000)) + 's'
    }

    with open(nazwa_pliku, 'w') as plik:
        json.dump(dane, plik)


### Odczytanie danych z pliku json ###
def odczytaj_dane(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        dane = json.load(plik)
        if(dane and dane['Model'] == 'A'):
            ucięty_tekst = dane['Czas'][:-1]
            return int(ucięty_tekst)
        return 0
