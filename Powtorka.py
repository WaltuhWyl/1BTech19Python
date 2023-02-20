#DOBRZE ZAD1#

# a = int(input())
# b = int(input())
# suma_i = 0
# suma_j = 0

# for i in range(1, a):
#   if a %i  == 0:
#     suma_i += i
# print("Suma1:", suma_i)

# for j in range(1, b):
#   if b % j  == 0:
#     suma_j += j
# print("Suma1:", suma_j)

# if suma_i == b+1 and suma_j == a+1:
#   print("Dobrze")
# else:
#   print("Źle")


#      #ZAD2 Nie działa z niewadomych przyczyn#
# from math import gcd
# licz1 = int(input("Pierwszy licznik: "))
# mia1 = int(input("Pierwszy mianownik: "))
# licz2 = int(input("Drugi licznik: "))
# mia2 = int(input("Drugi mianownik: "))

# NWW = gcd(mia1, mia2)
# e = (NWW // mia1) * licz1
# f = (NWW // mia2) * licz2
# g = e + f


# if g > NWW:
#   coś = g/NWW
#   print(coś)
# else:
#   print(f"{licz1}/{mia1} + {licz2}/{mia2} = {e}/{NWW} + {f}/{NWW} = {g}/{NWW}")

#Działa na innych zasadach
# licz1 = int(input("Pierwszy licznik: "))
# mia1 = int(input("Pierwszy mianownik: "))
# licz2 = int(input("Drugi licznik: "))
# mia2 = int(input("Drugi mianownik: "))

# x, y = mia1, mia2
# iloczyn = x * y
# while y > 0:
#   x, y = y, x%y
# NWW = iloczyn//x

# e = (NWW // mia1) * licz1
# f = (NWW // mia2) * licz2
# g = e + f

# if g > NWW:
#   coś = g/NWW
#   print(coś)
# else:
#   print(f"{licz1}/{mia1} + {licz2}/{mia2} = {e}/{NWW} + {f}/{NWW} = {g}/{NWW}")

# poczatek = int(input("podaj ile (od początku) liczb pierwszych: "))
# i = 2
# licznik = 0
# while 1:
#   flaga = True;
#   for j in range(2, i):
#     if i % j ==0:
#       flaga = False
#       break
#   if flaga:
#       print(i, end=" ")
#       licznik += 1
#   if licznik == poczatek:
#     break
#   else:
#     i = i + 1

#                                                      PRE
# SZYFROWANIE RSA - Asymetryczne

# from math import gcd as NWD # Greatest Common Dividor - czyli NWD

# pie1 = 97
# pie2 = 101

# F = (pie1 - 1) * (pie2 - 1)
# N = pie1 * pie2

# for i in range(2, F):
#     if NWD(i, F) == 1:
#         E = i
#         break
# print(E, N)

# for i in range(2, N):
#     if (i * E) % F == 1:
#         D = i
#         break
# print(D,N)

# msg = input("Podaj słowo do szyfracji: ")

# szyfr = ""
# for i in msg:
#     szyfr += chr((ord(i) ** E) % N)
# print("Twój szyfr:", szyfr)

# jawny = ""
# for i in szyfr:
#     jawny += chr((ord(i) **D ) % N)
# print("Twoja deszyfracja:", jawny)


print("                                    #Huffman#")
print(" ")

W = "AAAAABBCCCCDDDEEEEEEEFGGGH" 
W += "."
H = ""
ilosc = 1
for i in range(len(W)-1):
  if W[i] == W[i+1]:
    ilosc += 1
  else:
    if ilosc > 1:
      H += str(ilosc)
    H += W[i]
    ilosc = 1

print(H)