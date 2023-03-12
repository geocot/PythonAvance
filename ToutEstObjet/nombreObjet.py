distance = 100
distance = distance.__add__(200)
print(distance)
#Résultat = 300

#----------------------------------------------------
import numbers
print(isinstance(10,numbers.Number)) #Résultat True
print(isinstance(10.5,numbers.Number)) #Résultat True
print(isinstance("Allo!",numbers.Number)) #Résultat False

print(isinstance(10,float)) #Résultat False
print(isinstance(10.5,float)) #Résultat True

