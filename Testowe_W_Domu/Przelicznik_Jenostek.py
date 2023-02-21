print("                   PRZELICZNIK JEDNOSTEK")
print("Co chcesz zrobić?: ")
print("1) Godziny na minuty")
print("2) Minuty na godziny")
print("3) Bity na bajty")
print("4) Bajty na bity")
print("\n")

while True:
    wybor_zadania = input("Wybierz: ")
    if wybor_zadania in('1', '2', '3', '4', 'Godziny na minuty', 'godziny na minuty', 'minuty na godziny', 'Minuty na godziny', 'Bity na bajty', 'bity na bajty', 'Bajty na bity', 'bajty na bity'):
        print("\n")
        if wybor_zadania == '1' or wybor_zadania == 'Godziny na minuty' or wybor_zadania == 'godziny na minuty':
            pierwsza_wartosc = float(input("Ilośc godzin: "))
            wynik = int(pierwsza_wartosc * 60)           
            if (pierwsza_wartosc * 60) % 60 != 0:
                print(f"Ilość minut po zaokrągleniu: {wynik}min", f"(Dokłanie: {pierwsza_wartosc * 60}min) ", "\n")
            else:
                print(f"Ilość minut: {wynik}min", "\n")

        elif wybor_zadania == '2' or wybor_zadania == 'minuty na godziny' or wybor_zadania == 'Minuty na godziny':
            pierwsza_wartosc = float(input("Ilość minut: "))
            wynik = int(pierwsza_wartosc // 60)
            if pierwsza_wartosc % 60 != 0:
                print(f"Ilość godzin po zaokrągleniu: {wynik}h", f"(Dokłanie: {pierwsza_wartosc / 60}h) ", "\n")
            else:
                print(f"Ilość godzin: {wynik}h", "\n")

        elif wybor_zadania == '3' or wybor_zadania == 'Bity na bajty' or wybor_zadania == 'bity na bajty':
            pierwsza_wartosc = float(input("Ilość bitów: "))
            wynik = int(pierwsza_wartosc * 8)
            if (pierwsza_wartosc * 8) % 8 != 0:
                print(f"Ilość bajtów po zaokrągleniu: {wynik}B", f"(Dokłanie: {pierwsza_wartosc * 8}B) ", "\n")
            else:
                print(f"Ilośc bajtów: {wynik}B", "\n")

        elif wybor_zadania == '4' or wybor_zadania == 'Bajty na bity' or wybor_zadania == 'bajty na bity':
            pierwsza_wartosc = float(input("Ilość bajtów: "))
            wynik = int(pierwsza_wartosc // 8)           
            if pierwsza_wartosc % 8 != 0:
                print(f"Ilość bitów po zaokrągleniu: {wynik}b", f"(Dokłanie: {pierwsza_wartosc / 8}b) ", "\n")
            else:
                print(f"Ilośc bitów: {wynik}b", "\n")

        print("\n")      
        nast_wyb = input("Zrobić kolejne zadanie? (Tak(1)/Nie(2)): ")
        print("\n")
        if (nast_wyb != '1' or nast_wyb != 'Tak' or nast_wyb != 'tak') and (nast_wyb == '2' or nast_wyb == 'Nie' or nast_wyb == 'nie'):
          print("Zakończyłeś używanie programu")
          break
        elif nast_wyb != '1' and nast_wyb != 'Tak' and nast_wyb != 'tak' and nast_wyb != '2' and nast_wyb != 'Nie' and nast_wyb != 'nie':
          print("Zrobiłeś bład. (Źle wybrałeś opcję)")
          break


    else:
        print("Zrobiłeś błąd. Wybierz opcję od 1 do 4.")
        break







# #LEPSZA WERSJA W FAZIE TESTOWEJ I NAPRAWIE

# print("PRZELICZNIK JEDNOSTEK", "\n")

# options = {
#     '1': 'Godziny na minuty',
#     '2': 'Minuty na godziny',
#     '3': 'Bity na bajty',
#     '4': 'Bajty na bity'
# }

# while True:
#     print("Co chcesz zrobić?: ", "\n")
#     for option in options.values():
#         print(option)
#     print("\n")
#     wybor_zadania = input("Wybierz: ")
#     if wybor_zadania in options.keys():
#         print("\n")
#         try:
#             pierwsza_wartosc = float(input(f"{options[wybor_zadania]}: "))
#         except ValueError:
#             print("Niepoprawna wartość. Wprowadź liczbę.")
#             continue

#         if wybor_zadania == '1':
#             wynik = int(pierwsza_wartosc * 60)           
#             if (pierwsza_wartosc * 60) % 60 != 0:
#                 print(f"Ilość minut po zaokrągleniu: {wynik}min", f"(Dokłanie: {pierwsza_wartosc * 60}min) ", "\n")
#             else:
#                 print(f"Ilość minut: {wynik}min", "\n")

#         elif wybor_zadania == '2':
#             wynik = int(pierwsza_wartosc // 60)
#             if pierwsza_wartosc % 60 != 0:
#                 print(f"Ilość godzin po zaokrągleniu: {wynik}h", f"(Dokłanie: {pierwsza_wartosc / 60}h) ", "\n")
#             else:
#                 print(f"Ilość godzin: {wynik}h", "\n")

#         elif wybor_zadania == '3':
#             wynik = int(pierwsza_wartosc * 8)
#             if (pierwsza_wartosc * 8) % 8 != 0:
#                 print(f"Ilość bajtów po zaokrągleniu: {wynik}B", f"(Dokłanie: {pierwsza_wartosc * 8}B) ", "\n")
#             else:
#                 print(f"Ilośc bajtów: {wynik}B", "\n")

#         elif wybor_zadania == '4':
#             wynik = int(pierwsza_wartosc // 8)           
#             if pierwsza_wartosc % 8 != 0:
#                 print(f"Ilość bitów po zaokrągleniu: {wynik}b", f"(Dokłanie: {pierwsza_wartosc * 8}b) ", "\n")
#             else:
#               print(f"Ilośc bitów: {wynik}B", "\n")

#         nast_wyb = input("Zrobić kolejne zadanie? (Tak(1)/Nie(2)): ")
#         print("\n")
#         if (nast_wyb != '1' or nast_wyb != 'Tak' or nast_wyb != 'tak') and (nast_wyb == '2' or nast_wyb == 'Nie' or nast_wyb == 'nie'):
#           print("Zakończyłeś używanie programu")
#           break
#         elif nast_wyb != '1' and nast_wyb != 'Tak' and nast_wyb != 'tak' and nast_wyb != '2' and nast_wyb != 'Nie' and nast_wyb != 'nie':
#           print("Zrobiłeś bład. (Źle wybrałeś opcję)")
#           break
#     else:
#       print("Zrobiłeś błąd. Wpisz prawidłowe wartości")
#       break