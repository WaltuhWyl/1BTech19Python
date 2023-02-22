#####MOJA METODA####
# #w klasie
# T = [50, 20, 10, 5, 2, 1, 0.5, 0.10, 0.01, 0.02, 0.05]
# T.sort(reverse=True)
# x = float(input("Reszta: "))
# print(" ")
# for i in T:
#   ilość = x // i
#   if ilość > 0:
#     x = x - ilość * i
#     wynik = int(ilość // 1)
#     print(f"{wynik} razy {i}zł")

#w domu
# T = [100, 200, 500, 50, 20, 10, 5, 2, 1, 0.5, 0.10, 0.01, 0.02, 0.05]
# T.sort(reverse=True)

# try:
#   x = float(input("Reszta: "))
# except:
#   ValueError
#   print("ValueError (musisz wpisać cyfrę)")
# else:
#   print(" ")
#   if x == 0:
#     print("Nie ma reszty z zera")
#     exit(0)
#   else:
#     for i in T:
#       ilość = x // i
#       if ilość > 0:
#         x = x - ilość * i
#         wynik = int(ilość // 1)
#         print(f"{wynik} razy {i}zł")


#####LUB to co robiliśmy w klasie#####

# T = [50, 20, 10, 5, 2, 1]
# T.sort(reverse=True)
# W =[]
# x = int(input("Reszta: "))
# for i in T:
#   ilość = x // i
#   if ilość > 0:
#     x = x - ilość * i
#     for j in range(ilość):
#       W.append(i)
# print(W)

#####Inna metoda z lekcji#####

# T = [50, 20, 10, 5, 2, 1]
# T.sort(reverse=True)
# x = int(input("Reszta: "))
# for i in T:
#   ilość = x // i
#   if ilość > 0:
#     x = x - ilość * i
#     print(f"{ilość} razy {i}zł")