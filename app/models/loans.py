from datetime import timedelta
from .db import get_connection

mydb = get_connection()

class Loan:
    def __init__(self, id_prestamo=None, id_cliente=None, monto=None, interes=None, monto_total=None, 
                 plazo=None, estado='Pendiente', fecha_inicio=None, fecha_vencimiento=None, **kwargs):
        self.id_prestamo = id_prestamo
        self.id_cliente = id_cliente
        self.monto = monto
        self.interes = interes
        self.monto_total = monto_total
        self.plazo = plazo
        self.estado = estado
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        # kwargs permite manejar columnas adicionales no definidas explícitamente
        self.extra_attributes = kwargs

    @staticmethod
    def get_all():
        with get_connection() as mydb:
            with mydb.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM prestamos")
                prestamos = cursor.fetchall()
        return prestamos

    @staticmethod
    def get_by_id(id_prestamo):
        try:
            mydb = get_connection()
            with mydb.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM prestamos WHERE id_prestamo = %s", (id_prestamo,))
                prestamo_data = cursor.fetchone()

            if prestamo_data:
                # Convertir el diccionario en una instancia de Loan
                return Loan(
                    id_prestamo=prestamo_data['id_prestamo'],
                    id_cliente=prestamo_data['id_cliente'],
                    monto=prestamo_data['monto'],
                    interes=prestamo_data['interes'],
                    monto_total=prestamo_data['monto_total'],
                    plazo=prestamo_data['plazo'],
                    estado=prestamo_data['estado'],
                    fecha_inicio=prestamo_data['fecha_inicio'],
                    fecha_vencimiento=prestamo_data['fecha_vencimiento']
                )
            return None  # Si no se encuentra el préstamo
        except Exception as e:
            # Manejo de excepciones
            print(f"Error al obtener el préstamo: {e}")
            return None

    def save(self):
        try:
            with get_connection() as mydb:
                with mydb.cursor() as cursor:
                    if self.id_prestamo:
                        # Update existing loan
                        query = """
                            UPDATE prestamos 
                            SET id_cliente = %s, monto = %s, interes = %s, monto_total = %s, 
                                plazo = %s, estado = %s, fecha_inicio = %s, fecha_vencimiento = %s
                            WHERE id_prestamo = %s
                        """
                        cursor.execute(query, (self.id_cliente, self.monto, self.interes, self.monto_total,
                                            self.plazo, self.estado, self.fecha_inicio, self.fecha_vencimiento, self.id_prestamo))
                    else:
                        # Insert new loan
                        query = """
                            INSERT INTO prestamos (id_cliente, monto, interes, monto_total, plazo, estado, fecha_inicio, fecha_vencimiento)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        """
                        cursor.execute(query, (self.id_cliente, self.monto, self.interes, self.monto_total,
                                            self.plazo, self.estado, self.fecha_inicio, self.fecha_vencimiento))
                        self.id_prestamo = cursor.lastrowid
                mydb.commit()
            return True
        except Exception as e:
            print(f"Error al guardar el préstamo: {e}")
            return False

    @staticmethod
    def delete(id_prestamo):
        try:
            with get_connection() as mydb:
                with mydb.cursor() as cursor:
                    cursor.execute("DELETE FROM prestamos WHERE id_prestamo = %s", (id_prestamo,))
                mydb.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar el préstamo: {e}")
            return False

    @staticmethod
    def get_prestamos_pendientes():
        try:
            with get_connection() as mydb:
                with mydb.cursor(dictionary=True) as cursor:
                    sql = "SELECT * FROM vista_prestamos WHERE estado = 'Pendiente'"
                    cursor.execute(sql)
                    result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error al obtener préstamos pendientes: {e}")
            return []
        
    @staticmethod
    def get_prestamos():
        try:
            with get_connection() as mydb:
                with mydb.cursor(dictionary=True) as cursor:
                    sql = "SELECT * FROM vista_prestamos WHERE estado = 'Activo'"
                    cursor.execute(sql)
                    result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error al obtener préstamos: {e}")
            return []
        
    @staticmethod
    def get_by_user_id(id_cliente):
        """Obtiene un préstamo asociado a un cliente específico."""
        mydb = get_connection()
        with mydb.cursor(dictionary=True) as cursor:
            query = """
                SELECT * 
                FROM prestamos 
                WHERE id_cliente = %s
                ORDER BY id_prestamo DESC LIMIT 1
            """
            cursor.execute(query, (id_cliente,))
            result = cursor.fetchone()  # Devuelve el último préstamo encontrado o None
        return Loan(**result) if result else None
    
    def calcular_fechas_pago(self):
        """
        Calcula las fechas de pago mensuales basándose en la fecha de inicio y el plazo del préstamo.
        """
        if not self.fecha_inicio or not self.plazo:
            return []
        
        fechas_pago = []
        fecha_actual = self.fecha_inicio
        for _ in range(self.plazo):
            fecha_actual += timedelta(days=30) # Asumiendo 30 días por mes
            fechas_pago.append(fecha_actual)
        return fechas_pago