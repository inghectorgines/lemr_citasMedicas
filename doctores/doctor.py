import mysql.connector
import datetime
import hashlib
import doctores.conexion as conexion

#llamar la clase de la conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Doctor:
    
    def __init__(self, nombre, apellidos, instituto, consultorio, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.instituto = instituto
        self.consultorio = consultorio
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        #cifrar contraseñas
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO doctores VALUES(null, %s, %s, %s, %s, %s, %s, %s)"
        doctor = (self.nombre, self.apellidos, self.instituto, self.consultorio, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, doctor)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0,self]
        
        return result

    def identificar(self):
        # Login de usuarios
        sql = "SELECT * FROM doctores WHERE email = %s AND password = %s"

        #cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #datos para consulta
        doctor = (self.email, cifrado.hexdigest())

        cursor.execute(sql, doctor)
        result = cursor.fetchone()

        return result