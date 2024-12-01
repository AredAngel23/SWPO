from selenium import webdriver
import time

from app.tests.test_login import test_login, test_admin_login
from app.tests.test_users import test_eliminar_cliente, test_cambiar_contraseña, test_registrar_usuario

def initialize_driver():
    driver = webdriver.Chrome() 
    return driver

def main():
    driver = initialize_driver()
    driver.maximize_window()
    driver.get('http://127.0.0.1:5000/')

    try:
        # Pruebas
        resultado = test_eliminar_cliente(driver)
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