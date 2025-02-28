l = list()      #Creamos una lista vacia
texto = input("introduce un numero entero: ")
if texto.isnumeric(): #comprueba si son numeros 
    num = int(texto)
    l.append(num)  
    print("numero entero introducido " + str(num) + " añadido a la lista")
else:
    print("no has introducido ningun numero entero")
    






