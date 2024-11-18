from flask import Blueprint, render_template, session, redirect, url_for, flash
from datetime import datetime

from models.loans import Loan
from models.users import User

from forms.loan_forms import LoanForm 

loan_views = Blueprint('loan',__name__)

@loan_views.route('/préstamo/solicitar', methods=['GET', 'POST'])
def solicitar():
    if 'user' not in session:
        return redirect(url_for('user.login'))
    
    user = User.__get__(session['user']['id'])

    if not user.is_approved:
        flash('Tu cuenta está pendiente de aprobación. No puedes solicitar un préstamo aún.', 'warning')
        return redirect(url_for('home.index'))
    
    # Verifica si el domicilio está registrado
    if not user.has_address():
        flash('Es necesario registrar tu domicilio antes de solicitar un préstamo.', 'warning')
        return redirect(url_for('user.address'))
    
    form = LoanForm()

    if form.validate_on_submit():
        id_cliente = session.get('user')['id']
        monto = form.monto.data
        periodo = form.periodo.data
        modalidad_pago = form.modalidad_pago.data
        fecha_in = datetime.utcnow()
        
        # Crea y guarda el préstamo
        loan = Loan(id_cliente, monto, periodo, modalidad_pago, fecha_in)
        loan.save()

        # Guarda los datos del préstamo en la sesión para usarlos en la función de redireccionamiento
        session['loan_data'] = {
            'monto': monto,
            'periodo': periodo,
            'modalidad_pago': modalidad_pago,
            'fecha_in': fecha_in
        }

        return redirect(url_for('loan.loan'))
    
    return render_template('loan/solicitar_loan.html', form=form) 

@loan_views.route('/préstamo/previo/', methods=['GET'])
def loan():
    # Obtenemos los datos de la sesión
    loan_data = session.get('loan_data')

    if loan_data:
        # Puedes acceder a los datos individuales
        monto = loan_data['monto']
        periodo = loan_data['periodo']
        modalidad_pago = loan_data['modalidad_pago']
        fecha_in = loan_data['fecha_in']

        if modalidad_pago == 1:
            pagos = int(periodo) * 2
            modalidad = 'Quincenal'
        else:
            pagos = periodo
            modalidad = 'Mensual'

        # Calcular el monto total a pagar 
        tasa_interes = 0.1  # Tasa de interés
        monto_total = monto * tasa_interes + monto

        # Aquí puedes hacer lo que necesites con los datos, por ejemplo, mostrarlos en una plantilla
        return render_template('loan/calcular_loan.html', monto=monto, periodo=periodo, fecha_in=fecha_in, pagos=pagos, modalidad=modalidad, monto_total=monto_total)
    else:
        # Manejo en caso de que los datos no estén en la sesión
        return "No se encontraron datos de préstamo previo."

@loan_views.route('/préstamo/estado/')
def estado():
    # Obtenemos los datos de la sesión
    loan_data = session.get('loan_data')

    if loan_data:
        # Puedes acceder a los datos individuales
        monto = loan_data['monto']
        periodo = loan_data['periodo']
        modalidad_pago = loan_data['modalidad_pago']
        fecha_in = loan_data['fecha_in']

        if modalidad_pago == 1:
            pagos = periodo * 2
            modalidad = 'Quincenal'
        else:
            pagos = periodo
            modalidad = 'Mensual'

        # Calcular el monto total a pagar 
        tasa_interes = 0.1  # Tasa de interés
        monto_total = monto * tasa_interes + monto

    return render_template('loan/estado_loan.html', monto=monto, periodo=periodo, modalidad=modalidad, monto_total=monto_total)

@loan_views.route('/préstamo/pagos/')
def pagos():
    return render_template('loan/pagos_loan.html')