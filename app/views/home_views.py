from flask import Blueprint, render_template, session, redirect, url_for
from datetime import datetime

from models.loans import Loan

from forms.loan_forms import LoanForm 

home_views = Blueprint('home',__name__)

@home_views.route('/')
def index():
    user = session.get('user')
    return render_template('home/index.html')

@home_views.route('/préstamo/', methods = ['GET', 'POST'])
def loan():
    if 'user' not in session:
        # Si el usuario no ha iniciado sesión, redirecciona a la página de inicio de sesión
        return redirect(url_for('user.login'))
    
    if 'address_registered' not in session:
        # Si el usuario no ha registrado su domicilio, redirecciona a la página de registro de domicilio
        return redirect(url_for('user.address')) 

    form = LoanForm()

    if form.validate_on_submit():
        id_cliente = session.get('user')['id']
        monto = form.monto.data
        periodo = form.periodo.data
        modalidad_pago = form.modalidad_pago.data
        fecha_in = datetime.utcnow()
        
        user = Loan(id_cliente, monto, periodo, modalidad_pago, fecha_in)
        user.save()

        # Guardamos los datos en la sesión para usarlos en la función de redireccionamiento
        session['loan_data'] = {
            'monto': monto,
            'periodo': periodo,
            'modalidad_pago': modalidad_pago,
            'fecha_in': fecha_in
        }

        return redirect(url_for('loan.pre_loan'))
    
    return render_template('home/loan.html', form = form)    

@home_views.route('/about/')
def about():
    return render_template('home/about.html') 

@home_views.route('/comentarios/')
def comentarios():
    return render_template('home/comentarios.html')
