d = {"02540859" : 37 , "22851463" : 82}  # creamos un diccionario
texto = input("introduce un DNI")
if texto in d: #comprobamos si esta en el diccionario
    print("la edad de " + texto + " es " + str(d[texto]))
else:
    edad = input("Documento no existe. Introduzca edad")
    if edad.isnumeric():
        num = int(edad)
        d[texto] = num
        print("añadido al diccionario")
print(d) #mostramos por pantalla el diccionario
