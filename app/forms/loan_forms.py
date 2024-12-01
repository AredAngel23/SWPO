from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class LoanForm(FlaskForm):
    monto = DecimalField('Monto requerido', validators=[
            DataRequired(message='El monto es obligatorio'),
            NumberRange(min=500, max=50000, message='El monto debe estar entre $500 y $50,000')
    ])
    plazo = IntegerField('Plazo (en meses)', validators=[
        DataRequired(message='El plazo es obligatorio'),
        NumberRange(min=2, max=24, message='El plazo debe estar entre 2 y 24 meses')
    ])
    submit = SubmitField('Enviar Solicitud')