#Zapisywanie do .csv
import csv;
import random;

#filename jest .csv
def write_file(filename):

    plik = open(filename, 'w')
    writer = csv.writer(plik, delimiter=';')

    header = ["Model", "Wynik", "Czas"]
    writer.writerow(header);

    Model = random.choice(["A","B","C"])
    Wynik = random.randint(0, 1000)
    Czas = str(random.randint(0,1000)) + "s"
    info = [Model, Wynik, Czas]
    writer.writerow(info);

    plik.close()

#filename jest .csv
def reading(filename)-> int:
    with open(filename, 'r') as plik:
        czytelnik = csv.reader(plik, delimiter=';')
        next(czytelnik)
        wiersz = next(czytelnik)
        if(wiersz and wiersz[0] == "A"):
            trimmed_text = wiersz[2][:-1]
            return int(trimmed_text)
        return 0;
