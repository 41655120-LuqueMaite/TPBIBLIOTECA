def es_nombre_valido(nombre: str):
    for caracter in nombre:
        if caracter.isdigit():
            return False
    return True

def es_dni_valido(dni: str):
    if dni.isdigit() and (len(dni) == 7 or len(dni) == 8):
        return True
    else:
        return False

def es_isbn_valido(isbn: str):
    if isbn.isdigit():
        return True
    else:
        return False


class Miembro: 
    def __init__(self, dni: str, nombre: str):
        self.__dni = dni
        self.__nombre = nombre
        self.setDni(dni)
        self.setNombre(nombre)
        self.__libros_prestados = []

    def getDni(self):
        return self.__dni

    def setDni(self, dni: str):
        if es_dni_valido(dni):
            self.__dni = dni
            return True
        else:
            print("El DNI debe contener solo números y tener entre 7 y 8 dígitos.")
            return False

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre: str):
        if es_nombre_valido(nombre):
            self.__nombre = nombre
            return True
        else:
            print("El nombre no puede contener números.")
            return False

    def getLibrosPrestados(self):
        return self.__libros_prestados

    def agregarLibroPrestado(self, libro):
        self.__libros_prestados.append(libro)

    def quitarLibroPrestado(self, libro):
        if libro in self.__libros_prestados:
            self.__libros_prestados.remove(libro)


class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, ejemplar: int):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__ejemplar = ejemplar
        self.__disponible = True
        self.__prestado_a = []

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getIsbn(self):
        return self.__isbn

    def getEjemplar(self):
        return self.__ejemplar

    def setEjemplar(self, cantidad: int):
        self.__ejemplar = cantidad

    def getPrestadoA(self):
        return self.__prestado_a

    def estaDisponible(self):
        if len(self.__prestado_a) < self.__ejemplar:
            return True
        else:
            return False

    def prestar_libro(self, miembro):
        if self.estaDisponible():
            self.__prestado_a.append(miembro)

    def devolver_libro(self, miembro):
        if miembro in self.__prestado_a:
            self.__prestado_a.remove(miembro)


