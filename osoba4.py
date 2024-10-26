import json
import random
import os.path

### Zapisywanie danych do pliku json ###
def zapisz_dane_json(nazwa_pliku):
    dane = {
        "Model": random.choice(['A', 'B', 'C']),
        "Wynik": random.randrange(0, 1000),
        "Czas":  str(random.randrange(0, 1000)) + 's'
    }
    with open(nazwa_pliku, 'w') as plik:
        json.dump(dane, plik)


### Odczytanie danych z pliku json ###
def odczytaj_dane_json(nazwa_pliku):
    if(not os.path.isfile(nazwa_pliku)):
        return 0
    with open(nazwa_pliku, 'r') as plik:
        dane = json.load(plik)
        if(dane and dane['Model'] == 'A'):
            ucięty_tekst = dane['Czas'][:-1]
            return int(ucięty_tekst)
        return 0
