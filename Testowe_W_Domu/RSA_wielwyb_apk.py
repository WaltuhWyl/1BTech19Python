print("1) Napisać wiadomość")
print("2) Odszyfrować wiadomość")

while True:
  print(" ")
  wybór = input("Co chcesz zrobić? (1/2): ")
  print(" ")
  if wybór in ('1', '2'):
    if wybór == '1':
  
      from math import gcd as NWD
      wybór_l_p = input("Masz wybrane liczby pierwsze? (Tak1/Nie2): ")
      print(" ")
      if wybór_l_p in ('1', '2'):
        if wybór_l_p == '2':
          g = int(input("podaj od ilu mam szukać liczb pierwszych: "))
          h = int(input("podaj do ilu mam szukać liczb pierwszych: "))
          for i in range(g, h+1):
            flaga = True;
            for j in range(2, i):
              if i % j ==0:
                flaga = False
                break
            if flaga:
                print(i, end=" ")
          print(" ")
          print(" ")
          pie1 = int(input("Pierwsza liczba pierwsza: "))
          for piei in range(2, pie1):
            if pie1 % piei == 0:
              print("Liczba nie jest pierwsza")
              exit(0)
          pie2 = int(input("Druga liczba pierwsza: "))
          for piej in range(2, pie2):
            if pie2 % piej == 0:
              print("Liczba nie jest pierwsza")
              exit(0)
          print("Liczby pierwsze:", pie1, pie2)

          F = (pie1 - 1) * (pie2 - 1)
          N = pie1 * pie2
          print("Euler:", F)
          print("n:", N)

          for i in range(2, F):
              if NWD(i, F) == 1:
                  E = i
                  break
          print("Klucz publiczny", E, N)

          for i in range(2, N):
              if (i * E) % F == 1:
                  D = i
                  break
          print("Klucz prywatny:", D,N)
          print(" ")
      
          msg = input("Podaj słowo do szyfracji: ")

          szyfr = ""
          for i in msg:
              szyfr += chr((ord(i) ** E) % N)
          print("Twój szyfr:", szyfr)

          jawny = ""
          for i in szyfr:
              jawny += chr((ord(i) **D ) % N)
          print("Twoja deszyfracja:", jawny)


        if wybór_l_p == '1':
          pie1 = int(input("Pierwsza liczba pierwsza: "))
          pie2 = int(input("Druga liczba pierwsza: "))
          print("Liczby pierwsze:", pie1, pie2)

          F = (pie1 - 1) * (pie2 - 1)
          N = pie1 * pie2
          print("Euler:", F)
          print("n:", N)

          for i in range(2, F):
              if NWD(i, F) == 1:
                  E = i
                  break
          print("Klucz publiczny", E, N)

          for i in range(2, N):
              if (i * E) % F == 1:
                  D = i
                  break
          print("Klucz prywatny:", D,N)
          print(" ")
      
          msg = input("Podaj słowo do szyfracji: ")

          szyfr = ""
          for i in msg:
              szyfr += chr((ord(i) ** E) % N)
          print("Twój szyfr:", szyfr)

          jawny = ""
          for i in szyfr:
              jawny += chr((ord(i) **D ) % N)
          print("Twoja deszyfracja:", jawny)
      else:
        print("Zrobiłeś błąd")
        exit(0)

    elif wybór == '2':
    
      D = int(input("Klucz prywatny: "))
      N = int(input("n: "))
      print(" ")
      szyfr = input("Podaj słowo do deszyfracji: ")

      jawny = ""
      for i in szyfr:
          jawny += chr((ord(i) **D ) % N)
      print("Twoja deszyfracja:", jawny)

    print(" ")
    nast_wybór = input("Chcesz coś jeszcze zrobić (Tak1/Nie2)?: ")
    print(" ")
    if nast_wybór == '2':
      break

  else:
    print("Zrobiłeś błąd")
    break