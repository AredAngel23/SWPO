from .db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash

mydb = get_connection()

class User:

    def __init__(self,
                 nombre,
                 ape_pat,
                 ape_mat,
                 id_genero,
                 fecha_nacimiento,
                 id_nivelEdu,
                 id_ocupacion,
                 ingresos_mensuales,
                 curp,
                 tel_cel,
                 tel_casa,
                 email,
                 password,
                 rol='cliente',
                 is_approved=0,
                 id_usuario = None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.ape_pat = ape_pat
        self.ape_mat = ape_mat
        self.id_genero = id_genero
        self.fecha_nacimiento = fecha_nacimiento
        self.id_nivelEdu = id_nivelEdu
        self.id_ocupacion = id_ocupacion
        self.ingresos_mensuales = ingresos_mensuales
        self.curp = curp
        self.tel_cel = tel_cel
        self.tel_casa = tel_casa
        self.email = email
        self.rol = rol
        self.password = password
        self.is_approved = is_approved

    def save(self):
        if self.id_usuario is None:
            # Insertar un nuevo usuario
            with mydb.cursor() as cursor:
                # Hasheamos la contraseña antes de guardar
                self.password = generate_password_hash(self.password, method='pbkdf2:sha256', salt_length=8)
                sql = """
                    INSERT INTO clientes 
                    (nombre, ape_pat, ape_mat, id_genero, fecha_nacimiento, id_nivelEdu, id_ocupacion, 
                    ingresos_mensuales, curp, tel_cel, tel_casa, email, password, is_approved) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                val = (
                    self.nombre, self.ape_pat, self.ape_mat, self.id_genero, self.fecha_nacimiento, 
                    self.id_nivelEdu, self.id_ocupacion, self.ingresos_mensuales, self.curp, 
                    self.tel_cel, self.tel_casa, self.email, self.password, self.is_approved
                )
                cursor.execute(sql, val)
                mydb.commit()
                self.id_usuario = cursor.lastrowid
                return self.id_usuario
        else:
            # Actualizar un usuario existente
            with mydb.cursor() as cursor:
                sql = """
                    UPDATE clientes 
                    SET nombre = %s, ape_pat = %s, ape_mat = %s, id_genero = %s, fecha_nacimiento = %s, 
                    id_nivelEdu = %s, id_ocupacion = %s, ingresos_mensuales = %s, curp = %s, 
                    tel_cel = %s, tel_casa = %s, is_approved = %s
                    WHERE id_usuario = %s
                """
                val = (
                    self.nombre, self.ape_pat, self.ape_mat, self.id_genero, self.fecha_nacimiento, 
                    self.id_nivelEdu, self.id_ocupacion, self.ingresos_mensuales, self.curp, 
                    self.tel_cel, self.tel_casa, self.is_approved, self.id_usuario
                )
                cursor.execute(sql, val)
                mydb.commit()
                return self.id_usuario
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM clientes WHERE id_usuario = { self.id_usuario }"
            cursor.execute(sql)
            mydb.commit()
            return self.id_usuario
        
    @staticmethod
    def __get__(id_usuario):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM clientes WHERE id_usuario = { id_usuario }"
            cursor.execute(sql)

            user = cursor.fetchone()

            if user:
                user = User(nombre=user["nombre"], 
                            ape_pat=user["ape_pat"], 
                            ape_mat=user["ape_mat"], 
                            id_genero=user["id_genero"], 
                            fecha_nacimiento=user["fecha_nacimiento"], 
                            id_nivelEdu=user["id_nivelEdu"], 
                            id_ocupacion=user["id_ocupacion"],
                            ingresos_mensuales=user["ingresos_mensuales"],
                            curp=user["curp"],
                            tel_cel=user["tel_cel"],
                            tel_casa=user["tel_casa"],
                            email=user["email"],
                            password=user["password"],
                            rol=user['rol'],
                            id_usuario=id_usuario,
                            is_approved=user["is_approved"])
                return user
            
            return None
        
    @staticmethod
    def get_clients():
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM vistaclientes"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        
    @staticmethod
    def get_users():
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM vistausuarios"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        
    @staticmethod
    def check_email(email):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM clientes WHERE email = '{ email }'"
            cursor.execute(sql)

            user = cursor.fetchone()

            if user:
                return 'User exist'
            else:
                return None
            
    @staticmethod
    def get_by_password(email, password):
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT id_usuario, email, password FROM clientes WHERE email = %s"
            val = (email,)
            cursor.execute(sql, val)
            user = cursor.fetchone()
            
            if user != None:
                if check_password_hash(user["password"], password):
                    return User.__get__(user["id_usuario"])
            return None
          
    @staticmethod
    def get_genero():
        with mydb.cursor() as cursor:
            sql = f"SELECT * FROM genero"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result

    @staticmethod
    def get_nivelEdu():
        with mydb.cursor() as cursor:
            sql = f"SELECT * FROM nivel_educativo"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
        
    @staticmethod
    def get_ocupacion():
        with mydb.cursor() as cursor:
            sql = f"SELECT * FROM ocupacion"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
    
    def change_password(self, old_password, new_password):
        with mydb.cursor() as cursor:
            # Primero, recuperar la contraseña almacenada en la base de datos
            sql = "SELECT password FROM clientes WHERE id_usuario = %s"
            cursor.execute(sql, (self.id_usuario,))
            result = cursor.fetchone()

            if result is not None:
                stored_password = result[0]

                # Verificar si la contraseña actual proporcionada es correcta
                if check_password_hash(stored_password, old_password):
                    # Si es correcta, encriptar la nueva contraseña
                    new_hashed_password = generate_password_hash(new_password, method='pbkdf2:sha256', salt_length=8)

                    # Actualizar la contraseña en la base de datos
                    update_sql = "UPDATE clientes SET password = %s WHERE id_usuario = %s"
                    cursor.execute(update_sql, (new_hashed_password, self.id_usuario))
                    mydb.commit()
                    return "Contraseña actualizada exitosamente"
                else:
                    return "La contraseña actual es incorrecta"
            else:
                return "Usuario no encontrado"
            
    def has_address(self):
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT COUNT(*) AS count FROM domicilio WHERE id_cliente = %s"
            val = (self.id_usuario,)
            cursor.execute(sql, val)
            result = cursor.fetchone()
            return result['count'] > 0
    
    # Importación diferida dentro del método o función donde se use Address
    def get_address(self):
        from models.address import Address
        with mydb.cursor(dictionary=True) as cursor:
                sql = "SELECT * FROM domicilio WHERE id_cliente = %s LIMIT 1"
                val = (self.id_usuario,)
                cursor.execute(sql, val)

                address = cursor.fetchone()

                if address:
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
                
                return None
        
        # from models.address import Address
        # with mydb.cursor(dictionary=True) as cursor:
        #     sql = "SELECT * FROM domicilio WHERE id_cliente = %s LIMIT 1"
        #     val = (self.id_usuario,)
        #     cursor.execute(sql, val)    
        #     result = cursor.fetchone()
        #     if result:
        #         return Address(**result)
        #     return None