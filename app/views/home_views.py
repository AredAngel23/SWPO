from flask import Blueprint, render_template,session, redirect, url_for, flash

from models.users import User
from models.loans import Loan

home_views = Blueprint('home',__name__)

@home_views.route('/')
def index():
    user = session.get('user')
    if 'user' in session:
        user = User.__get__(session['user']['id'])
        if not user:    
            flash('Usuario no encontrado', 'danger')
            return redirect(url_for('user.login'))
        # Verificar si el cliente ya tiene un préstamo activo o pendiente
        existing_loan = Loan.get_by_user_id(user.id_usuario)
        if existing_loan:
            # Obtener el estado actual del préstamo
            estado_actual = existing_loan.estado
            
            # Obtener el estado almacenado previamente en la sesión
            estado_previo = session.get('loan_status')
            
            # Si el estado ha cambiado o no se ha almacenado previamente
            if estado_actual != estado_previo:
                # Actualizar el estado en la sesión
                session['loan_status'] = estado_actual
                
                # Mostrar el mensaje flash correspondiente
                if estado_actual == 'Aprobado': 
                    flash('Tu solicitud de préstamo ha sido aprobada, ve al apartado "Préstamos" para finalizar con el préstamo.', 'info')
                elif estado_actual == 'Pendiente':
                    flash('Espera la aprobación de tu solicitud de préstamo.', 'info')
                elif estado_actual == 'Activo':
                    flash('Felicidades tienes un préstamo activo, dirigete a Préstamos>>Mi Préstamo para gestionarlo.', 'info')
                elif estado_actual == 'Rechazado':
                    flash('Tu solicitud de préstamo fue rechazada, pero puedes solicitar nuevamente.', 'info')

    return render_template('home/index.html')

@home_views.route('/info_préstamo/')
def pre_loan():
    is_approved = None
    if 'user' in session:
        user = User.__get__(session['user']['id'])
        if not user:    
            flash('Usuario no encontrado', 'danger')
            return redirect(url_for('user.login'))
        
        existing_loan = Loan.get_by_user_id(user.id_usuario)    
    
        if user.is_approved == 0:
            flash('Tu datos están pendientes de aprobación por un administrador, Este proceso podría demorar hasta 2 días como máximo, mantente al pendiente de la página para tu aprobación.', 'warning')
        elif user.is_approved == 1:
            if session['user'].get('rol') != 'admin':
                # Verificar si el mensaje ya fue mostrado
                if not session.get('approval_message_shown'):
                    flash('Tus datos de registro han sido verificados y aprobados con éxito.', 'success')
                    session['approval_message_shown'] = True  # Marca que ya se mostró el mensaje
                is_approved = 1
        else:
            flash('Tus datos han sido revisados y lamentablemente tu cuenta ha sido rechazada por el administrador. Si tienes alguna duda o crees que esto ha sido un error, por favor contactanos.', 'danger')

    return render_template('home/info_loan.html', is_approved=is_approved, existing_loan=existing_loan)    

@home_views.route('/about/')
def about():
    return render_template('home/about.html') 

@home_views.route('/comentarios/')
def comentarios():
    return render_template('home/comentarios.html')
