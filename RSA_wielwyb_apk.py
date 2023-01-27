print("1) Napisać wiadomość")
print("2) Odszyfrować wiadomość")

while True:
  print(" ")
  wybór = input("Co chcesz zrobić? (1/2): ")
  print(" ")
  if wybór in ('1', '2'):
    if wybór == '1':

      from math import gcd as NWD

      pie1 = 97
      pie2 = 101
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