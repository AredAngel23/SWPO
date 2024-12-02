from selenium.webdriver.common.by import By
from urllib.parse import unquote
import time

def test_registrar_usuario(driver):
    ##### Ingresar al registro de usuarios #####
    btn_register = driver.find_element(By.ID, 'btn-register')
    btn_register.click()
    time.sleep(2)

    ##### Llenar el formulario de registro #####
    input_nombre = driver.find_element(By.ID, 'nombre')
    input_nombre.send_keys('Joaquin')
    time.sleep(2)
    input_ape_pat = driver.find_element(By.ID, 'ape_pat')
    input_ape_pat.send_keys('Perez')
    time.sleep(2)
    input_ape_mat = driver.find_element(By.ID, 'ape_mat')
    input_ape_mat.send_keys('Rodriguez')
    time.sleep(2)
    input_genero = driver.find_element(By.ID, 'id_genero')
    input_genero.send_keys('Masculino')
    time.sleep(2)
    input_fecha_nacimiento = driver.find_element(By.ID, 'fecha_nacimiento')
    input_fecha_nacimiento.send_keys('2000-01-01')
    time.sleep(2)
    input_nivelEducativo = driver.find_element(By.ID, 'id_nivelEdu')
    input_nivelEducativo.send_keys('Sin estudios')
    time.sleep(2)
    input_ocupacion = driver.find_element(By.ID, 'id_ocupacion')
    input_ocupacion.send_keys('Desempleado')
    time.sleep(2)
    input_ingresos_mensuales = driver.find_element(By.ID, 'ingresos_mensuales')
    input_ingresos_mensuales.send_keys('7500')
    time.sleep(2)
    input_curp = driver.find_element(By.ID, 'curp')
    input_curp.send_keys('PERA030718HTLRDNJ4')
    time.sleep(2)
    input_tel_cel = driver.find_element(By.ID, 'tel_cel')
    input_tel_cel.send_keys('2411553132')
    time.sleep(2)
    input_tel_casa = driver.find_element(By.ID, 'tel_casa')
    input_tel_casa.send_keys('')
    time.sleep(2)
    input_email = driver.find_element(By.ID, 'email')
    input_email.send_keys('prueba11@gmail.com')
    time.sleep(2)
    input_password = driver.find_element(By.ID, 'password')
    input_password.send_keys('12345')
    time.sleep(2)
    input_password_confirm = driver.find_element(By.ID, 'password_confirm')
    input_password_confirm.send_keys('12345')
    time.sleep(2)
    btn_registrar = driver.find_element(By.CLASS_NAME, 'submit-button')
    btn_registrar.click()
    time.sleep(2)
    ##### Verificar mensaje correcto en alerta #####
    success_message = driver.find_element(By.CLASS_NAME, 'alert')
    assert "Registro Exitoso" in success_message.text, "Mensaje de éxito no coincide"
    
    ##### Decodificar la url para retornar el resultado de la comparación de ambas, url esperada y codificada #####
    decoded_url = unquote(driver.current_url)
    expected_url = "http://127.0.0.1:8000/usuarios/iniciar_sesión/"

    return decoded_url == expected_url

def test_eliminar_cliente(driver):
    ##### Ingresar como admin #####
    btn_login = driver.find_element(By.ID, 'btn-login')
    btn_login.click()
    time.sleep(2)
    input_email = driver.find_element(By.ID, 'email')
    input_email.send_keys('ared230000@gmail.com')
    time.sleep(2)
    input_password = driver.find_element(By.ID, 'password')
    input_password.send_keys('12345')
    time.sleep(2)
    btn_ingresar = driver.find_element(By.ID, 'btn-ingresar')
    btn_ingresar.click()
    time.sleep(2)

    ##### Navegar a la sección de clientes #####   
    link_clients = driver.find_element(By.ID, 'link-clients')
    link_clients.click()
    time.sleep(2)

    ##### Buscar al cliente específico #####
    filas = driver.find_elements(By.CLASS_NAME, 'client-row')

    cliente_encontrado = False

    for fila in filas:
        email_element = fila.find_element(By.ID, 'td_email')
        if email_element.text == 'prueba8@gmail.com':
            cliente_encontrado = True

            ##### Eliminar cliente #####
            eliminar_boton = fila.find_element(By.CLASS_NAME, "reject")
            eliminar_boton.click()
            time.sleep(2)

            ##### Validar el mensaje del alerta #####
            alert_text = driver.switch_to.alert.text
            assert "¿Estás seguro de eliminar al cliente?" in alert_text, "Texto de la alerta no coincide"
            time.sleep(2)

            driver.switch_to.alert.accept()    
            break  # Detener el bucle una vez que se haya encontrado y eliminado el cliente

    # Validar si el cliente fue encontrado
    assert cliente_encontrado, "Cliente con el correo especificado no encontrado."

    return driver.current_url == "http://127.0.0.1:8000/admin/clientes/"

def test_cambiar_contraseña(driver):
    ##### Ingresar como usuario #####
    btn_login = driver.find_element(By.ID, 'btn-login')
    btn_login.click()
    time.sleep(2)
    input_email = driver.find_element(By.ID, 'email')
    input_email.send_keys('prueba7@gmail.com')
    time.sleep(2)
    input_password = driver.find_element(By.ID, 'password')
    input_password.send_keys('12345')
    time.sleep(2)
    btn_ingresar = driver.find_element(By.ID, 'btn-ingresar')
    btn_ingresar.click()
    time.sleep(2)

    ##### Navegar a la sección de perfil #####
    link_perfil = driver.find_element(By.ID, 'link-perfil')
    link_perfil.click()
    time.sleep(2)

    ##### Desplazarse a la sección de cambio de contraseña #####
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    ##### Llenar formulario de cambio de contraseña #####
    input_old_password = driver.find_element(By.ID, 'old_password')
    input_old_password.send_keys('12345')
    time.sleep(2)
    input_new_password = driver.find_element(By.ID, 'new_password')
    input_new_password.send_keys('123456')
    time.sleep(2)
    input_confirm_password = driver.find_element(By.ID, 'confirm_password')
    input_confirm_password.send_keys('123456')
    time.sleep(2)
    btn_cambiar_contraseña = driver.find_element(By.ID, 'btn-cambiar-contraseña')
    btn_cambiar_contraseña.click()
    time.sleep(2)
    ##### Verificar mensaje correcto en alerta #####
    success_message = driver.find_element(By.CLASS_NAME, 'alert-success')
    assert "Contraseña actualizada exitosamente" in success_message.text, "Mensaje de éxito no coincide"

    return driver.current_url == "http://127.0.0.1:8000/usuarios/perfil/"