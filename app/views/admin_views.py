from flask import Blueprint, render_template, redirect, url_for
from models.users import User 

admin_views = Blueprint('admin',__name__)

@admin_views.route('/admin/')
def admin():
    return render_template('admin/main.html')

@admin_views.route('/admin/clientes/')
def mostrar_usuarios():
    users = User.get_all()
    return render_template('admin/clientes.html', users = users)

@admin_views.route('/admin/clientes/<int:id>/eliminar', methods=['POST'])  
def delete(id):
    user=User.__get__(id)
    if user != None:
        user.delete()
    return redirect(url_for('admin.mostrar_usuarios'))