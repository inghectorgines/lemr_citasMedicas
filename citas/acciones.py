import citas.cita as modelo

class Acciones:

    def crear(self, usuario):
        print(f"Ok Dr. {usuario[1]}!! Vamos a crear una nueva cita...")

        titulo = input("Introduce el titulo de tu cita: ")
        paciente = input("Introduce el paciente de tu cita: ")
        fechaCita = input("Introduce la fecha de la fecha de tu cita: ")

        cita = modelo.Cita(usuario[0], titulo, paciente, fechaCita)
        guardar = cita.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto! Has guardado la cita: {cita.titulo}")
        
        else:
            print(f"\nNo se ha registrado la cita correctamente, intentalo mas tarde: Dr. {usuario[1]}")

    def mostrar(self, usuario):
        print(f"\nDr. {usuario[1]}!! Estas son todas las citas registradas: ")

        cita = modelo.Cita(usuario[0])
        citas = cita.listar()

        #print(notas)

        for cita in citas:
            print("\n**********************************************")
            print(f"Titulo de la cita: {cita[2]}")
            print(f"Paciente: {cita[3]}")
            print(f"Fecha de la cita: {cita[4]}")
            print("**********************************************")

    def editar(self, usuario):
        print(f"\nDr. {usuario[1]}!!! editar tus citas")

        titulo = input("Introduce el titulo de la cita: ")

        print("""
        Acciones disponibles:
            - Editar titulo (titulo)
            - Editar paciente (paciente)
            - Editar fecha (fecha)
        """)

        tipoEdicion = input("¿Que campo va editar?: ")

        if tipoEdicion == "titulo":
            
            actualizacion = input("Introduce el nuevo titulo: ")

            cita = modelo.Cita(usuario[0], titulo)
            editar = cita.editarTitulo(actualizacion)
        elif tipoEdicion == "paciente":
            actualizacion = input("Introduce el paciente nuevo: ")

            cita = modelo.Cita(usuario[0], titulo)
            editar = cita.editarPaciente(actualizacion)
        elif tipoEdicion == "fecha":
            actualizacion = input("Introduce la nueva fecha: ")

            cita = modelo.Cita(usuario[0], titulo)
            editar = cita.editarFecha(actualizacion)

        if editar[0] >= 1:
            print(f"Se actualizo: {cita.titulo}")
        else:
            print("Cita no editada, prueba mas tarde")


    def borrar(self, usuario):
        print(f"\nDr. {usuario[1]}!!! Borrar tus citas")

        titulo = input("Introduce titulo de la cita a borrar: ")

        cita = modelo.Cita(usuario[0], titulo)
        eliminar = cita.eliminar()

        if eliminar[0] >= 1:
            print(f"Se borro tu nota: {cita.titulo}")
        else:
            print("Nota no eliminada, prueba mas tarde")