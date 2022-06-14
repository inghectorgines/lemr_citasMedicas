from cmath import log
import doctores.doctor as modelo
import citas.acciones

class Acciones:

    def registro(self):
        print("Se procedera a realizar tu registro en el sistema...")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        instituto = input("¿Cual es el instituo al que pertenece?: ")
        consultorio = input("¿Cual es su consultorio?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")


        doctor = modelo.Doctor(nombre,apellidos, instituto, consultorio, email,password)
        registro = doctor.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto Dr. {registro[1].nombre} se ha registrado con el email {registro[1].email}")
        else:
            print("\nNo se ha registrado correctamente")

    def login(self):
        print("\nIdentificate en el sistema...")


        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        doctor = modelo.Doctor('', '', '', '', email, password)
        login = doctor.identificar()

        if email == login[5]:
            print(f"Bienvenido Dr. {login[1]}, te has registrado en el sistema el {login[7]}")
            self.proximasAcciones(login)
        

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
            - Crear cita (crear)
            - Mostrar citas (mostrar)
            - Editar cita (editar)
            - Eliminar cita (eliminar)
            - Salir (salir)
        """)

        accion = input("¿Que quieres hacer?: ")
        hazEl = citas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "editar":
            hazEl.editar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            exit()

        return None
        