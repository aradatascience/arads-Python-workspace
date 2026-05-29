# 1. Funkcja zwraca True jeśli jest problem lub False jesli jest OK
def czy_ponad_norme(poziom):
    return poziom > 100

# 2. Dane
cukier = [95, 120, 88, 140, 105]
wyniki_alarmujace = []

# 3. Pętla i selekcja danych
for pomiar in cukier:
    if czy_ponad_norme(pomiar):
        wyniki_alarmujace.append(pomiar)

# 4. Wynik
print(f"Znaleziono {len(wyniki_alarmujace)} wyników ponad normę.")
print(f"Wartości alarmujące: {wyniki_alarmujace}")
