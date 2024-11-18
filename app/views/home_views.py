from flask import Blueprint, render_template, request, session, redirect, url_for, flash

from models.users import User

home_views = Blueprint('home',__name__)

@home_views.route('/')
def index():
    user = session.get('user')
    return render_template('home/index.html')

@home_views.route('/info_préstamo/')
def pre_loan():
    if 'user' not in session:
        return redirect(url_for('user.login', next=request.url))
    
    user = User.__get__(session['user']['id'])
    if not user:    
        flash('Usuario no encontrado', 'danger')
        return redirect(url_for('user.login'))
    
    if user.is_approved == 0:
        flash('Tu cuenta está pendiente de aprobación por un administrador.', 'warning')
        is_approved = 0
    elif user.is_approved == 1:
        flash('Tus datos han sido verificados y aprobados con exito.', 'success')
        is_approved = 1
        #return redirect(url_for('loan.solicitar'))
    else:
        is_approved = 2
        flash('Tu cuenta ha sido rechazada por un administrador.', 'danger')

    return render_template('home/info_loan.html', is_approved=is_approved)    

@home_views.route('/about/')
def about():
    return render_template('home/about.html') 

@home_views.route('/comentarios/')
def comentarios():
    return render_template('home/comentarios.html')
