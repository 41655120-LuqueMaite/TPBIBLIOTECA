class Estudiantes:
    def __init__ (self , nombreyap:str, nmatricula:int, carrera:str):
        self.__nombreyap = nombreyap
        self.__nmatricula = nmatricula 
        self.__carrera = carrera
        self.cursos_inscritos = []

    def getnombre(self):
        return self.__nombreyap

    def getmatricula(self):
        return self.__nmatricula

    def getcarrera(self):
        return self.__carrera


class Cursos:
    def __init__ (self , nombrecurso:str, codigocurso:int, profencargado:str, cantmax:int):
        self.__nombrecurso = nombrecurso
        self.__codigocurso = codigocurso
        self.__profencargado = profencargado
        self.__cantmax = cantmax
        self.alumnos_inscriptos = []

    def getnombrecurso(self):
        return self.__nombrecurso

    def getcodigocurso(self):
        return self.__codigocurso

    def getprofencargado(self):
        return self.__profencargado

    def getcantmax(self):
        return self.__cantmax

class SistemaFacultad: 
    def __init__(self):
        self.estudiantes:list[Estudiantes]=[]
        self.cursos:list[Cursos]=[]

    def AgregarEstudiante(self):
        while True:
            nombreyap = input("Ingrese Nombre y Apellido del estudiante a ingresar: ")
            if nombreyap == "":
                print("Error: El nombre no puede estar vacío.")
            else:
                tiene_numero = False
                for caracter in nombreyap:
                    if caracter in "0123456789":
                        tiene_numero = True
                if tiene_numero:
                    print("El nombre y apellido no puede contener números. Intente de nuevo.")
                else:
                    break 
        while True:
            matricula_input = input("Ingrese matricula correspondiente: ")
            if not matricula_input.isdigit():
                print("Error: La matrícula debe contener solo números. Intente de nuevo.")
            else:
                nmatricula = int(matricula_input)
                if self.buscar_estudiante(nmatricula) is not None:
                    print("Ya existe un estudiante registrado con la matrícula", nmatricula)
                else:
                    break

        print("Seleccione la carrera del estudiante:")
        print("1- Análisis Funcional de Sistemas Informáticos")
        print("2- Desarrollo de Software")
        print("3- Infraestructura de la Información")
        
        while True:
            opcion_carrera = input("Ingrese una opción (1-3): ")
            if opcion_carrera == "1":
                carrera = "Análisis Funcional de Sistemas Informáticos"
                break
            elif opcion_carrera == "2":
                carrera = "Desarrollo de Software"
                break
            elif opcion_carrera == "3":
                carrera = "Infraestructura de la Información"
                break
            else:
                print("Opción inválida. Debe ingresar 1, 2 o 3.")

        nuevo_estudiante = Estudiantes(nombreyap, nmatricula, carrera)
        self.estudiantes.append(nuevo_estudiante)
        print("El estudiante se agregó con éxito.")

    def AgregarCurso(self):
        while True:
            nombrecurso = input("Ingrese el nombre del curso a agregar: ")
            if nombrecurso == "":
                print("Error: El nombre del curso no puede estar vacío.")
            else:
                break
        while True:
            codigo_input = input("Ingrese el codigo del curso correspondiente: ")
            if not codigo_input.isdigit():
                print("Error: El código debe contener solo números. Intente de nuevo.")
            else:
                codigocurso = int(codigo_input)
                if self.buscar_curso(codigocurso) is not None:
                    print("Ya existe un curso registrado con el código", codigocurso)
                else:
                    break

        profencargado = input("Ingrese el profesor/a encargado/a del curso: ")
        
        while True:
            cantmax_input = input("Ingrese la capacidad maxima de alumnos que puede tener el curso: ")
            if not cantmax_input.isdigit():
                print("Error: La capacidad debe ser un número entero. Intente de nuevo.")
            else:
                cantmax = int(cantmax_input)
                break
        
        nuevo_curso = Cursos(nombrecurso, codigocurso, profencargado, cantmax)
        self.cursos.append(nuevo_curso)
        print("El curso se agregó con éxito.")

    def buscar_estudiante(self, matricula: int):
        for matricest in self.estudiantes:
            if matricest.getmatricula() == matricula:
                return matricest
        return None 

    def buscar_curso(self, codigo: int):
        for codclase in self.cursos:
            if codclase.getcodigocurso() == codigo:
                return codclase
        return None
    
    def InscribirEstACurso(self):
        matricula_input = input("Ingrese la matricula del estudiante: ")
        codigo_input = input("Ingrese el codigo del curso: ")

        if not matricula_input.isdigit() or not codigo_input.isdigit():
            print("Error: La matrícula y el código deben ser números.")
            return

        nmatricula = int(matricula_input)
        codigocurso = int(codigo_input)

        estudiante = self.buscar_estudiante(nmatricula)
        curso = self.buscar_curso(codigocurso)

        if estudiante is None:
            print("No se encontró ningún estudiante con esa matrícula.")
            return

        if curso is None:
            print("No se encontró ningún curso con ese código.")
            return

        if len(curso.alumnos_inscriptos) >= curso.getcantmax():
            print("El curso ya alcanzó su capacidad máxima de alumnos.")
            return
        
        else:
            curso.alumnos_inscriptos.append(estudiante)
            estudiante.cursos_inscritos.append(curso)
            print("Estudiante:", estudiante.getnombre(), "Matrícula:", estudiante.getmatricula(), "fue inscripto/a correctamente" )

    def BajaCurso(self):
        matricula_input = input("Ingrese la matricula del estudiante a dar de baja: ")
        codigo_input = input("Ingrese el codigo del curso: ")

        if not matricula_input.isdigit() or not codigo_input.isdigit():
            print("Error: La matrícula y el código deben ser números.")
            return

        nmatricula = int(matricula_input)
        codigocurso = int(codigo_input)

        estudiante = self.buscar_estudiante(nmatricula)
        curso = self.buscar_curso(codigocurso)

        if estudiante is None:
            print(" No se encontró ningún estudiante con esa matrícula.")
            return

        if curso is None:
            print("No se encontró ningún curso con ese código.")
            return

        if curso not in estudiante.cursos_inscritos:
            print("El estudiante no estába inscripto en el curso.")
            return

        else:
            curso.alumnos_inscriptos.remove(estudiante)
            estudiante.cursos_inscritos.remove(curso)
            print("El estudiante con el siguiente numero de matricula", nmatricula, "se ha dado de baja del curso con el siguiente codigo ", codigocurso)

    def ConsultarEstadoCursos(self):
        if not self.cursos:
            print("No hay cursos registrados en el sistema.")
            return

        print("ESTADO DE CURSOS")
        for curso in self.cursos:
            inscriptos = len(curso.alumnos_inscriptos)
            disponibles = curso.getcantmax() - inscriptos
            
            print("Curso:", curso.getnombrecurso(), "Código:", curso.getcodigocurso())
            print("  Profesor:", curso.getprofencargado())
            print("  Inscriptos:", inscriptos, "/ Capacidad Máxima:", curso.getcantmax())
            print("  Cupos disponibles:", disponibles)

    def ConsultarEstadoEstudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados en el sistema.")
            return

        print("ESTADO DE ESTUDIANTES")
        for estudiante in self.estudiantes:
            print("Estudiante:", estudiante.getnombre(), "Matrícula:", estudiante.getmatricula(), )
            print("  Carrera:", estudiante.getcarrera())
            
            if estudiante.cursos_inscritos:
                print("  Cursos inscriptos:")
                for curso in estudiante.cursos_inscritos:
                    print("-", curso.getnombrecurso())
            else:
                print("  Cursos inscriptos: Ninguno")

def main():
    facultad = SistemaFacultad()
    while True:
        opcion = menu()

        if opcion == "7":
            break
        elif opcion == "1":
            facultad.AgregarEstudiante()
        elif opcion == "2":
            facultad.AgregarCurso()
        elif opcion == "3":
            facultad.InscribirEstACurso()
        elif opcion == "4":
            facultad.BajaCurso()
        elif opcion == "5":
            facultad.ConsultarEstadoCursos()
        elif opcion == "6":
            facultad.ConsultarEstadoEstudiantes()

    print("Programa Terminado")


def menu():
    print("Sistema de Gestion de Facultad:")
    print("1-Agregar Estudiante:")
    print("2-Agregar Curso:")
    print("3-Inscribir Estudiante a Curso:")
    print("4-Dar de Baja Estudiante de Curso:")
    print("5-Consultar Estado de Cursos:")
    print("6-Consultar Estado de Estudiantes:")
    print("7-Salir:")

    return input("Seleccione una opcion: ")


main()