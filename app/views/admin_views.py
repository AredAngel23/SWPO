from flask import Blueprint, render_template, redirect, url_for, flash
from utils.decorators import admin_required

from models.users import User
from models.address import Address
from models.loans import Loan

admin_views = Blueprint('admin',__name__)

@admin_views.route('/admin/')
@admin_required
def admin():
    usuarios_pendientes = User.get_users() # Obtener usuarios que no están aprobados
    prestamos_pendientes = Loan.get_prestamos_pendientes() # Obtener préstamos pendientes de aprobación
    return render_template('admin/main.html', users=usuarios_pendientes, loansP=prestamos_pendientes)

@admin_views.route('/admin/usuarios/aprobar/<int:id_usuario>/')
@admin_required
def aprobar_usuario(id_usuario):
    user = User.__get__(id_usuario)  # Método que obtiene un usuario por su ID
    if user:
        if not user.is_approved: # Si el usuario aún no está aprobado
            user.is_approved = 1
            user.save()
            flash(f'Usuario {user.nombre} aprobado exitosamente.', 'success')
        else:
            flash(f'El usuario {user.nombre} ya está aprobado.', 'info')
    else:
        flash('Usuario no encontrado.', 'warning')
    
    return redirect(url_for('admin.admin'))

@admin_views.route('/admin/usuarios/rechazar/<int:id_usuario>/')
@admin_required
def rechazar_usuario(id_usuario):
    user = User.__get__(id_usuario)  # Método que obtiene un usuario por su ID
    if user:
        if not user.is_approved: # Si el usuario aún no está aprobado
            user.is_approved = 2
            user.save()
            flash(f'Usuario {user.nombre} rechazado exitosamente.', 'success')
        else:
            flash(f'El usuario {user.nombre} ya está rechazado.', 'info')
    else:
        flash('Usuario no encontrado.', 'warning')
    
    return redirect(url_for('admin.admin'))

@admin_views.route('/admin/clientes/')
@admin_required
def mostrar_clientes():
    users = User.get_clients()
    return render_template('admin/clientes.html', users = users)

@admin_views.route('/admin/clientes/dirección/<int:id_usuario>/')
@admin_required
def mostrar_domicilio_clientes(id_usuario):
    user = User.__get__(id_usuario) 
    if user:
        if not user.has_address():
            flash(f'El usuario {user.nombre} aún no registra su domicilio.', 'info')
        else:
            address = Address.get_address(user.id_usuario)
            name = user.nombre, user.ape_pat, user.ape_mat
            name = ' '.join(name)
            return render_template('admin/domicilio_clientes.html', address = address, name = name)
    else:
        flash('Usuario no encontrado.', 'error')

    return redirect(url_for('admin.mostrar_clientes'))

@admin_views.route('/admin/clientes/eliminar/<int:id>/', methods=['POST']) 
@admin_required 
def delete(id):
    user=User.__get__(id)
    if user != None:
        user.delete()
    return redirect(url_for('admin.mostrar_clientes')) 

@admin_views.route('/admin/prestamo/aprobar/<int:id_prestamo>/', methods=['POST'])
@admin_required 
def aprobar_prestamo(id_prestamo):
    # Obtener el préstamo por ID
    loan = Loan.get_by_id(id_prestamo)
    if not loan:
        flash('Préstamo no encontrado.', 'danger')
        return redirect(url_for('admin.admin'))

    # Verificar el estado del préstamo
    if loan.estado == 'Aprobado':
        flash('El préstamo ya está aprobado.', 'info')
        return redirect(url_for('admin.admin'))
    elif loan.estado == 'Rechazado':
        flash('El préstamo fue rechazado previamente y no puede ser aprobado.', 'warning')
        return redirect(url_for('admin.admin'))
    elif loan.estado != 'Pendiente':
        flash('El préstamo no está en estado pendiente y no puede ser aprobado.', 'info')
        return redirect(url_for('admin.admin'))

    loan.estado = 'Aprobado'
    loan.save()  

    flash('Préstamo aprobado correctamente. El cliente deberá finalizar la solicitud.', 'success')
    return redirect(url_for('admin.admin'))

@admin_views.route('/admin/prestamo/rechazar/<int:id_prestamo>/', methods=['POST'])
@admin_required 
def rechazar_prestamo(id_prestamo):
    # Obtener el préstamo por ID
    loan = Loan.get_by_id(id_prestamo)
    if not loan:
        flash('Préstamo no encontrado.', 'danger')
        return redirect(url_for('admin.admin'))

    if loan.estado == 'Rechazado':
        flash('El préstamo ya esta rechazado.', 'info')
        return redirect(url_for('admin.admin'))

    loan.estado = 'Rechazado'
    loan.save()

    flash('Préstamo rechazado correctamente.', 'success')
    return redirect(url_for('admin.admin'))

@admin_views.route('/admin/préstamos/')
@admin_required
def mostrar_prestamos():
    prestamos = Loan.get_prestamos()
    return render_template('admin/prestamos.html', loans=prestamos)