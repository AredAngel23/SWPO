from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

from models.address import Address

class AddressForm(FlaskForm):
    estado = Address.get_estado
    id_estado = SelectField("Estado: ", choices=estado, coerce=int, validate_choice=False, validators=[DataRequired()])
    municipio = StringField("Municipio: ", validators=[DataRequired(), Length(min=5, max=50)])  
    cp = IntegerField("Codigó Postal: ", validators=[DataRequired()])
    tipo_asentamiento = Address.get_tipo_asentamineto
    tipo_asen = SelectField("Tipo de Asentamiento: ", choices=tipo_asentamiento, coerce=int, validate_choice=False,    validators=[DataRequired()])  
    asentamiento = StringField("Asentamiento: ", validators=[DataRequired(), Length(min=5, max=60)])  
    calle = StringField("Calle: ", validators=[DataRequired(), Length(min=4, max=50)])
    num_ext = IntegerField("Número Exterior: ", validators=[Optional(), NumberRange(min=0.0, max=None)])
    num_int = IntegerField("Número Interior: ", validators=[Optional(), NumberRange(min=0.0, max=None)])  
    submit = SubmitField("Registrar")
  
   


