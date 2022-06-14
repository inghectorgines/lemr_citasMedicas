import doctores.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Cita:

    def __init__(self, doctor_id, titulo="", paciente="", fechaCita=""):
        self.doctor_id = doctor_id
        self.titulo = titulo
        self.paciente = paciente
        self.fechaCita = fechaCita

    def guardar(self):
        sql = "INSERT INTO citas VALUES(null, %s, %s, %s, %s, NOW())"
        cita = (self.doctor_id, self.titulo, self.paciente, self.fechaCita)

        cursor.execute(sql, cita)
        database.commit()

        return [cursor.rowcount, self]

    def listar(self):
        sql = f"SELECT * FROM citas WHERE doctor_id = {self.doctor_id}"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def eliminar(self):
        sql = f"DELETE FROM citas WHERE doctor_id = {self.doctor_id} AND titulo LIKE '%{self.titulo}%'"

        cursor.execute(sql)
        database.commit()

        return[cursor.rowcount, self]

    def editarTitulo(self, actualizacion):
        sql = f"UPDATE citas SET titulo = '{actualizacion}' WHERE titulo LIKE '%{self.titulo}%' AND doctor_id = '{self.doctor_id}'"
        cursor.execute(sql)
        database.commit()

        return[cursor.rowcount, self]

    def editarPaciente(self, actualizacion):
        sql = f"UPDATE citas SET paciente = '{actualizacion}' WHERE titulo LIKE '%{self.titulo}%' AND doctor_id = '{self.doctor_id}'"
        cursor.execute(sql)
        database.commit()

        return[cursor.rowcount, self]

    def editarFecha(self, actualizacion):
        sql = f"UPDATE citas SET fechaCita = '{actualizacion}' WHERE titulo LIKE '%{self.titulo}%' AND doctor_id = '{self.doctor_id}'"
        cursor.execute(sql)
        database.commit()

        return[cursor.rowcount, self]