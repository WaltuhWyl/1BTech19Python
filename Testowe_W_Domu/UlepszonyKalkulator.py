#GORSZY OD SKRÓCONY KALKULATOR#

def odej(x, y):
  return(x - y)
def dziel(x, y):
  return(x/y)

print("Co chcesz zrobić?")
print("1) Mnożenie, (nieskończone)")
print("2) Dodawanie (nieskończone)")
print("3) Odejmowanie")
print("4) Dzielenie", "\n")

while True:
    
  
    x = input("Wybierz (1/2/3/4): ")
    if x in ('1', '2', '3', '4'):
        if x == '1':
          print(" ")
          print("Wybrałeś mnożenie")
          ilocz = 1
          print(" ")
          a = int(input("Ile liczb chcesz pomnożyć? "))
          for i in range(a):
            b = int(input("Liczba: "))
            ilocz = ilocz*b
          print(" ")
          print("Wynik:", ilocz)

        elif x == '2':
          print(" ")
          print("Wybrałeś dodawanie")
          suma = 0
          print(" ")
          c = int(input("Ile liczb chcesz dodać? "))
          for i in range(c):
            d = int(input("Liczba: "))
            suma += d
          print(" ")
          print("Wynik:", suma)

        elif x == '3':
          print(" ")
          print("Wybrałeś odejmowanie")
          print(" ")
          o = int(input("Liczba 1:"))
          d = int(input("Liczba 2:"))
          print(" ")
          print("Wynik", odej(o, d))

        elif x == '4':
          print(" ")
          print("Wybrałeś dzielenie")
          print(" ")
          t = int(input("Liczba 1:"))
          y = int(input("Liczba 2:"))
          print(" ")
          print("Wynik", dziel(t, y))

        print(" ")      
        nast_wyb = input("Zrobić kolejne zadanie? (Tak(1)/Nie(2)) ")
        print(" ")
        if nast_wyb == '2':
          break
    
    else:
      print("Zrobiłes błąd")
      break