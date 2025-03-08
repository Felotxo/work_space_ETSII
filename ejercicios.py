x = int(input("introduce un numero a: "))
y = int(input("introduce un numero b: "))
if x < y:
        print("el numero menor es: ", x)
elif x == y:
        print("a y b son iguales")
else:
        print("el numero menor es: ", y)


from random import shuffle
x = ["skyrim", "pertenece", "a", "los", "nordicos"]
shuffle(x)
print(x)
