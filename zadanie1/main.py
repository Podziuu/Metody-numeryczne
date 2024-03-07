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
print(bisekcja.calculate(stop[0], function[0]))
