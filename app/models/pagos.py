from .db import get_connection

class Pago:
    def __init__(self, id_pago=None, id_prestamo=None, monto_pagado=None, fecha_pago=None, 
                 metodo_pago=None, saldo_restante=None):
        self.id_pago = id_pago
        self.id_prestamo = id_prestamo
        self.monto_pagado = monto_pagado
        self.fecha_pago = fecha_pago
        self.metodo_pago = metodo_pago
        self.saldo_restante = saldo_restante

    @staticmethod
    def get_all():
        mydb = get_connection()
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pagos")
        pagos = cursor.fetchall()
        cursor.close()
        return pagos

    @staticmethod
    def get_by_id(id_pago):
        mydb = get_connection()
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pagos WHERE id_pago = %s", (id_pago,))
        pago = cursor.fetchone()
        cursor.close()
        return pago

    def save(self):
        mydb = get_connection()
        cursor = mydb.cursor()
        if self.id_pago:
            # Update existing payment
            query = """
                UPDATE pagos 
                SET id_prestamo = %s, monto_pagado = %s, fecha_pago = %s, 
                    metodo_pago = %s, saldo_restante = %s
                WHERE id_pago = %s
            """
            cursor.execute(query, (self.id_prestamo, self.monto_pagado, self.fecha_pago,
                                   self.metodo_pago, self.saldo_restante, self.id_pago))
        else:
            # Insert new payment
            query = """
                INSERT INTO pagos (id_prestamo, monto_pagado, fecha_pago, metodo_pago, saldo_restante)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (self.id_prestamo, self.monto_pagado, self.fecha_pago,
                                   self.metodo_pago, self.saldo_restante))
            self.id_pago = cursor.lastrowid
        mydb.commit()
        cursor.close()

    @staticmethod
    def delete(id_pago):
        mydb = get_connection()
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM pagos WHERE id_pago = %s", (id_pago,))
        mydb.commit()
        cursor.close()