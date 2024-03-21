from menu import Menu

menu = Menu()

# number of equations
num = menu.nOfEquations()

# a -> matrix of coefficients
# b -> vector of results
[a, b] = menu.fileLoad()

# x -> stop condition [1 - epsilon, 2 - iterations]
# y -> value of stop condition
[x, y] = menu.stopChoice()