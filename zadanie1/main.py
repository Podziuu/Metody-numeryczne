import numpy as np
import matplotlib.pyplot as plt

from menu import Menu
from calculations import Calculations
from bisekcja import Bisekcja

menu = Menu()
function = menu.functionChoice()
edges = menu.edgesChoice()
stop = menu.stopChoice()

calculations = Calculations(function[1])
bisekcja = Bisekcja(calculations, edges[0], edges[1], stop[1])
result = bisekcja.calculate(stop[0], function[0])
print(result)

x_values = np.linspace(edges[0], edges[1], 100)
if function[0] == 1:
    y_values = calculations.horner(x_values)
elif function[0] == 2:
    y_values = calculations.trigonometry(x_values)
elif function[0] == 3:
    y_values = calculations.exponential(x_values)

plt.plot(x_values, y_values, label="f(x)")
plt.scatter(result[0], 0, color="red", label="Punkt zerowy")
plt.axhline(0, color="black", lw=0.5)
plt.axvline(result[0], color="green", lw=0.5)
plt.grid(color="gray", linestyle="--", linewidth=0.5)
plt.legend()
plt.show()
