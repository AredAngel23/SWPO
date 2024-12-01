from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from utils.decorators import client_required
from decimal import Decimal
from datetime import datetime, timedelta

from models.loans import Loan
from models.users import User

from forms.loan_forms import LoanForm 

loan_views = Blueprint('loan',__name__)

@loan_views.route('/préstamo/solicitar/', methods=['GET', 'POST'])
@client_required
def solicitar_prestamo():
    # Verificar que el usuario está autenticado
    if 'user' not in session:
        return redirect(url_for('user.login'))
    
    # Obtener datos del usuario
    user = User.__get__(session['user']['id'])
    if not user:    
        flash('Usuario no encontrado', 'danger')
        return redirect(url_for('user.login'))

    # Verificar que el usuario esté aprobado para solicitar un préstamo
    if not user.is_approved:
        flash('No puedes solicitar un préstamo aún.', 'warning')
        return redirect(url_for('home.index'))
    
    # Verificar que el usuario tenga un domicilio registrado
    if not user.has_address():
        flash('Es necesario registrar tu domicilio antes de solicitar un préstamo.', 'warning')
        return redirect(url_for('user.address'))
    
    # Verificar si el cliente ya tiene un préstamo activo o pendiente
    existing_loan = Loan.get_by_user_id(user.id_usuario)
    if existing_loan:
        if existing_loan.estado == 'Aprobado' or existing_loan.estado == 'Activo': 
            flash('Solo puedes tener un préstamo activo a la vez.', 'info')
            return redirect(url_for('home.pre_loan')) 
        elif existing_loan.estado == 'Pendiente':
            flash('Espera la aprobación de tu solicitud, solo puedes solicitar un préstamo.', 'info')
            return redirect(url_for('home.pre_loan'))
    
    form = LoanForm()

    if form.validate_on_submit():
        id_cliente = session.get('user')['id']
        monto = Decimal(form.monto.data) # Convertir el monto a decimal
        plazo = form.plazo.data
        interes = Decimal('0.15')  # Interés fijo del 15% con Decimal 
        monto_total = monto * (1 + interes)  # Calcular el monto total con interés
        
        # Crear y guardar el préstamo
        loan = Loan(
            id_cliente=id_cliente,
            monto=monto,
            interes=interes,
            monto_total=monto_total,
            plazo=plazo,
            estado='Pendiente'
        )
        loan.save()

        flash('Solicitud de préstamo enviada correctamente.', 'success')
        return redirect(url_for('home.pre_loan'))
    
    return render_template('loan/solicitar_loan.html', form=form) 

@loan_views.route('/préstamo/finalizar_solicitud/', methods=['GET', 'POST'])
@client_required
def finalizar_solicitud():
    # Obtener datos del usuario
    user = User.__get__(session['user']['id'])
    if not user:
        flash('Usuario no encontrado.', 'danger')
        return redirect(url_for('user.login'))

    # Verificar si el cliente tiene un préstamo aprobado
    loan = Loan.get_by_user_id(user.id_usuario)
    if not loan or loan.estado != 'Aprobado':
        flash('No tienes una solicitud de préstamo para finalizar.', 'info')
        return redirect(url_for('home.pre_loan'))

    if request.method == 'POST':
        # Registrar fechas y actualizar el préstamo
        loan.estado = 'Activo'
        fecha_inicio = datetime.now()
        fecha_vencimiento = fecha_inicio + timedelta(days=loan.plazo * 30)
        loan.fecha_inicio = fecha_inicio
        loan.fecha_vencimiento = fecha_vencimiento
        loan.save()

        flash('Préstamo finalizado correctamente.', 'success')
        return redirect(url_for('loan.loan'))
    
    return render_template('loan/finalizar_solicitud.html', loan=loan)

@loan_views.route('/préstamo/mi_préstamo/')
@client_required
def loan():
    # Obtener datos del usuario
    user = User.__get__(session['user']['id'])
    if not user:
        flash('Usuario no encontrado.', 'danger')
        return redirect(url_for('user.login'))

    # Verificar si el cliente tiene un préstamo activo
    loan = Loan.get_by_user_id(user.id_usuario)
    if not loan or loan.estado != 'Activo':
        flash('No tienes un préstamo activo para gestionar.', 'info')
        return redirect(url_for('home.pre_loan'))
    
    # Calcular las fechas de pago
    fechas_pago = loan.calcular_fechas_pago()

    return render_template('loan/loan.html', loan=loan, fechas_pago=fechas_pago)

@loan_views.route('/préstamo/mi_préstamo/pagar/')
@client_required
def pagos():
    return redirect(url_for('loan.loan'))