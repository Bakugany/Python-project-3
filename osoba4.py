import json
import random

### Zapisywanie danych do pliku json ###
def zapisz_dane(nazwa_pliku):
    dane = {
        "Model": random.choice(['A', 'B', 'C']),
        "Wynik": random.randrange(0, 1000),
        "Czas":  random.randrange(0, 1000)
    }

    with open(nazwa_pliku, 'w') as plik:
        json.dump(dane, plik)


### Odczytanie danych z pliku json ###
def odczytaj_dane(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        dane = json.load[plik]
        if(dane['Model'] == 'A'):
            return dane['Czas']
        return 0
