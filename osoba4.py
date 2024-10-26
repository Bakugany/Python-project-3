### Zapisywanie danych do pliku json ###

import json
import random

def create_and_save_data():
    dane = {
        "Model": random.choice(['A', 'B', 'C']),
        "Wynik": random.randrange(0, 1000),
        "Czas":  random.randrange(0, 1000)
    }

    with open("Dane.json", 'w') as plik:
        json.dump(dane, plik)

create_and_save_data()
