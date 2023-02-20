#LEPSZY OD ULEPSZONYKALKULATOR I KALKULATOR NA 2 WARTOŚCI#


print("Co chcesz zrobić?")
print("1) Mnożenie (nieskończone)")
print("2) Dodawanie (nieskończone)")
print("3) Odejmowanie")
print("4) Dzielenie", "\n")

while True:
    wybor = input("Wybierz (1/2/3/4): ")
    
    if wybor == '1':
        print("\nWybrałeś mnożenie")
        wynik = 1
        ilosc_liczb = int(input("Ile liczb chcesz pomnożyć? "))
        for i in range(ilosc_liczb):
            liczba = int(input("Liczba: "))
            wynik *= liczba
        print("\nWynik:", wynik)

    elif wybor == '2':
        print("\nWybrałeś dodawanie")
        wynik = 0
        ilosc_liczb = int(input("Ile liczb chcesz dodać? "))
        for i in range(ilosc_liczb):
            liczba = int(input("Liczba: "))
            wynik += liczba
        print("\nWynik:", wynik)

    elif wybor == '3':
        print("\nWybrałeś odejmowanie")
        liczba1 = int(input("Liczba 1:"))
        liczba2 = int(input("Liczba 2:"))
        wynik = liczba1 - liczba2
        print("\nWynik:", wynik)

    elif wybor == '4':
        print("\nWybrałeś dzielenie")
        liczba1 = int(input("Liczba 1:"))
        liczba2 = int(input("Liczba 2:"))
        wynik = liczba1 / liczba2
        print("\nWynik:", wynik)

    else:
        print("Błąd. Wybierz 1, 2, 3 lub 4.\n")
        continue

    nast_wyb = input("Zrobić kolejne zadanie? (Tak(1)/Nie(2)): ")
    print(" ")
    if nast_wyb != 'Tak' and nast_wyb != 'tak' and nast_wyb != '1':
      break
