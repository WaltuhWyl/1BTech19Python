#ZAD1
# a = int(input())
# print(a%10)
# print(a%100//10)
# print(a%1000//100)

# x = int(input())
# def suma(a):
#   suma = 0
#   while a > 0:
#     suma += a%10
#     a = a//10
#   return suma
# print(suma(x))

#ZAD2
# n = int(input())
# for i in range(2, n):
#   if n % i == 0:
#     print("Liczba nie jest pierwsza")
#     exit(0)
# print("Liczba jest pierwsza")

#ZAD3
# a = int(input())
# sprawdzenie = 0
# for i in range(1, a):
#   if a%i ==0:
#     sprawdzenie += i
# if sprawdzenie == a:
#   print("doskonała")
# else:
#   print("niedoskonała")

#ZAD4
# a  = int(input())
# b = int(input())
# nwd = 0
# while b > 0:
#   a, b = b, a%b
#   nwd = a
# if nwd ==1:
#   print("Względnie pierwsza")
# else:
#   print("Nie")

#ZAD5
# a = int(input("Podaj liczbę: "))
# for i in range(10,20):
#     a1 = a
#     i1 = i
#     while a1 != i1:
#         if a1 > i1:
#             a1 -= i1
#         else:
#             i1 -= a1
#     if a1 == 1:
#         print(i)

#ZAD6
# a = int(input())
# b = int(input())
# a1 = a
# b1 = b
# while a != b:
#     if a > b:
#         a -= b
#     else:
#         b -= a
# a1 //= a
# b1 //= b
# print(f"{a1}/{b1}")

#ZAD7
