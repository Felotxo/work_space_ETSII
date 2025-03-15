# ejercicio final Sistema de Gestion de Biblioteca, realizado por Felix Perez. 

# CREAMOS UNA CLASE LIBRO CON LOS ATRIBUTOS TITULO, AUTOR, ISBN Y DISPONIIBLE

class Libro():
# DEFINIENDO LOS ATRIBUTOS DEL LIBRO
    def __init__(self,titulo,autor,isbn,disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
# definimos el metodo str para que nos muestre los atributos del libro
    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Disponible: {self.disponible}" 

    # defino la lista biblioteca
biblioteca = []

# desarrollo los metodos para agregar, prestar, devolver, mostrar, buscar y salir del sistema

def agregar():     
        titulo = input("Que titulo tiene el libro: ")
        autor = input("Quien es el autor: ")
        isbn = input("Cual es el ISBN: ")
    
    # Creamos una instancia de Libro y la agregamos a la lista
        libro = Libro(titulo, autor, isbn)
        biblioteca.append(libro)
        print("¡Libro agregado correctamente!")


def prestar():
    isbn = input("Escriba el ISBN del libro que desea: ")
    
    for libro in biblioteca:
        if libro.isbn == isbn:
            if not libro.disponible:
                    print("El libro no está disponible.")
            else:
                libro.disponible = False
                print(f"Libro '{libro.titulo}' prestado correctamente.")
            return
        print("libro no encontrado")
        
def devolver():
    isbn = input("Escriba el ISBN del libro a devolver: ")
    
    for libro in biblioteca:
        if libro.isbn == isbn:
            if not libro.disponible:
                libro.disponible = True
                print(f"Libro '{libro.titulo}' devuelto correctamente.")
            else:
                print("El libro ya estaba disponible.")
            return
        print("Libro no encontrado.")
    
def mostrar():
    if not biblioteca:
        print("No hay libros en la biblioteca.")
    else:
        for libro in biblioteca:
            print(libro)

def buscar():

    titulo = input("Que libro quiere buscar?: ")
    
    # ejecutamos un bucle determinado para que busque en la lista biblioteca si tenemos el libro
    for libro in biblioteca:
        # lower para no discriminar may y min 
        if libro.titulo.lower() == titulo.lower():
            print("Libro encontrado:", "titulo del libro: ", libro.titulo, "Autor :", libro.autor,"isbn :", libro.isbn,"disponible: ", libro.disponible) 
            break 
    else:      
        print("Libro no encontrado.")

def salir():
    print("Que tenga un bonito dia")
    exit()

def main():
    while True:
        print("\n Bienvenido al sistema de Gestion de Biblioteca")
        print("1. Agregar Libro")
        print("2. Prestar Libro")
        print("3. Devolver Libro")
        print("4. Mostrar Libros")
        print("5. Buscar")
        print("6. Salir del Sistema")
    
        opcion = int(input("Elija una opcion por favor: "))

        if opcion == 1:
            agregar()
                         
        elif opcion == 2:
            prestar()
        
        elif opcion == 3:
            devolver()
                
        elif opcion == 4:
            mostrar()

        elif opcion == 5:
            buscar()

        elif opcion == 6:
            salir()

        else:
            print("la opcion introducida no es valida. Solo del 1 al 6.")

if __name__ == "__main__":
    main() 





    
                


    