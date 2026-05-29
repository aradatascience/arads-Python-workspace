def oblicz_napiwek(kwota_rachunku, procent=10):
    napiwek = kwota_rachunku * (procent / 100)
    return napiwek

# 1. Pobieramy dane
rachunek = float(input("Ile wyniósł rachunek (np. 50.50)?"))

# 2. Funkcja
napiwek_extra = oblicz_napiwek(rachunek, 15)

# 3. Wyświetlanie
print(f"Ekstra napiwek wyniesie {napiwek_extra} zł (15% kwoty).")
