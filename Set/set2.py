ensemble1 = {1,2,3,4,"Martin"}
ensemble2= {1,4,5,6,"Martin"}

print("Union:",ensemble1.union(ensemble2))
print("Intersection:",ensemble1.intersection(ensemble2))
print("Différence:",ensemble1.difference(ensemble2))
print("Différence symétrique:",ensemble1.symmetric_difference(ensemble2))
# Résultats:
# Union: {1, 2, 3, 4, 5, 6, 'Martin'}
# Intersection: {1, 'Martin', 4}
# Différence: {2, 3}
# Différence symétrique: {2, 3, 5, 6}
