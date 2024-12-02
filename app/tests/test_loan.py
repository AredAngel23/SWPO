from selenium.webdriver.common.by import By
from urllib.parse import unquote
import time

def test_solicitar_prestamo(driver):
    ##### Ingresar como usuario #####
    btn_login = driver.find_element(By.ID, 'btn-login')
    btn_login.click()
    time.sleep(2)
    input_email = driver.find_element(By.ID, 'email')
    input_email.send_keys('prueba11@gmail.com')
    time.sleep(2)
    input_password = driver.find_element(By.ID, 'password')
    input_password.send_keys('12345')
    time.sleep(2)
    btn_ingresar = driver.find_element(By.ID, 'btn-ingresar')
    btn_ingresar.click()
    time.sleep(2)

    ##### Ir a la sección de prestamos #####
    link_loan = driver.find_element(By.ID, 'link-loan')
    link_loan.click()
    time.sleep(2)
    ##### Ir a la sección para solicitar prestamo #####
    btn_solicitar_loan = driver.find_element(By.CLASS_NAME, 'primerlink')
    btn_solicitar_loan.click()
    time.sleep(2)

    ##### Solicitar prestamo #####
    input_monto = driver.find_element(By.ID, 'monto')
    input_monto.send_keys('10000')
    time.sleep(2)
    input_plazo = driver.find_element(By.ID, 'plazo')
    input_plazo.send_keys('12')
    time.sleep(2)
    btn_solicitar = driver.find_element(By.ID, 'btn-submit')
    btn_solicitar.click()
    time.sleep(2)
    ##### Verificar mensaje de éxito #####
    success_message = driver.find_element(By.CLASS_NAME, 'alert-success')
    assert "Solicitud de préstamo enviada correctamente." in success_message.text, "Mensaje de éxito no coincide"
    time.sleep(2)

    ##### Decodificar la url para retornar el resultado de la comparación de ambas, url esperada y codificada #####
    decoded_url = unquote(driver.current_url)
    expected_url = "http://127.0.0.1:8000/info_préstamo/"

    return decoded_url == expected_url
