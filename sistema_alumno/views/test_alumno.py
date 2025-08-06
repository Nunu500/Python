import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.alumno_controller import AlumnoController
from models.alumno import Alumno
class TestAlumno:
    def __init__(self):
        self.ac = AlumnoController()
    def main(self):
     while True:
         os.system("cls" if os.name == "nt" else "clear")
         print("-------MENU-------")
         print("1. Cargar alumno")
         print("2. Ver alumno")
         print("4. Borrar alumno")
         print("5. Ver todo")
         print("6. Salir")
         resp = input("Opcion: ")
         if resp == "1":
            nombre = input("Nombre: ")
            email = input("Email: ")
            matricula = input("Matricula: ")
            self.ac.save(Alumno(nombre, email, matricula))
         elif resp == "5":
            for alu in self.ac.getAll():
               print(alu.getInformacion())

            input("Presione para continuar...")
         elif resp == "6":
            print("Bye")
            break
if __name__ == "__main__":
   vista = TestAlumno()
   vista.main()