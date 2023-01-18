#ZAD 1
# a = int(input())
# b = int(input())
# c = int(input())

# if b - a == c - b:
#   print("arytmetyczny")
# if b / a == c / b:
#   print("geometryczny")
# if a < b < c:
#   print("rosnący")
# if a > b > c:
#   print("malejący")

#ZAD 2
# suma = 0
# for i in range(100, 1000):
#   if i%8 ==0 and i%16 !=0:
#     suma = suma + i
# print(suma)

# #ZAD 3
# for i in range(99, 9, -1):
#   if i%7 ==0:
#     wielok = i
#     break



# ilość = 0
# for i in range(1000, 10000):
#   if i%wielok ==0:
#     ilość = ilość + 1

# print(ilość)
#Zad4
    
# ilość = 0
# for i in range(10, 100):
#   cd = i // 10
#   cj = i%10
#   if cd >= 2*cj:
#     ilość += 1
# print(ilość)

#Zad 5 nie sprawdzone
# suma = 0
# ilosc = 0
# for i in range(100, 1000):
#   cs = i // 100
#   cd = (i%100)//10
#   cj = i%10
#   if cs > cd+cj:
#     ilosc += 1
#     suma += i
# print(ilosc, " ", suma)

#Zad6 adono
# suma = 0
# n = int(input())
# for i in range(10, n*10+1):
#   if i%19 ==0 and 10<=i>=99:
#     suma += i
# print(suma)

#Zad7

#Zad8
# n = int(input())
# suma = 0
# for i in range(1, n+1):
#   for j in range(i):

# n = int(input())
# a, b, c = 2, 5, 
# suma = 0
# for i in range(n):
#     a, b = a-b, a+b
#     suma += b
# print(suma)