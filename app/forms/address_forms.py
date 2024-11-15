from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, IntegerField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, NumberRange, Optional

from models.address import Address

class AddressForm(FlaskForm):
    estado = Address.get_estado()
    id_estado = SelectField("Estado: ",
                            choices=[('', 'Selecciona tu estado')] + [(str(g[0]), g[1]) for g in estado],
                            coerce=str, 
                            validate_choice=False, 
                            validators=[DataRequired()]
                        )
    municipio = StringField("Municipio: ", validators=[DataRequired(), Length(min=5, max=50)])  
    cp = IntegerField("Código Postal: ",
                      validators=[DataRequired(),
                                  NumberRange(min=10000, max=99999, message="El código postal debe tener 5 dígitos.")]
                    )
    tipo_asentamiento = Address.get_tipo_asentamiento()
    tipo_asen = SelectField("Tipo de Asentamineto: ",
                            choices=[('', 'Selecciona tu tipo de asentamiento')] + [(str(g[0]), g[1]) for g in tipo_asentamiento],
                            coerce=str, 
                            validate_choice=False, 
                            validators=[DataRequired()]
                        )    
    asentamiento = StringField("Asentamiento: ", validators=[DataRequired(), Length(min=5, max=60)])  
    calle = StringField("Calle: ", validators=[DataRequired(), Length(min=3, max=50)])
    num_ext = IntegerField("Número Exterior: ", validators=[Optional(), NumberRange(min=1)])
    num_int = IntegerField("Número Interior: ", validators=[Optional(), NumberRange(min=1)])
    submit = SubmitField("Registrar")

    ######## Verificar que el valor de estado no sea '' #########
    def validate_id_estado(form, field):
        if field.data == '':
            raise ValidationError("Por favor selecciona un estado.")
        
    ######## Verificar que el valor de tipo de asentamineto no sea '' #########
    def validate_tipo_asen(form, field):
        if field.data == '':
            raise ValidationError("Por favor selecciona un tipo de asentamiento.")
        
        
class ProfileAddressForm(FlaskForm):
    estado = Address.get_estado()
    id_estado = SelectField("Estado: ", choices=estado, coerce=int, validate_choice=False, validators=[DataRequired()])
    municipio = StringField("Municipio: ", validators=[DataRequired(), Length(min=5, max=50)])  
    cp = IntegerField("Código Postal: ",
                      validators=[DataRequired(),
                                  NumberRange(min=10000, max=99999, message="El código postal debe tener 5 dígitos.")]
                    )
    tipo_asentamiento = Address.get_tipo_asentamiento()    
    tipo_asen = SelectField("Tipo de Asentamiento: ", choices=tipo_asentamiento, coerce=int, validate_choice=False, validators=[DataRequired()])    
    asentamiento = StringField("Asentamiento: ", validators=[DataRequired(), Length(min=5, max=60)])  
    calle = StringField("Calle: ", validators=[DataRequired(), Length(min=3, max=50)])
    num_int = IntegerField("Número Interior: ", validators=[Optional(), NumberRange(min=1)])
    num_ext = IntegerField("Número Exterior: ", validators=[Optional(), NumberRange(min=1)])
    submit = SubmitField('Guardar Cambios')  
   


