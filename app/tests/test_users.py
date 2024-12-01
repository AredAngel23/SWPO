from selenium.webdriver.common.by import By
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
    input_nivelEducativo.send_keys('')
    time.sleep(2)

    return driver.current_url == "http://127.0.0.1:5000/usuarios/iniciar_sesión/"

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
    time.sleep(2)

    cliente_encontrado = False

    for fila in filas:
        email_element = fila.find_element(By.ID, 'td-email')
        if email_element.text == 'aldo@gmail.com':
            cliente_encontrado = True

            ##### Eliminar cliente #####
            eliminar_boton = fila.find_element(By.CLASS_NAME, "reject")
            eliminar_boton.click()
            time.sleep(2)

            ##### Validar el mensaje del alerta #####
            alert_text = driver.switch_to.alert.text
            assert "¿Estás seguro de eliminar al cliente?" in alert_text, "Texto de la alerta no coincide"

            driver.switch_to.alert.accept()    
            break  # Detener el bucle una vez que se haya encontrado y eliminado el cliente

    # Validar si el cliente fue encontrado
    assert cliente_encontrado, "Cliente con el correo especificado no encontrado."

    return driver.current_url == "http://127.0.0.1:5000/admin/clientes/"

def test_cambiar_contraseña(driver):
    ##### Ingresar como usuario #####
    btn_login = driver.find_element(By.ID, 'btn-login')
    btn_login.click()
    time.sleep(2)

    input_email = driver.find_element(By.ID, 'email')
    input_email.send_keys('angy@gmail.com')
    time.sleep(2)

    input_password = driver.find_element(By.ID, 'password')
    input_password.send_keys('1234567')
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
    input_old_password.send_keys('1234567')
    time.sleep(2)

    input_new_password = driver.find_element(By.ID, 'new_password')
    input_new_password.send_keys('12345')
    time.sleep(2)

    input_confirm_password = driver.find_element(By.ID, 'confirm_password')
    input_confirm_password.send_keys('12345')
    time.sleep(2)

    btn_cambiar_contraseña = driver.find_element(By.ID, 'btn-cambiar-contraseña')
    btn_cambiar_contraseña.click()
    time.sleep(2)

    success_message = driver.find_element(By.CLASS_NAME, 'alert-success')
    assert "Contraseña actualizada exitosamente" in success_message.text, "Mensaje de éxito no coincide"
    time.sleep(2)

    return driver.current_url == "http://127.0.0.1:5000/usuarios/perfil/"