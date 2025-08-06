class Alumno:
    nombreApellido = None
    email = None
    matricula = None

    def __init__(self, nombreApellido, email, matricula):
        self.nombreApellido = nombreApellido
        self.email = email
        self.matricula = matricula
    
    def getInformacion(self):
        return f"alumno: {self.nombreApellido}, email {self.email}, matricula {self.matricula}"