from pathlib import Path
import os
import osoba3 as o3
import osoba4 as o4

# miesiace = [.], dni = [[.], [.]], pory = [.], tryb = 'rano'/'wieczor', rozszerzenie = 'csv'/'json',
def przetwarzanie_plikow(miesiace, dni, pory, tryb, rozszerzenie):
    cnt = 0
    for i in range(len(miesiace)):
        for j in range(len(dni[i])):
            sciezka = os.path.join(os.getcwd(), miesiace[i], dni[i][j])
            sciezka = Path(sciezka)
            
            if len(pory) > cnt:
                if pory[cnt] == 'rano':
                    sciezka = sciezka / 'rano'
                elif pory[cnt] == 'wieczor':
                    sciezka = sciezka / 'wieczor'
                    
            else:
                sciezka = sciezka / 'rano'
                
            cnt += 1
            
            if not os.path.exists(sciezka):
                os.makedirs(sciezka)
                
            if rozszerzenie == 'json':
                sciezka = sciezka / 'Dane.json'
                if tryb == 'r':
                    o4.odczytaj_dane_json(sciezka)
                elif tryb == 'w':
                    o4.zapisz_dane_json(sciezka)
                    
            elif rozszerzenie == 'csv':
                sciezka = sciezka / 'Dane.csv'
                if tryb == 'r':
                    o3.odczytaj_dane_csv(sciezka)
                elif tryb == 'w':
                    o3.zapisz_dane_csv(sciezka)
