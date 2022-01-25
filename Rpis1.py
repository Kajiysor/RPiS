import numpy as np
import random

print("A) Generowanie liczby losowej z przedziału (0, 1):")
print(f"Liczba wylosowana: {float(np.random.random(1))}\n")


print("B) Symulowanie wyciągnięcia trzech kart z tali:")
# Karty z numerami 39-52 to trefle
a, b, c = random.sample(range(1, 52), 3)
if a > 39 or b > 39 or c > 3:
    print("W wyciągniętych kartach znajduje się trefl\n")
else:
    print("W Wyciągniętych kartach nie znajduje się trefl\n")



print("C) Powtórzenie losowania wielokrotnie:")
def losowanie(N):
    counter_trefl = 0
    for i in range(N):
        a, b, c = random.sample(range(1, 53), 3)
        if a > 39 or b > 39 or c > 39:
            counter_trefl += 1
    return counter_trefl/N
n = 1
while True:
    if round(losowanie(n), 3) == 0.587:
        print(f"Ilosc losowan potrzebna do osiagniecia prawdopodobienstwa z Zad. 7 to: {n}\n")
        break
    n += 1