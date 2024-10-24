from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TelField, PasswordField, EmailField, SelectField, ValidationError, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange, Optional

from models.users import User

class RegisterForm(FlaskForm):
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
    ingresos_mensuales = FloatField("Ingresos Mensuales: ", validators={NumberRange(min=0.0, max=None)})
    curp = StringField("Curp: ", validators=[DataRequired(), Length(min=18, max=18)])
    tel_cel = TelField("Tel Cel: ", validators=[DataRequired(), Length(min=10, max=10)])
    tel_casa = TelField("Tel Casa: ", validators=[Optional(), Length(min=10, max=10)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                    Length(min=5, max=50), 
                                                    EqualTo('password_confirm', 
                                                            message='Las contraseñas deben coincidir')])
    password_confirm = PasswordField('Password Confirm', validators=[DataRequired()])
    submit = SubmitField("Continuar")

    ######## Validar Correo Unico #########
    def validate_email(self, field):
        ######## Consultar si el correo existe en la base de datos #######
        if User.check_email(field.data):
            raise ValidationError('El correo ya existe')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Ingresar')

################ Formulario de Perfil ################
class ProfileForm(FlaskForm):
    # password No se edita
    # email, Verificar antes de actualizar
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
    ingresos_mensuales = FloatField("Ingresos Mensuales: ", validators={NumberRange(min=0.0, max=None)})
    curp = StringField("Curp: ", validators=[DataRequired(), Length(min=18, max=18)])
    tel_cel = TelField("Tel Cel: ", validators=[DataRequired(), Length(min=10, max=10)])
    tel_casa = TelField("Tel Casa: ", validators=[Optional(), Length(min=10, max=10)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Guardar Cambios')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Contraseña actual', validators=[DataRequired()])
    new_password = PasswordField('Nueva contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar nueva contraseña', validators=[DataRequired(), EqualTo('new_password', message='Las contraseñas deben coincidir')])
    submit = SubmitField('Cambiar contraseña')