print("                                    #Pierwsze#", "\n")
print("1)a) Sprawdzanie czy liczba jest pierwsza")

#Program sprawdzający czy liczba jest pierwsza
spr_czy_l_j_p = int(input("Wpisz liczbę: "))
for i in range(2, spr_czy_l_j_p):
  if spr_czy_l_j_p % i == 0:
    print("Liczba nie jest pierwsza")
    exit(0)
print("Liczba jest pierwsza")
print(" ")


print("1)b) Generowanie liczb pierwszych w przedziale")
od_ilu = int(input("podaj do ilu mam szukać liczb pierwszych: "))
do_ilu = int(input("podaj do ilu mam szukać liczb pierwszych: "))
for i in range(od_ilu, do_ilu+1):
  flaga = True;
  for j in range(2, i):
    if i % j ==0:
      flaga = False
      break
  if flaga:
      print(i, end=" ")
print(" ")
print(" ")


print("1)c)  Generowanie liczb pierwszych (pierwsze n-liczb pierwszych): ")
poczatek = int(input("podaj ile (od początku) liczb pierwszych: "))
i = 2
licznik = 0
while 1:
  flaga = True;
  for j in range(2, i):
    if i % j ==0:
      flaga = False
      break
  if flaga:
      print(i, end=" ")
      licznik += 1
  if licznik == poczatek:
    break
  else:
    i = i + 1
print(" ")
print(" ")

####################################################################
print("                                    #NWD# ", "\n")
print("2)a) NWD modulo")

a = int(input("Pierwsza liczba: "))
b = int(input("Druga liczba: "))
while b > 0:
  a, b = b, a%b
print(a, "\n")

print("2)b) NWD (NIE)modulo")

a = int(input("Pierwsza liczba: "))
b = int(input("Druga liczba: "))

while a != b:
  if a > b : a = a - b
  if b > a : b = b - a
print(a, "\n")

####################################################################
print("                                    #NWW#")
print(" ")

print("4)a) NWW z Eukledisem z Algorytm NWD Euklides(musi być a)")
a = int(input("Pierwsza liczba: "))
b = int(input("Druga liczba: "))
iloczyn = a*b
while b > 0:
  a, b = b, a%b
print(iloczyn//a)
print(" ")


print("4)b) NWW z odejmowaniem z Algorytm NWD.py")
a = int(input("Pierwsza liczba: "))
b = int(input("Druga liczba: "))
iloczyn = a*b
while a != b:
  if a > b : a = a - b
  if b > a : b = b - a
print(iloczyn//a)
print(" ")

################################################################
print("                                    #Ułamki#")
print(" ")

print("5)a) Dodawanie ułamków")
a = int(input("Pierwsza licznik: "))
b = int(input("Pierwszy mianownik: "))
c = int(input("Drugi licznik: "))
d = int(input("Drugi mianownik: "))

x, y = b, d
iloczyn = x * y
while y > 0:
  x, y = y, x%y
NWW = iloczyn//x

e = (NWW // b) * a
f = (NWW // d) * c
g = e + f
print(f"{a}/{b} + {c}/{d} = {e}/{NWW} + {f}/{NWW} = {g}/{NWW}")
print(" ")

###############################################################
print("                                    #Cezar#")
print(" ")

print("6)a) Zadanie testowe: wypisz alfabet liter wielkich")
for i in range(65,91):
    print(chr(i), end="")
print(" ")
print(" ")

print("6)b) Szyfrowanie cezarem i przykład funkcji")

napis = input("Podaj coś do zaszyfrowania: ")
szyfr = ""
print(napis[0], napis[1], napis[2])
print(len(napis))

for i in range(len(napis)):
    szyfr = szyfr + chr(65 + ((ord(napis[i])-65+3) % 26))
print(szyfr)
print(" ")
print(" ")

###########################################################
print("                                    #RSA(teoretycznie nie dokończone)#")
print(" ")

print("7)a) Omównienie RSA")
# 1. Wybór dużych liczb pierwszych (lepiej by były bardzo duże)
p = 11
q = 13
print("Liczba p:", p,"Liczba q:",  q)

#2. Obliczenie n=p*q i funkcji Eulera F=(p-1)*(q-1)
n = p * q
F = (p-1) * (q-1)
print("n:", n)
print("Euler:", F)

#3. Generujemy klucz publiczny e taki, że NWD(e, F)=1
from math import gcd
for i in range(2, F):
  if gcd(i, F) == 1:
    e = i
    break
print("Klucz publiczny:", e, n)

#4. Generujemy klucz prywatny d taki, że (d*e) % F = 1
for j in range(2, F):
  if ((j*e) % F) == 1:
    d = j
    break
print("Klucz prywatny:", d, n)

#                              Przykład działania RSA
# m = moja wiadomość = message
# c = m**e % n (szyfrogram = cypher = wiadomość zaszyfrowana)
# t = c**d % n (tekst jawny, czyli nasza wiadomość = text (message))

m = input("Podaj słowo do szyfracji: ")
cipher = ""
for i in m:
  cipher += chr((ord(i)**e)%n)
print(cipher)

tekst = ""
for j in cipher:
    tekst += chr((ord(j)**d)%n)
print("Twoja deszyfracja:", tekst)