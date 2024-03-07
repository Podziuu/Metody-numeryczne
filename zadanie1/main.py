import numpy as np
import matplotlib.pyplot as plt

# print("Menu:")
# print()
#
# print("Wybierz kryterium stopu: ")
# print("1. Wariant A - |xi - xi-1| < E")
# print("2. Wariant B - |f(xi)| < E")
# print("3. Liczba iteracji ")
# stop = int(input("Wybor: "))
#
# if stop == 1 or stop == 2:
#     epsilon = float(input("Podaj epsilon: "))
# elif stop == 3:
    # iterations = int(input("Podaj liczbe iteracji: "))


print("Podaj funkcje:")
print("1. Funkcja wielomianowa")
print("2. Funkcja trygonometryczna")
print("3. Funkcja wykladnicza")
print("4. Złożenie funkcji")
choice = int(input("Wybor: "))

if choice == 1:
    degree = int(input("Podaj stopien wielomianu: "))
    polynomial = []
    for i in range(degree + 1):
        polynomial.append(float(input("Podaj " + str(i + 1) + " wspolczynnik wielomianu: ")))
elif choice == 2:
    print("Wybierz funkcje trygonometryczna:")
    print("1. Sinus")
    print("2. Cosinus")
    print("3. Tangens")
    trygFunc = int(input("Wybor: "))

elif choice == 3:
    expBase = float(input("Podaj podstawe funkcji wykladniczej: "))
    print(expBase.is_integer())

