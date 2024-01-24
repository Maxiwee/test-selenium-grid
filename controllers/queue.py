import os
import requests
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def test(url, name, queue):
    #tiempo = random.randint(2, 10)
    #print(tiempo)
    options = webdriver.ChromeOptions()
    options.set_capability(f"name:", f"{name}")
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
        sleep(60)
        driver.quit()
        queue.instance_ready()
        return "Ejecucion finalizada"
    except Exception as err:
        print("## ERROR ##", err)
        driver.quit()
        return "Error"

class Queue():
    def __init__(self):
        self.queue = []

    def get_selenium_queue(self):
        GRID_SERVER_IP = os.getenv("GRID_SERVER_IP")
        print(GRID_SERVER_IP)
        res = requests.get('http://localhost:4444/se/grid/newsessionqueue/queue').json()
        return res["value"]

    def start_thread(self, id):
        MAX_SESIONS = 2

        findId = id in self.queue

        if findId:
            return True
        if len(self.queue):
            print(f"Hay cola, nuevo elemento:{id}")
            self.queue.append(id)
            return f"Add to queue {id}"
        else:
            instances_on = self.get_selenium_queue()
            if len(instances_on) < MAX_SESIONS:
                url = "https://dev.viradoctores.com/"
                thread = threading.Thread(target=test, args=(url, id, self))
                thread.start()
                return f"Add to grid {id}"
            else:
                self.queue.append(id)
                return f"Add to queue {id}"

    def instance_ready(self):
        if len(self.queue):
            next_item = self.queue[0]
            res = self.start_thread(next_item)
            self.queue.pop(0)
        else:
            return "COLA ACABADA"