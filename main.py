from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import concurrent.futures
import random
import threading

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"


def test(url):
    #tiempo = random.randint(2, 10)
    #print(tiempo)
    options = webdriver.ChromeOptions()
    options.set_capability(f"se:", "My simple test")
    driver = webdriver.Remote(command_executor="http://localhost:4444", options=options)
    #sleep(tiempo)
    try:
        driver.maximize_window()
        driver.get(url)
        print(f"Se inicio el navegador y entramos a la URL")

        driver.implicitly_wait(2)
        login = driver.find_element(By.LINK_TEXT, 'Inicia sesión')
        login.click()
        #print("Se hace click en el primero boton de iniciar sesión")
        #sleep(10)
        email = driver.find_element(By.NAME, 'email')
        email.send_keys("maxirocha250397@gmail.com")
        #print("Ingresamos el correo")
        #sleep(10)
        password = driver.find_element(By.NAME, 'password')
        password.send_keys("12345678")
        #print("Ingresamos la contraseña")
        #sleep(10)
        button_login = driver.find_element(By.CSS_SELECTOR, "button")
        button_login.click()
        #print("Nos logueamos")
        #sleep(10)
        driver.implicitly_wait(10)
        button_profile = driver.find_element(By.CLASS_NAME, "szh-menu-button")
        button_profile.click()
        #print("Apretamos la foto de nuestro perifl")
        #sleep(10)
        driver.implicitly_wait(5)
        profile = driver.find_elements(By.XPATH, "//a[contains(@href,'profile')]")
        profile[0].click()
        #print("Ingresamos a nuestra info de perfil")
        sleep(15)
        driver.implicitly_wait(15)
        icon_help = driver.find_elements(By.XPATH, "//div[contains(@title,'Ayuda')]")
        icon_help[0].click()

        #print("Vamos a la seccion de ayuda")
        driver.quit()
        return "Ejecucion finalizada"
    except Exception as err:
        print("## ERROR ##", err)
        driver.quit()
        return "Error"

@app.route('/test')
def asd():
    url = "https://dev.viradoctores.com/"
    thread = threading.Thread(target=test, args=(url))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3005, debug=False)
    #urls = ["https://dev.viradoctores.com/", "https://dev.viradoctores.com/", "https://dev.viradoctores.com/", "https://dev.viradoctores.com/", "https://dev.viradoctores.com/", "https://dev.viradoctores.com/", "https://dev.viradoctores.com/", "https://dev.viradoctores.com/"]

    #hilos = []
    #c = 1
    #for url in urls:
    #    thread = threading.Thread(target=test, args=(url, c))
    #    c +=1
    #    hilos.append(thread)
    #    thread.start()

    #for hilo in hilos:
    #    hilo.join()

    #with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    #    results = list(executor.map(test, urls))

    #for url in urls:
    #    test(url)

    #for res in results:
        #print(res)
