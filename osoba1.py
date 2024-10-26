import argparse
import osoba2

rozwiniecie_skrot_na_numer={'pn' : 1, 'wt' : 2, 'sr' : 3, 'cz' : 4, 'pt' : 5, 'sob' : 6, 'nd' : 7}
rozwiniecia_numerow_na_pelna_nazwe = {1: 'poniedzialek', 2: 'wtorek',
                           3: 'sroda', 4: 'czwartek', 5: 'piatek', 6: 'sobota',
                           7: 'niedziela'}

parser = argparse.ArgumentParser()

parser.add_argument("-t", action = "store_true", help=""
"Uruchomiony z flagą -t pozwala na zapis pliku. Domyślnie pliki są odczytywane.")
parser.add_argument("-j", action = "store_true", help=""
"Uruchomiony z flagą -j pozwala na działanie na plikach typu json."
"Domyślnie działamy na plikach na plikach csv jeżeli nie podano tego parametru.")
parser.add_argument("--miesiace", nargs = "*",  help = ""
"Przyjmuje ciąg miesięcy podawanych bez przecinków po argumencie nazywamy miesiące ")
parser.add_argument("--dni", nargs = "*", help = ""
"Przyjmuje ciąg skrótów nazw dni"
" (można również podawać przedziały np. pn-pt) podawanych bez przecinków po argumencie nazywamy dni")
parser.add_argument("--pory", nargs = "*", help = ""
"Przyjmuje ciąg liter podawanych bez przecinków r lub w oznaczających rano lub wieczór"
"jeżeli nie podano nic, to domyślnie jest rano. ")
args = parser.parse_args()

miesiace = []
for miesiac in args.miesiace:
    miesiace.append(miesiac)

pory = []
for pora in args.pory:
    if(pora == "r"):
        pory.append("rano")
    if(pora == "w"):
      pory.append("wieczor")

dni = []
for dzien in args.dni:
    napis = dzien.split('-')
    if(len(napis) == 1):
       dni.append([rozwiniecia_numerow_na_pelna_nazwe[rozwiniecie_skrot_na_numer[napis[0]]]])
    else:
        zestaw = []
        for i in range(rozwiniecie_skrot_na_numer[napis[0]], rozwiniecie_skrot_na_numer[napis[1]] + 1):
            zestaw.append(rozwiniecia_numerow_na_pelna_nazwe[i])
        dni.append(zestaw)

if (args.t == True):
    tryb = 'w'
else:
    tryb = 'r'

if (args.j == True):
    rozszerzenie = 'json'
else:
    rozszerzenie = 'csv'

osoba2.przetwarzanie_plikow(miesiace, dni, pory, tryb, rozszerzenie)
