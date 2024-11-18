from flask import Blueprint, render_template, redirect, url_for, flash
from utils.decorators import admin_required

from models.users import User
from models.address import Address

admin_views = Blueprint('admin',__name__)

@admin_views.route('/admin/')
@admin_required
def admin():
    # Obtener usuarios que no están aprobados
    usuarios_pendientes = User.get_users()
    return render_template('admin/main.html', users=usuarios_pendientes)

@admin_views.route('/admin/<int:id_usuario>/aprobar')
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

@admin_views.route('/admin/<int:id_usuario>/rechazar')
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

@admin_views.route('/admin/clientes/<int:id>/eliminar', methods=['POST']) 
@admin_required 
def delete(id):
    user=User.__get__(id)
    if user != None:
        user.delete()
    return redirect(url_for('admin.mostrar_clientes')) 