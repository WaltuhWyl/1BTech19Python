## KALKULATOR https://www.programiz.com/python-programming/examples/calculator
def dodaj(x, y):
    return x + y

def odejmij(x, y):
    return x - y

def pomnóż(x, y):
    return x * y

def podziel(x, y):
    return x / y

print("Co chcesz zrobić?(1/2/3/4):")
print("1.Dodaj")
print("2.Odejmij")
print("3.Pomnóż")
print("4.Podziel?")

while True:
    
    wybór = input("Wybierz(1/2/3/4): ")
  
    if wybór in ('1', '2', '3', '4'):
        liczba1 = float(input("Pierwsza liczba: "))
        liczba2 = float(input("Druga liczba: "))

        if wybór == '1':
          print(liczba1, "+", liczba2, "=", dodaj(liczba1, liczba2))
        
        elif wybór == '2':
          print(liczba1, "-", liczba2, "=", odejmij(liczba1, liczba2))
        
        elif wybór == '3':
          print(liczba1, "*", liczba2, "=", pomnóż(liczba1, liczba2))
        
        elif wybór == '4':
          print(liczba1, "/", liczba2, "=", podziel(liczba1, liczba2))
        
      
  
        next_calculation = input("Zrobić kolejne działanie? (tak/nie): ")
        if next_calculation == "nie":
          break
    
    else:
        print("Coś źle zrobiłeś")