from flask import Blueprint, render_template,session, redirect, url_for, flash

from models.users import User

home_views = Blueprint('home',__name__)

@home_views.route('/')
def index():
    user = session.get('user')
    return render_template('home/index.html')

@home_views.route('/info_préstamo/')
def pre_loan():
    is_approved = None
    if 'user' in session:
        user = User.__get__(session['user']['id'])
        if not user:    
            flash('Usuario no encontrado', 'danger')
            return redirect(url_for('user.login'))
        
        if user.is_approved == 0:
            flash('Tu datos están pendientes de aprobación por un administrador, Este proceso podría demorar hasta 2 días como máximo, mantente al pendiente de la página para tu aprobación.', 'warning')
        elif user.is_approved == 1:
            if session['user'].get('rol') != 'admin':
                flash('Tus datos han sido verificados y aprobados con exito.', 'success')
                is_approved = 1
        else:
            flash('Tus datos han sido revisados y lamentablemente tu cuenta ha sido rechazada por el administrador. Si tienes alguna duda o crees que esto ha sido un error, por favor contactanos.', 'danger')

    return render_template('home/info_loan.html', is_approved=is_approved)    

@home_views.route('/about/')
def about():
    return render_template('home/about.html') 

@home_views.route('/comentarios/')
def comentarios():
    return render_template('home/comentarios.html')
