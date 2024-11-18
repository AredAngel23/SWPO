import mysql
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
                sql = """
                    INSERT INTO domicilio 
                    (id_estado, municipio, cp, tipo_asen, asentamiento, calle, num_ext, num_int, id_cliente) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                val = (
                    self.id_estado, self.municipio, self.cp, self.tipo_asen, self.asentamiento, self.calle,
                    self.num_ext, self.num_int, self.id_cliente
                )
                cursor.execute(sql, val)
                mydb.commit()
                self.id_domicilio = cursor.lastrowid
                return self.id_domicilio
        else:
            # Aactualizar el domicilio
            with mydb.cursor() as cursor:
                sql = """
                    UPDATE domicilio
                    SET id_estado = %s, municipio = %s, cp = %s, tipo_asen = %s, asentamiento = %s,
                    calle = %s, num_ext = %s, num_int = %s, id_cliente = %s 
                    WHERE id_domicilio = %s
                """
                val = (
                    self.id_estado, self.municipio, self.cp, self.tipo_asen, self.asentamiento,
                    self.calle, self.num_ext, self.num_int, self.id_cliente, self.id_domicilio
                )
                cursor.execute(sql, val)
                mydb.commit()
                return self.id_domicilio
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM domicilio WHERE id_domicilio = { self.id_domicilio }"
            cursor.execute(sql)
            mydb.commit()
            return self.id_domicilio
            
    @staticmethod
    def get_by_cliente_id(id_cliente):
        try:
            with mydb.cursor(dictionary=True) as cursor:
                # Ejecuta la consulta
                sql = "SELECT * FROM domicilio WHERE id_cliente = %s"
                cursor.execute(sql, (id_cliente,))

                address = cursor.fetchone()

                if address:
                    # Crea y retorna la instancia de Address si existe el resultado
                    address = Address(id_estado=address['id_estado'],
                                    municipio=address['municipio'],
                                    cp=address['cp'],
                                    tipo_asen=address['tipo_asen'],
                                    asentamiento=address['asentamiento'],
                                    calle=address['calle'],
                                    num_ext=address['num_ext'],
                                    num_int=address['num_int'],
                                    id_cliente=address['id_cliente'],
                                    id_domicilio=address['id_domicilio'])
                    return address
                else:
                    return None
        except mysql.connector.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None
        
    @staticmethod
    def get_estado():
        with mydb.cursor() as cursor:
            sql = f"SELECT * FROM estados"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result

    @staticmethod
    def get_tipo_asentamiento():
        with mydb.cursor() as cursor:
            sql = f"SELECT * FROM tipos_asen"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
        
    @staticmethod
    def get_address(id_cliente):
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM vista_domicilioxcliente WHERE id_cliente = %s LIMIT 1"
            cursor.execute(sql,(id_cliente,))
            result = cursor.fetchone()
            return result