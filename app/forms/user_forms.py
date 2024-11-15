from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TelField, PasswordField, EmailField, SelectField, ValidationError, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange, Optional, Regexp

from models.users import User

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(message='Ingresa tu correo'), Email()])
    password = PasswordField('Password', validators=[DataRequired(message='Ingresa tu contraseña')])
    submit = SubmitField('Ingresar')

class RegisterForm(FlaskForm):
    nombre = StringField("Nombre: ", validators=[DataRequired(), Length(min=4, max=25)])
    ape_pat = StringField("Apellido Paterno: ", validators=[DataRequired(), Length(min=4, max=25)])      
    ape_mat = StringField("Apellido Materno: ", validators=[DataRequired(), Length(min=4, max=25)])
    genero = User.get_genero()
    id_genero = SelectField("Género: ", 
                            choices=[('', 'Selecciona tu género')] + [(str(g[0]), g[1]) for g in genero],
                            coerce=str, 
                            validate_choice=False, 
                            validators=[DataRequired()]
                            )    
    fecha_nacimiento = DateField("Fecha de Nacimiento: ", validators=[DataRequired()])
    nivelEdu = User.get_nivelEdu()
    id_nivelEdu = SelectField("Nivel Educativo: ",
                            choices=[('', 'Selecciona tu nivel educativo')] + [(str(g[0]), g[1]) for g in nivelEdu],
                            coerce=str, 
                            validate_choice=False, 
                            validators=[DataRequired()]
                            )
    ocupacion = User.get_ocupacion()
    id_ocupacion = SelectField("Ocupacion: ", 
                                choices=[('', 'Selecciona tu ocupación')] + [(str(g[0]), g[1]) for g in ocupacion],
                                coerce=str, 
                                validate_choice=False, 
                                validators=[DataRequired()]
                                )
    ingresos_mensuales = FloatField("Ingresos Mensuales: ", validators=[DataRequired(), NumberRange(min=0, message="El ingreso mensual no puede ser negativo")])    
    curp = StringField("Curp: ", validators=[DataRequired(), Length(min=18, max=18)])
    tel_cel = TelField("Tel Cel: ",
                       validators=[DataRequired(),
                                   Length(min=10, max=10),
                                   Regexp(r'^\+?\d{1,4}?[ .-]?\(?\d{1,3}?\)?[ .-]?\d{1,4}[ .-]?\d{1,4}$',
                                          message="Formato de teléfono inválido")]
                                          )
    tel_casa = TelField("Tel Casa: ",
                        validators=[Optional(),
                                    Length(min=10, max=10),
                                    Regexp(r'^\+?\d{1,4}?[ .-]?\(?\d{1,3}?\)?[ .-]?\d{1,4}[ .-]?\d{1,4}$',
                                           message="Formato de teléfono inválido")]
                                           )
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=5, max=50), EqualTo('password_confirm', message='Las contraseñas deben coincidir')])
    password_confirm = PasswordField('Confirmar Contraseña', validators=[DataRequired()])
    submit = SubmitField("Continuar")

    ######## Verificar que el valor de id_genero no sea '' #########
    def validate_id_genero(form, field):
        if field.data == '':
            raise ValidationError("Por favor selecciona un género válido.")
        
    ######## Verificar que el valor de id_nivelEdu no sea '' #########
    def validate_id_nivelEdu(form, field):
        if field.data == '':
            raise ValidationError("Por favor selecciona un nivel educativo válido.")
        
    ######## Verificar que el valor de id_ocupación no sea '' #########
    def validate_id_ocupacion(form, field):
        if field.data == '':
            raise ValidationError("Por favor selecciona una ocupación valida.")

    ######## Validar Correo Unico #########
    def validate_email(self, field):
        ######## Consultar si el correo existe en la base de datos #######
        if User.check_email(field.data):
            raise ValidationError('El correo ya existe')

class ProfileForm(FlaskForm):
    nombre = StringField("Nombre: ", validators=[DataRequired(), Length(min=4, max=25)])
    ape_pat = StringField("Apellido Paterno: ", validators=[DataRequired(), Length(min=4, max=25)])      
    ape_mat = StringField("Apellido Materno: ", validators=[DataRequired(), Length(min=4, max=25)])
    genero = User.get_genero()
    id_genero = SelectField("Genero: ", choices=genero, coerce=int, validate_choice=False, validators=[DataRequired()])
    fecha_nacimiento = DateField("Fecha de Nacimiento: ", validators=[DataRequired()])
    nivelEdu = User.get_nivelEdu()
    id_nivelEdu = SelectField("Educación: ", choices=nivelEdu, coerce=int, validate_choice=False, validators=[DataRequired()])
    ocupacion = User.get_ocupacion()
    id_ocupacion = SelectField("Ocupacion: ", choices=ocupacion, coerce=int, validate_choice=False, validators=[DataRequired()])
    ingresos_mensuales = FloatField("Ingresos Mensuales: ", 
                                    validators=[DataRequired(), 
                                                NumberRange(min=0, message="El ingreso mensual no puede ser negativo")]
                                    )    
    curp = StringField("Curp: ", validators=[DataRequired(), Length(min=18, max=18)])
    tel_cel = TelField("Tel Cel: ", 
                       validators=[DataRequired(), 
                                   Length(min=10, max=10), 
                                   Regexp(r'^\+?\d{1,4}?[ .-]?\(?\d{1,3}?\)?[ .-]?\d{1,4}[ .-]?\d{1,4}$', 
                                          message="Formato de teléfono inválido")]
                                          )
    tel_casa = TelField("Tel Casa: ", 
                        validators=[Optional(), 
                                    Length(min=10, max=10), 
                                    Regexp(r'^\+?\d{1,4}?[ .-]?\(?\d{1,3}?\)?[ .-]?\d{1,4}[ .-]?\d{1,4}$', 
                                           message="Formato de teléfono inválido")]
                                           )
    email = EmailField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Guardar Cambios')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Contraseña actual', validators=[DataRequired()])
    new_password = PasswordField('Nueva contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar nueva contraseña', validators=[DataRequired(), EqualTo('new_password', message='Las contraseñas deben coincidir')])
    submit = SubmitField('Cambiar contraseña')