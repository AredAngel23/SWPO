from selenium.webdriver.common.by import By
import time

def test_aprobar_usuario(driver):
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

    ##### Buscar al usuario específico #####
    filas = driver.find_elements(By.ID, 'user_row')
    time.sleep(2)
    
    usuario_encontrado = False
    for fila in filas:
        email_element = fila.find_element(By.CLASS_NAME, 'td-email')
        if email_element.text == 'prueba5@gmail.com':
            usuario_encontrado = True

            ##### Aprobar al usuario #####
            btn_approve = fila.find_element(By.CLASS_NAME, 'approve')
            btn_approve.click()
            time.sleep(2)

            ##### Confirmar la acción #####
            alert = driver.switch_to.alert
            alert.accept()
            time.sleep(2)
    
            break # Detener el bucle una vez que se haya encontrado y eliminado el cliente
    
    # Validar si el usuario fue encontrado
    assert usuario_encontrado, "Usuario con el correo especificado no encontrado."

    return 

def test_aprobar_prestamo(driver):
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

    ##### Buscar al prestamo específico #####
    filas = driver.find_elements(By.ID, 'loan_row')
    time.sleep(2)

    prestamo_encontrado = False
    for fila in filas:
        email_element = fila.find_element(By.ID, 'td_email')
        if email_element.text == '@gmail.com':
            prestamo_encontrado = True

            ##### Aprobar el préstamo #####
            btn_approve = fila.find_element(By.ID, 'approve_loan')
            btn_approve.click()
            time.sleep(2)

            ##### Confirmar la acción #####
            alert = driver.switch_to.alert
            alert.accept()
            time.sleep(2)

            break # Detener el bucle una vez que se haya encontrado y eliminado el cliente
    
    # Validar si el usuario fue encontrado
    assert prestamo_encontrado, "Préstamo especificado no encontrado."

    return
