# 1. Funkcja obliczająca BMI i zwracająca kategorię
def analizuj_bmi(waga, wzrost_m):
    bmi = waga / (wzrost_m ** 2)

    if bmi < 18.5:
        kategoria = "Niedowaga"
    elif bmi < 25:
        kategoria = "Norma"
    elif bmi < 30:
        kategoria = "Nadwaga"
    else:
        kategoria = "Otyłość"

    return round(bmi, 2), kategoria

# 2. Symulowana baza danych pacjentów (lista słowników)
pacjenci = [
    {"imie": "Jan", "waga": 85, "wzrost": 1.80},
    {"imie": "Anna", "waga": 60, "wzrost": 1.65},
    {"imie": "Marek", "waga": 110, "wzrost": 1.75},
    {"imie": "Angelika", "waga": 55, "wzrost": 1.71}
]

# 3. Analiza danych w pętli
print("--- RAPORT KLINICZNY ---")
for pacjent in pacjenci:
    wynik_bmi, status = analizuj_bmi(pacjent["waga"], pacjent["wzrost"])
    print(f"Pacjent: {pacjent['imie']} | BMI: {wynik_bmi} | Status: {status}")
