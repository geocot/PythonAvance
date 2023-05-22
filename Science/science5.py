import sympy as sp
x = sp.symbols("x")
print(sp.exp(x**2))
print(sp.sqrt(2))

#Geométrie
pol = sp.Polygon((0,0),(2,0),(2,2),(0,2))
print(pol.area) #Résultat = 4

#Résolution d'équations à plusieurs inconnus
x, y = sp.symbols("x y")
#Équation1 = x+y =5 // Équation2 = x-y =5
equation_1 = sp.Eq((x + y), 5)
equation_2 = sp.Eq((x - y), 5)
solution = sp.solve((equation_1, equation_2), (x, y))
print("Solution:", solution)
#Résultat: Solution: {x: 5, y: 0}

