from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField, RadioField, SelectField, BooleanField
from wtforms.validators import DataRequired, NumberRange, InputRequired

from models.loans import Loan

class LoanForm(FlaskForm):      
    monto = FloatField("Monto:", 
                       validators=[InputRequired(),
                                   NumberRange(min=500,
                                               max=20000,
                                               message='El monto debe estar entre $500 y $20,000')]
                       )  
    periodo = RadioField("Periodo del Préstamo: ", 
                        choices=['2','4','6','8','10','12'],
                        validators=[DataRequired()]
                        )
    modalidad_pago = Loan.get_modalidad
    modalidad_pago = SelectField("Modalidad de Pago: ",
                                 choices=modalidad_pago,
                                 coerce=int,
                                 validate_choice=False, 
                                 validators=[DataRequired()]
                                 )
    accept_tc = BooleanField('Acepto términos y condiiones',
                              validators=[DataRequired()]
                              )
    submit = SubmitField("Continuar")
  
   


