# Czytanie i Zapisywanie na pliku .csv
import csv;
import random;

# Nazwa pliku musi być .csv
def zapisz_dane_csv(nazwa_pliku):

    plik = open(nazwa_pliku, 'w')
    writer = csv.writer(plik, delimiter=';')

    tytuł = ["Model", "Wynik", "Czas"]
    writer.writerow(tytuł);

    model = random.choice(["A","B","C"])
    wynik = random.randint(0, 1000)
    czas = str(random.randint(0,1000)) + "s"
    info = [model, wynik, czas]
    writer.writerow(info);

    plik.close()

# Nazwa_pliku musi być .csv
def odczytaj_dane_csv(nazwa_pliku)-> int:
    with open(nazwa_pliku, 'r') as plik:
        czytelnik = csv.reader(plik, delimiter=';')
        next(czytelnik)
        wiersz = next(czytelnik)
        if(wiersz and wiersz[0] == "A"):
            czas_int = int(wiersz[2][:-1])
            return czas_int
        return 0;
