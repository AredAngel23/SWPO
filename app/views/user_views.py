from flask import Blueprint, render_template, flash, redirect, url_for, session, abort

from models.users import User
from models.address import Address

from forms.user_forms import RegisterForm, LoginForm, ProfileForm
from forms.address_forms import AddressForm

user_views = Blueprint('user',__name__)

@user_views.route('/usuarios/registro/', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        nombre = form.nombre.data
        ape_pat = form.ape_pat.data
        ape_mat = form.ape_mat.data
        id_genero = form.id_genero.data
        fecha_nacimiento = form.fecha_nacimiento.data
        id_nivelEdu = form.id_nivelEdu.data
        id_ocupacion = form.id_ocupacion.data
        ingresos_mensuales = form.ingresos_mensuales.data
        curp = form.curp.data
        tel_cel = form.tel_cel.data
        tel_casa = form.tel_casa.data
        email = form.email.data
        password = form.password.data

        user = User(nombre, ape_pat, ape_mat, id_genero, fecha_nacimiento, id_nivelEdu, id_ocupacion, ingresos_mensuales, curp, tel_cel, tel_casa, email, password)
        user.save()
        flash ('Registro Exitoso')

        return redirect(url_for('user.login'))
    
    return render_template('auth/register.html', form = form)


@user_views.route('/usuarios/iniciar_sesión/', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
        
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.get_by_password(email, password)
        if not user:
            flash('Verifica tus Datos')
        else:
            session['user'] = {'email': email, 'id': user.id_usuario, 'rol':user.rol}
            if user.rol == 'cliente':
                return render_template('home/index.html', user=user, form=form)
            else:
                return redirect(url_for('user.admin'))
        
    return render_template('auth/login.html', form=form)

@user_views.route('/usuarios/domicilio/', methods = ['GET', 'POST'])
def address():
    if 'user' not in session:     
        # El usuario no ha iniciado sesión, redirecciona a la página de inicio de sesión
        return redirect(url_for('user.login')) 
    
    if 'address_registered' in session:
        # El usuario ya ha registrado su domicilio, redirecciona a la página de préstamo
        return ('Domicilio Ya Registrado')
    
    form = AddressForm()

    if form.validate_on_submit():
        id_estado = form.id_estado.data
        municipio = form.municipio.data
        cp = form.cp.data
        tipo_asen = form.tipo_asen.data
        asentamiento = form.asentamiento.data
        calle = form.calle.data
        num_ext = form.num_ext.data
        num_int = form.num_int.data
        id_cliente = session.get('user')['id']

        user = Address(id_estado, municipio, cp, tipo_asen, asentamiento, calle, num_ext, num_int, id_cliente)
        user.save()

        session['address_registered'] = True  # Marcar el domicilio como registrado
        return redirect(url_for('home.loan'))  # Redirigir de nuevo a la vista de préstamo
        #flash ('Domicilio Registrado')

    return render_template('auth/address.html', form=form)

@user_views.route('/cerrar_sesión/')  
def logout():
    session.clear()
    return redirect(url_for('home.index'))  

@user_views.route('/users/profile/', methods=('GET', 'POST'))
def profile():
    form = ProfileForm()
    user = User.__get__(id_usuario=session.get('user')['id'])
    if not user:    
        abort(404)
    if form.validate_on_submit():
        user.nombre = form.nombre.data
        user.ape_pat = form.ape_pat.data
        user.ape_mat = form.ape_mat.data
        user.id_genero = form.id_genero.data
        user.fecha_nacimiento = form.fecha_nacimiento.data
        user.id_nivelEdu = form.id_nivelEdu.data
        user.id_ocupacion = form.id_ocupacion.data
        user.ingresos_mensuales = form.ingresos_mensuales.data
        user.curp = form.curp.data
        user.tel_cel = form.tel_cel.data
        user.tel_casa = form.tel_casa.data
        user.save()
    form.nombre.data = user.nombre
    form.ape_pat.data = user.ape_pat
    form.ape_mat.data = user.ape_mat
    form.id_genero.data = user.id_genero
    form.fecha_nacimiento.data = user.fecha_nacimiento
    form.id_nivelEdu.data = user.id_nivelEdu
    form.id_ocupacion.data = user.id_ocupacion
    form.ingresos_mensuales.data = user.ingresos_mensuales
    form.curp.data = user.curp
    form.tel_cel.data = user.tel_cel
    form.tel_casa.data = user.tel_casa      
    return render_template('auth/profile.html', form=form)

@user_views.route('/users/')
def mostrar_usuarios():
    users = User.get_all()
    return render_template('admin/clientes.html', users = users)

@user_views.route('/usuarios/<int:id>/eliminar', methods=['POST'])  
def delete(id):
    user=User.__get__(id)
    if user != None:
        user.delete()
    return redirect(url_for('user.mostrar_usuarios'))

@user_views.route('/admin/')
def admin():
    return render_template('admin/main.html')
