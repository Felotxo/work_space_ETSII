def divide(x,y):
    try:
        resultado = x/y
    except ZeroDivisionError:
        print("no se puede dividir por cero")
    else:
        print("El resultado es: ")
    finally:
        print("Ejecutando el finally.")

divide(4,0)

divide(12,3)