# Czytanie i Zapisywanie na pliku .csv
import csv;
import random;
from pathlib import Path

# Nazwa pliku musi być .csv
# Jeśli plik już istnieje to go zamienia
def zapisz_dane(nazwa_pliku):

    # Otwieramy plik
    plik = open(nazwa_pliku, 'w')
    pisarz = csv.writer(plik, delimiter=';')

    # Piszemy linijkę na samej górze z nazwami tzw. "header"
    tytuł = ["Model", "Wynik", "Czas"]
    pisarz.writerow(tytuł);

    # Piszemy wylosowane inforamcje w następnej linijce
    model = random.choice(["A","B","C"])
    wynik = random.randint(0, 1000)
    czas = str(random.randint(0,1000)) + "s"
    info = [model, wynik, czas]
    pisarz.writerow(info);

    # Zamykamy plik
    plik.close()

# Nazwa_pliku musi być .csv
# Jeśli plik nie istnieje zwraca 0
def odczytaj_dane(nazwa_pliku)-> int:
    if Path(nazwa_pliku).exists():
        with open(nazwa_pliku, 'r') as plik:
            czytelnik = csv.reader(plik, delimiter=';')
            next(czytelnik)
            wiersz = next(czytelnik)

            # Sprawdzamy czy wiersz istnieje i jak tak to czytamy czas, gdy Model to "A"
            if(wiersz and wiersz[0] == "A"):
                czas_int = int(wiersz[2][:-1])
                return czas_int

    # W defaultowym przypadku zwracamy 0
    return 0;
