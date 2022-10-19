import numpy as np


def wyznacznik_macierzy(a):
    indexy = list(range(len(a)))
    wynik = 0
    if len(a[0]) == 2 and len(a) == 2:
        return a[0][0] * a[1][1] - a[1][0] * a[0][1]
    for ind in indexy:
        ac = a.copy()
        ac = ac[1:]
        height = len(ac)
        for i in range(height):
            ac[i] = ac[i][0:ind] + ac[i][ind+1:]
        znak = (-1) ** (ind % 2)
        podmacierz = wyznacznik_macierzy(ac)
        wynik += znak * podmacierz * a[0][ind]
    return wynik


M1 = [[-2, 2, -3],
      [-1, 5, 3],
      [2, 0, -1]]

M2 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]

M3 = [[1, 2, 3, 4, 1],
      [8, 5, 6, 7, 2],
      [9, 12, 10, 11, 3],
      [13, 14, 16, 15, 4],
      [10, 8, 6, 4, 2]]

print("Wyznacznik zaimplementowanym kodem: ", wyznacznik_macierzy(M1))
print("Wyznacznik np: ", np.linalg.det(M1))
print("---------------------------------------------------")
print("Wyznacznik zaimplementowanym kodem: ", wyznacznik_macierzy(M2))
print("Wyznacznik np: ", np.linalg.det(M2))
print("---------------------------------------------------")
print("Wyznacznik zaimplementowanym kodem: ", wyznacznik_macierzy(M3))
print("Wyznacznik np: ", np.linalg.det(M3))
