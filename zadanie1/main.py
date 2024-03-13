import numpy as np
import matplotlib.pyplot as plt

from menu import Menu
from bisekcja import Bisekcja
from falsi import Falsi

menu = Menu()
function = menu.functionChoice()
edges = menu.edgesChoice()
stop = menu.stopChoice()


bisekcja = Bisekcja(function, edges[0], edges[1], stop[1])
result = bisekcja.calculate(stop[0])
print(result)

if(result == "Error"):
    print("Metoda nie zbiega")
    exit()

falsi = Falsi(function, edges[0], edges[1], stop[1])
result2 = falsi.calculate(stop[0])
print(result2)

if(result2 == "Error"):
    print("Metoda nie zbiega")
    exit()

x_values = np.linspace(edges[0], edges[1], 100)
y_values = function.calculate(x_values)

plt.plot(x_values, y_values, label="f(x)")
plt.scatter(result[0], 0, color="red", label="Punkt zerowy")
plt.axhline(0, color="black", lw=0.5)
plt.axvline(result[0], color="green", lw=0.5)
plt.grid(color="gray", linestyle="--", linewidth=0.5)
plt.legend()
plt.show()
