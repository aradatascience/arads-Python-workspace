# Program: Powitanie i obliczanie wieku

# 1. Input
imie = input("Jak masz na imię? ")
rok_urodzenia_str = input("W którym roku się urodziłeś/aś? ")

# 2. Konwersja tekstu na liczbę (bo input zwraca tekst)
rok_urodzenia = int(rok_urodzenia_str)
aktualny_rok = 2026

# 3. Obliczenia
wiek = aktualny_rok - rok_urodzenia

# 4. Wyświetlenie z f-string (tekst + zmienne)
print(f"Cześć {imie}! W roku {aktualny_rok} masz lub skończysz {wiek} lat.")

# 5. Dodany warunek
if wiek >= 18:
    print("Jesteś pełnoletni!")
else:
    print("Nie jesteś pełnoletni!")
    brakuje = 18 - wiek
    print(f"Do osiemnastki brakuje Ci jeszcze {brakuje} lat. ")