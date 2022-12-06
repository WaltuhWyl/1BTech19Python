#PRE

# Lista zwykła
# print(list(range(2,8,1)))
# print(list(range(10)))

# Pętla liczb dwucyfrowych od 10 do 22
# for (i) in range(10, 22):
#   print(i)

# Pętla liczb dwucyfrowych nieparzystych od 15 do 31
# for (i) in range(15, 32, 2):
#   print(i)

# Pętla liczb dwucyfrowych malejaco (step ujemny) i co daje end

# for (i) in range(99, 9, -1):
#   print(i, end=" ")

# for (i) in range(99, 9, -1):
#   print(i)


#Pętla liczb dwucyfrowych malejaco (step dodatni)

# for (i) in range(10, 100, 1):
#   print(109-i, end=" ")

# Pętla liczb 3-cyfrowych podzielnych przez 20

# for (i) in range(100, 1000, 20):
#   print(i, end=" ")




#Zad 1

# n = int(input())

# for (i) in range(n):
#   print(i**3 + 3, end=" ")


#Zad 2

# for (i) in range(105, 1005, 15):
#   print(i, end=" ")

#lub


#for (i) in range(100, 1000):
#  if i % 15 ==0:
#    print(i)



#Zad 3

# p = int(input())

# for i in range(1, p+1):
#   if p%i ==0:
#     print(i)


#Zad 4

# s = 0
# for i in range(10, 100):
#   s = s + i
# print(s)

#Zad 5 !!! karta pracy 3b zad 5

# n = int(input("W ilę gramy?"))
# suma = n * (n+1) //2
# for i in range(n-1):
#   a = int(input())
#   suma = suma - a
# print(suma)

#Dodatek Napisz pętlę sumującą liczby dwucyfrowe parzyste

# suma = 0
# for i in range(10, 100, 2):
#   suma = suma + i
# print(suma)
