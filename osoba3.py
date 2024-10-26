import csv;
import random;

filename = "Dane.csv"

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
