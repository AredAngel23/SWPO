from .db import get_connection

mydb = get_connection()

class Address:

    def __init__(self, id_estado, municipio, cp, tipo_asen, asentamiento, calle, num_ext, num_int, id_cliente=1, id_domicilio = None):
        self.id_domicilio = id_domicilio
        self.id_estado = id_estado
        self.municipio = municipio
        self.cp = cp
        self.tipo_asen = tipo_asen
        self.asentamiento = asentamiento
        self.calle = calle
        self.num_ext = num_ext
        self.num_int = num_int
        self.id_cliente = id_cliente

    def save(self):
        if self.id_domicilio is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO domicilio (id_estado, municipio, cp, tipo_asen, asentamiento, calle, num_ext, num_int, id_cliente) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (self.id_estado, self.municipio, self.cp, self.tipo_asen, self.asentamiento, self.calle, self.num_ext, self.num_int, self.id_cliente)
                cursor.execute(sql, val)
                mydb.commit()
                self.id_domicilio = cursor.lastrowid
                return self.id_domicilio    
            
    @staticmethod
    def get_estado():
        with mydb.cursor() as cursor:
            sql = f"SELECT * FROM estados"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result

    @staticmethod
    def get_tipo_asentamineto():
        with mydb.cursor() as cursor:
            sql = f"SELECT * FROM tipos_asen"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result