class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__miembros = []

    def getLibro(self, isbn):
        for libro in self.__libros:
            if libro.getIsbn() == isbn:
                return libro 
        return None

    def getMiembro(self, dni):
        for miembro in self.__miembros:
            if miembro.getDni() == dni:
                return miembro
        return None

    def agregarLibro(self):
        isbn = input("Ingrese el ISBN del libro: ")
        if es_isbn_valido(isbn) == False:
            print("El ISBN debe contener solo números.")
            return

        libro_existente = self.getLibro(isbn)

        if libro_existente != None:
            agregarejemplar = int(input("El libro ya existe. ¿Cuántos ejemplares desea agregar?: "))
            cant_actual = libro_existente.getEjemplar()
            libro_existente.setEjemplar(cant_actual + agregarejemplar)
            print("Ejemplares agregados con éxito.")
        else:
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            if es_nombre_valido(autor) == False:
                print("El nombre del autor no puede contener números.")
                return

            agregarejemplar = int(input("Ingrese la cantidad de ejemplares: "))
            libro = Libro(titulo, autor, isbn, agregarejemplar)
            self.__libros.append(libro)
            print("Libro registrado con éxito.")

    def quitarLibro(self):
        isbn = input("Ingrese el ISBN del libro a borrar: ")
        if es_isbn_valido(isbn) == False:
            print("El ISBN debe contener solo números.")
            return

        libroaBorrar = self.getLibro(isbn)
        if libroaBorrar != None:
            self.__libros.remove(libroaBorrar)
            print("Libro eliminado del sistema.")
        else:
            print("No se encontró un libro con ese ISBN.")

    def agregarMiembro(self):
        nombre = input("Ingrese el nombre del socio: ")
        if es_nombre_valido(nombre) == False:
            print("El nombre no puede contener números.")
            return

        dni = input("Ingrese el DNI del socio: ")
        if es_dni_valido(dni) == False:
            print("El DNI debe ser numérico y tener entre 7 y 8 dígitos.")
            return

        if self.getMiembro(dni) != None:
            print("Ya existe un miembro registrado con ese DNI.")
            return
        
        miembroobj = Miembro(dni, nombre)
        self.__miembros.append(miembroobj)
        print("Socio registrado con éxito.")

    def quitarMiembro(self):
        dni = input("Ingrese el DNI de la persona a borrar: ")
        personaaborrar = self.getMiembro(dni)
        if personaaborrar != None:
            if len(personaaborrar.getLibrosPrestados()) > 0:
                print("No se puede borrar el socio porque tiene libros prestados pendientes.")
                return
            else:
                self.__miembros.remove(personaaborrar)
                print("Socio eliminado con éxito.")
        else:
            print("No se encontró ningún socio con ese DNI.")

    def prestar_libro(self):
        dni = input("Ingrese el DNI del socio: ")
        isbn = input("Ingrese el ISBN del libro a prestar: ")
        if es_isbn_valido(isbn) == False:
            print("El ISBN debe contener solo números.")
            return

        libroaprestar = self.getLibro(isbn)
        if libroaprestar == None:
            print("El libro no existe.")
            return

        miembroaprestar = self.getMiembro(dni)
        if miembroaprestar == None:
            print("El miembro no existe.")
            return

        if libroaprestar.estaDisponible():
            libroaprestar.prestar_libro(miembroaprestar)
            miembroaprestar.agregarLibroPrestado(libroaprestar)
            print("Préstamo realizado con éxito.")
        else:
            print("No hay ejemplares disponibles de este libro.")

    def devolver_libro(self):
        dni = input("Ingrese el DNI del socio: ")
        isbn = input("Ingrese el ISBN del libro a devolver: ")
        if es_isbn_valido(isbn) == False:
            print("El ISBN debe contener solo números.")
            return

        libroaDevolver = self.getLibro(isbn)
        miembro = self.getMiembro(dni)

        if libroaDevolver == None or miembro == None:
            print("Datos incorrectos de libro o miembro.")
            return

        if miembro in libroaDevolver.getPrestadoA():
            libroaDevolver.devolver_libro(miembro)
            miembro.quitarLibroPrestado(libroaDevolver)
            print("Libro devuelto con éxito.")
        else:
            print("Ese miembro no tenía prestado este libro.")

    def mostrarLibros(self):
        if len(self.__libros) == 0:
            print("No hay libros registrados.")
            return
        else:
            print("ESTADO DE LIBROS")
            for l in self.__libros:
                disponibles = l.getEjemplar() - len(l.getPrestadoA())
                if l.estaDisponible():
                    estado = "Disponible"
                else:
                    estado = "No disponible"
                
                print("Título: " + l.getTitulo() + " | ISBN: " + l.getIsbn() + " | Estado: " + estado + " (" + str(disponibles) + "/" + str(l.getEjemplar()) + " disponibles)")
                
                if len(l.getPrestadoA()) > 0:
                    for socio in l.getPrestadoA():
                        print("Prestado a: " + socio.getNombre())

    def mostrarMiembros(self):
        if len(self.__miembros) == 0:
            print("No hay miembros registrados.")
            return
        else:
            print("ESTADO DE MIEMBROS")
            for m in self.__miembros:
                print("Socio: " + m.getNombre() + " DNI: " + m.getDni())
                if len(m.getLibrosPrestados()) > 0:
                    for libro in m.getLibrosPrestados():
                        print(" Libro prestado: " + libro.getTitulo())
                else:
                    print(" No tiene libros prestados ")

    def mostrarLibrosPrestadosAMiembro(self):
        dni = input("Ingrese el DNI del socio a consultar: ")
        miembro = self.getMiembro(dni)
        if miembro == None:
            print("No existe un socio con ese DNI.")
            return
        else:
            print("Libros prestados a " + miembro.getNombre() + ":")
            if len(miembro.getLibrosPrestados()) == 0:
                print("No posee libros prestados actualmente.")
            else:
                for l in miembro.getLibrosPrestados():
                    print( l.getTitulo() + " ISBN: " + l.getIsbn() )


def menu(): 
    print(" Sistema Biblioteca ")
    print("1- Agregar Libro")
    print("2- Quitar Libro")
    print("3- Agregar Miembro")
    print("4- Borrar Miembro")
    print("5- Prestar Libro")
    print("6- Devolver Libro")
    print("7- Mostrar Estado de Libros")
    print("8- Mostrar Estado de Miembros")
    print("9- Consultar Libros de un Miembro")
    print("10- Salir")
    return input("Seleccione una opción: ")


def main():
    biblioteca_urquiza = Biblioteca()
    while True:
        opcion = menu()

        if opcion == "10": 
            break
        elif opcion == "1":
            biblioteca_urquiza.agregarLibro()
        elif opcion == "2":
            biblioteca_urquiza.quitarLibro()
        elif opcion == "3":
            biblioteca_urquiza.agregarMiembro()
        elif opcion == "4":
            biblioteca_urquiza.quitarMiembro()
        elif opcion == "5":
            biblioteca_urquiza.prestar_libro()
        elif opcion == "6":
            biblioteca_urquiza.devolver_libro()
        elif opcion == "7":
            biblioteca_urquiza.mostrarLibros()
        elif opcion == "8":
            biblioteca_urquiza.mostrarMiembros()
        elif opcion == "9":
            biblioteca_urquiza.mostrarLibrosPrestadosAMiembro()

    print("Programa Terminado.")

main()