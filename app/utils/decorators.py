from functools import wraps
from flask import session, redirect, url_for, flash

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Verifica si el usuario está en sesión
        if 'user' not in session:
            flash('Por favor, inicia sesión primero.', 'warning')
            return redirect(url_for('user.login'))

        # Verifica si el usuario tiene rol de administrador
        if session['user'].get('rol') != 'admin':
            flash('No tienes permiso para acceder a esta página.', 'danger')
            return redirect(url_for('home.index'))

        return f(*args, **kwargs)
    return decorated_function

def client_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Verifica si el usuario está en sesión
        if 'user' not in session:
            flash('Por favor, inicia sesión primero.', 'warning')
            return redirect(url_for('user.login'))

        # Verifica si el usuario tiene rol de cliente
        if session['user'].get('rol') != 'cliente':
            flash('No tienes permiso para acceder a esta página.', 'danger')
            return redirect(url_for('home.index'))

        return f(*args, **kwargs)
    return decorated_function
