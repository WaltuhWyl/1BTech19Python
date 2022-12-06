#1. sprawdzanie czy liczba jest pierwsza
#liczba pierwsza- liczba, która dzieli się tylko przez 1 i samą siebie
#2,3,5,7,11,13,17,19,23...Itd
#dzielniki właściwe- dzielniki liczby poza 1 i nią samą

# n = int(input())
# for i in range(2, n):
#   if n % i == 0:
#     print("Liczba nie jest pierwsza")
#     exit(0)
# print("Liczba jest pierwsza")

#2. generowanie liczb pierwszych (w przedziale [p, q])
# p = int(input("podaj do ilu mam szukać liczb pierwszych"))
# q = int(input("podaj do ilu mam szukać liczb pierwszych"))
# for i in range(p, q+1):
#   flaga = True;
#   for j in range(2, i):
#     if i % j ==0:
#       flaga = False
#       break
#   if flaga:
#       print(i, end=" ")

# generowanie liczb pierwszych (pierwsze nliczb pierwszych)

# p = int(input("podaj ile (od początku) liczb pierwszych"))
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
#   if licznik == p:
#     break
#   else:
#     i = i + 1