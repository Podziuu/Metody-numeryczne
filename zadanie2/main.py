from menu import Menu
from jacobi import Jacobi
import numpy as np

menu = Menu()

# number of equations
num = menu.nOfEquations()

# a -> matrix of coefficients
# b -> vector of results
[a, b] = menu.fileLoad()

# x -> stop condition [1 - epsilon, 2 - iterations]
# y -> value of stop condition
[x, y] = menu.stopChoice()

jacobi = Jacobi(y)

for i in range(num):
    print("\n" + "Uklad " + str(i + 1))
    reslut, iterations = (jacobi.calculate(a[i], b[i], x))
    if reslut is not None:
        for j in range(len(reslut)):
            print("X" + str(j+1) + " wynosi: " + str(reslut[j]))
        print("Liczba iteracji: " + str(iterations))
