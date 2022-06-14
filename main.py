#Print de datos
print("Alumno: Luis Enrique Montiel Rojas")

"""
Proyecto python + MySQL:
1.1. Crear tu sistema de Cita Médica (en la clase main, sin interfaz).
1.2. Debe de contener los módulos y paquetes separados de acuerdo a la funcinalidad, como lo vimos en clases.
1.3. Debe de haber la opción de registro del doctor(a), no. consultorio, y demas datos que concideres necesarios.
1.4. Debe permitir registar una consulta, borrar, eliminar, modificar y listar consultas.
1.5. El nombre del proyecto debe de empezar con sus iniciales de su nombre completo, script, y nombre su BD (ejemplo: hbog_).
"""
from doctores import acciones

print("""
Acciones disponibles:
    - Registro de Doctores (registro)
    - Login de Doctores (login)
""")

hazEl = acciones.Acciones()

accion = input("¿Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()
    
elif accion == "login":
    hazEl.login()