from selenium.webdriver.common.by import By

def test_login(driver):
    btn_login = driver.find_element(By.ID, 'btn-login')
    btn_login.click()

    input_email = driver.find_element(By.ID, 'email')
    input_email.send_keys('adri@gmail.com')

    input_password = driver.find_element(By.ID, 'password')
    input_password.send_keys('12345')

    btn_ingresar = driver.find_element(By.ID, 'btn-ingresar')
    btn_ingresar.click()

    return driver.current_url == "http://127.0.0.1:5000/"

def test_admin_login(driver):
    btn_login = driver.find_element(By.ID, 'btn-login')
    btn_login.click()

    input_email = driver.find_element(By.ID, 'email')
    input_email.send_keys('ared230000@gmail.com')

    input_password = driver.find_element(By.ID, 'password')
    input_password.send_keys('12345')

    btn_ingresar = driver.find_element(By.ID, 'btn-ingresar')
    btn_ingresar.click()

    return driver.current_url == "http://127.0.0.1:5000/admin/"