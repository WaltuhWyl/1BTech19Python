#Dodawanie ułamków
a = int(input())
b = int(input())
c = int(input())
d = int(input())

x, y = b, d
iloczyn = x * y
while y > 0:
  x, y = y, x%y
NWW = iloczyn//x

e = (NWW // b) * a
f = (NWW // d) * c
g = e + f
print(f"{a}/{b} + {c}/{d} = {e}/{NWW} + {f}/{NWW} = {g}/{NWW}")