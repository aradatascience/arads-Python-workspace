import pandas as pd

# dane
pacjenci = [
    {"imie": "Jan", "waga": 85, "wzrost": 1.80},
    {"imie": "Anna", "waga": 60, "wzrost": 1.65},
    {"imie": "Marek", "waga": 110, "wzrost": 1.75},
    {"imie": "Angelika", "waga": 55, "wzrost": 1.71}
]

# zmiana na tabelę Pandas
df = pd.DataFrame(pacjenci)

# obliczenie BMI dla wszystkich pacjentów na raz (bez pętli for)
df['BMI'] = df['waga'] / (df['wzrost'] ** 2)

print(df)

# filtrowanie otyłych pacjentów
otyly_pacjent = df[df['BMI'] > 30]

print(otyly_pacjent)
