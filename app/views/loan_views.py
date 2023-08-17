from flask import Blueprint, render_template, session

loan_views = Blueprint('loan',__name__)

@loan_views.route('/préstamo/previo/', methods=['GET'])
def pre_loan():
    # Obtenemos los datos de la sesión
    loan_data = session.get('loan_data')

    if loan_data:
        # Puedes acceder a los datos individuales
        monto = loan_data['monto']
        periodo = loan_data['periodo']
        modalidad_pago = loan_data['modalidad_pago']
        fecha_in = loan_data['fecha_in']

        if modalidad_pago == 1:
            pagos = periodo * 2
            modalidad = 'Quincenal'
        else:
            pagos = periodo
            modalidad = 'Mensual'

        # Calcular el monto total a pagar 
        tasa_interes = 0.1  # Tasa de interés
        monto_total = monto * tasa_interes + monto

        # Aquí puedes hacer lo que necesites con los datos, por ejemplo, mostrarlos en una plantilla
        return render_template('loan/pre_loan.html', monto=monto, periodo=periodo, fecha_in=fecha_in, pagos=pagos, modalidad=modalidad, monto_total=monto_total)
    else:
        # Manejo en caso de que los datos no estén en la sesión
        return "No se encontraron datos de préstamo previo."

@loan_views.route('/préstamo/estado/')
def estado():
    # Obtenemos los datos de la sesión
    loan_data = session.get('loan_data')

    if loan_data:
        # Puedes acceder a los datos individuales
        monto = loan_data['monto']
        periodo = loan_data['periodo']
        modalidad_pago = loan_data['modalidad_pago']
        fecha_in = loan_data['fecha_in']

        if modalidad_pago == 1:
            pagos = periodo * 2
            modalidad = 'Quincenal'
        else:
            pagos = periodo
            modalidad = 'Mensual'

        # Calcular el monto total a pagar 
        tasa_interes = 0.1  # Tasa de interés
        monto_total = monto * tasa_interes + monto

    return render_template('loan/estado_loan.html', monto=monto, periodo=periodo, modalidad=modalidad, monto_total=monto_total)

@loan_views.route('/préstamo/pagos/')
def pagos():
    return render_template('loan/pagos_loan.html')