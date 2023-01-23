# //Wygeneruj tablicę n losowych liczb:
# (1. Znajdź największą liczbę w tablicy
# (2. Znajdź najmniejszą liczbę w tablicy
# (3. Podaj ile razy występuje najwieksza liczba w tablicy
# (4. Podaj ile razy występuje najmniejsza liczba w tablicy
# (5. Podaj rozpiętość tablicy (różnica max - min)
# (6. Podaj sumę liczb w tablicy
# (7. Podaj średnią wartość liczb w tablicy
# (8. Których liczb jest więcej w tablicy: parzystych czy nieparzystych?
# (9. Ile w tablicy jest liczb pierwszych?
# (10. Podaj v-ce max i v-ce min liczb tablicy
zdanie = "Zadania z tablic (list)"
print(zdanie.center(100))

from random import randint
L = [randint(1,21) for i in range(20)]
print(L, "-Czysty L""\n")
print(max(L), "(1. Znajdź największą liczbę w tablicy", "\n")
print(min(L), "(2. Znajdź najmniejszą liczbę w tablicy", "\n")
print(L.count(max(L)), "(3. Podaj ile razy występuje najwieksza liczba w tablicy", "\n")
print(L.count(min(L)), "(4. Podaj ile razy występuje najmniejsza liczba w tablicy", "\n")
print(max(L)-min(L), "(5. Podaj rozpiętość tablicy (różnica max - min)", "\n")
print(sum(L), "(6. Podaj sumę liczb w tablicy", "\n")
print((sum(L)/20), "(7. Podaj średnią wartość liczb w tablicy (bład z zaokrągleniem)", "\n")