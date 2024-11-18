from flask import Blueprint, render_template, flash, redirect, request, url_for, session

from models.users import User
from models.address import Address

from forms.user_forms import RegisterForm, LoginForm, ProfileForm, ChangePasswordForm
from forms.address_forms import AddressForm, ProfileAddressForm

user_views = Blueprint('user',__name__)

@user_views.route('/usuarios/iniciar_sesión/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    next_url = request.args.get('next')  # Obtén la URL "next" si existe
        
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.get_by_password(email, password)
        
        if not user:
            flash('Verifica tus datos', 'danger')
        else:
            session['user'] = {'email': email, 'id': user.id_usuario, 'rol': user.rol}

            if user.rol == 'cliente':
                return redirect(next_url or url_for('home.index'))
            elif user.rol == 'admin':
                return redirect(next_url or url_for('admin.admin'))
            else:
                flash('Rol de usuario no reconocido.', 'danger')
                return redirect(url_for('user.login'))
    
    return render_template('auth/login.html', form=form)

@user_views.route('/usuarios/registro/', methods = ['GET', 'POST'])
def register():
    if 'user' in session:
        flash('Tus datos ya están registrados. Edita tus datos aquí si necesitas actualizarlos.', 'info')
        return redirect(url_for('user.profile'))
    
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
        flash ('Registro Exitoso', 'success')

        return redirect(url_for('user.login'))
    
    if form.errors:
        # Si hay errores en el formulario
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Verifica tus datos, {error}", 'danger')
    
    return render_template('auth/register.html', form = form)

@user_views.route('/usuarios/perfil/', methods=('GET', 'POST'))
def profile():
    if 'user' not in session:
        return redirect(url_for('user.login', next=request.url))
    
    user = User.__get__(session.get('user')['id'])
    if not user:    
        flash('Usuario no encontrado', 'danger')
        return redirect(url_for('user.login'))

    # Verifica si el domicilio está registrado
    has_address = user.has_address()

    form = ProfileForm()
    password_form = ChangePasswordForm()  

    # Actualización del perfil
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
        user.email = form.email.data
        user.save()

        flash('Perfil actualizado correctamente', 'success')

    # Cambio de contraseña
    if password_form.validate_on_submit():
        old_password = password_form.old_password.data
        new_password = password_form.new_password.data
        password_change_message = user.change_password(old_password, new_password)
        
        if "exitosamente" in password_change_message:
            flash(password_change_message, 'success')
            return redirect(url_for('user.profile'))
        else:
            flash(password_change_message, 'danger')

    # Pre-llenar el formulario con los datos del usuario actual        
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
    form.email.data = user.email   

    return render_template('auth/profile.html', form=form, password_form=password_form, has_address=has_address)

@user_views.route('/usuarios/domicilio/', methods=['GET', 'POST'])
def address():
    if 'user' not in session:
        return redirect(url_for('user.login', next=request.url))

    user = User.__get__(session['user']['id'])
    if not user:    
        flash('Usuario no encontrado', 'danger')
        return redirect(url_for('user.login'))

    # Verificar si el domicilio ya ha sido registrado
    if user.has_address():
        flash('Ya has registrado tu domicilio. Edita tus datos aquí si necesitas actualizarlos.', 'info')
        return redirect(url_for('user.address_profile'))
    
    form = AddressForm()

    if form.validate_on_submit():
        # Crear y guardar el registro de domicilio
        address = Address(
            id_estado=form.id_estado.data,
            municipio=form.municipio.data,
            cp=form.cp.data,
            tipo_asen=form.tipo_asen.data,
            asentamiento=form.asentamiento.data,
            calle=form.calle.data,
            num_ext=form.num_ext.data,
            num_int=form.num_int.data,
            id_cliente=user.id_usuario
        )
        address.save()
        flash('Registro de domicilio exitoso', 'success')

        return redirect(url_for('loan.solicitar'))

    # Si hay errores en el formulario, mostrar mensajes sin redirigir
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Verifica tus datos, {error}", 'danger')

    return render_template('auth/address.html', form=form)

@user_views.route('/usuarios/perfil/domicilio', methods=['GET', 'POST'])
def address_profile():
    if 'user' not in session:
        return redirect(url_for('user.login', next=request.url))
    
    user = User.__get__(session.get('user')['id'])
    if not user:
        flash('Usuario no encontrado', 'danger')
        return redirect(url_for('user.login'))

    # Validar que el usuario tenga un domicilio
    if not user.has_address():
        flash('No tienes un domicilio registrado. Por favor, regístralo primero.', 'warning')
        return redirect(url_for('user.address'))

    form = ProfileAddressForm()
    address = user.get_address()

    # Actualización del domicilio
    if form.validate_on_submit():
        address.id_estado = form.id_estado.data
        address.municipio = form.municipio.data
        address.cp = form.cp.data
        address.tipo_asen = form.tipo_asen.data
        address.asentamiento = form.asentamiento.data
        address.calle = form.calle.data
        address.num_ext = form.num_ext.data
        address.num_int = form.num_int.data
        address.save()

        flash('Domicilio actualizado correctamente.', 'success')

    if form.errors:
        # Si hay errores en el formulario
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Verifica tus datos, {error}", 'danger')

    # Prellenar el formulario con los datos del domicilio
    form.id_estado.data = address.id_estado
    form.municipio.data = address.municipio
    form.cp.data = address.cp
    form.tipo_asen.data = address.tipo_asen
    form.asentamiento.data = address.asentamiento
    form.calle.data = address.calle
    form.num_ext.data = address.num_ext
    form.num_int.data = address.num_int

    return render_template('auth/address_profile.html', form=form)

@user_views.route('/cerrar_sesión/')  
def logout():
    session.clear()
    flash('Sesión cerrada exitosamente.', 'success')
    return redirect(url_for('home.index'))