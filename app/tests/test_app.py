from selenium import webdriver
import time

from .test_login import test_login, test_admin_login
from .test_users import test_eliminar_cliente, test_cambiar_contraseña, test_registrar_usuario
from .test_admin import test_aprobar_usuario, test_aprobar_prestamo
from .test_loan import test_solicitar_prestamo

def initialize_driver():
    driver = webdriver.Firefox() 
    return driver

def main():
    driver = initialize_driver()
    driver.maximize_window()
    driver.get('http://127.0.0.1:8000/')

    try:
        # Pruebas
        resultado = test_aprobar_prestamo(driver)
        if resultado:
            print("Prueba Exitosa")
        else:
            print("Prueba Fallida")

        time.sleep(3)
    except Exception as e:
        print(f"Error durante las pruebas: {e}")
    finally:
        driver.quit()  

if __name__ == '__main__':
    main()