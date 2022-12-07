import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import math


def metryka_euklidesowa(a, b):
    dystans = 0
    for i in range(len(a)):
        dystans += (a[i] - b[i])**2
    return math.sqrt(dystans)


def odlegosci_od_x(lista, x):
    wynik = []
    for i in lista:
        para = (i[-1], (metryka_euklidesowa(x, i)))
        wynik.append(para)
    return wynik


def podzial(lista):
    wynik = {}
    for i in range(len(lista)):
        pom = lista[i][0]
        if pom in wynik.keys():
            wynik[pom].append(lista[i][1])
        else:
            wynik[pom] = [lista[i][1]]
        wynik[pom].sort()
    return wynik


def segregacja_odleglosci(lista):
    slownik = {}
    for i in lista:
        if i[0] not in slownik.keys():
            slownik[i[0]] = [i[1]]
        else:
            slownik[i[0]].append(i[1])
    return slownik


def sumowanie(lista, k):
    wynik = {}
    for klucz in lista.keys():
        suma = 0
        for i in range(k):
            suma += lista[klucz][i]
        if klucz not in wynik.keys():
            wynik[klucz] = []
        wynik[klucz].append(suma)
    return wynik


def sumowanie_odleglosci(lista, k):
    slownik = {}
    for i in lista.keys():
        tmp_list = lista[i]
        tmp_list.sort()
        slownik[i] = sum(tmp_list[0:k])
    return slownik


def decyzja(lista, x, k):
    wynik = []
    for i in range(len(x)):
        odleglosc = odlegosci_od_x(lista, x[i])
        slownik = podzial(odleglosc)
        sumaKodleglosci = sumowanie(slownik, k)
        print("Wektor: ", x[i])
        print("Sumy odległości do punktów: ", sumaKodleglosci)
        list = [(k, v) for k, v in sumaKodleglosci.items()]
        minimum = list[0][1]
        dec = 0
        for para in list[1:]:
            if para[1] == minimum:
                return None
            if para[1] < minimum:
                minimum = para[1]
                dec = para[0]
        wynik = np.append(wynik, dec)
        print("Decyzja: ", dec)
    wynik = np.reshape(wynik, (len(wynik), 1))
    x = np.hstack((x, wynik))
    return x


iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
X = iris.data
arr = df.to_numpy()
mask = np.random.rand(len(arr)) <= 0.7
training_array = arr[mask]
testing_array = arr[~mask]
testing_array_copy = np.delete(testing_array, 4, 1)
knn = decyzja(training_array, testing_array_copy, 5)
nonzero = np.nonzero(knn-testing_array)[0]
print(knn)
print("Ind niezerowych elementów porównania macierzy", nonzero)
print("% poprawności algorytmu: ", (1 - len(nonzero)/len(testing_array_copy))*100)

