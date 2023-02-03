import time
import os
import wget
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
import re,requests


URL_S = 'https://discord.com'
URL = 'https://discord.com/login'

# test
url_name = '/channels/653357729288814643/653357731591225381'

class ServerDiscord():
    def __init__(self,name,xpath,url):
        self.name = name
        self.url = url
        self.xpath = xpath
    
    def __str__(self):
        return self.name
#TODO: 4) En esta vemos los tiempos de espera y se programan de manera asyncrona ademas de elmina codigo redundante        

# time_verification es es el timpo que se le dedica a atencion a un servidor
class DiscordScrap():    
    def __init__(self,email,password,time_verification=3000):
        # Datos de una persona normal
        self.email = email
        self.password = password
        self.verification = time_verification   # timepo de verificacion de los mensajes definido cmoo el timepo activo del bot
        self.servers = []
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    # por el momento es asi pero despues va a poder usar la url de cada servidor de href
    def entry_server(self,url_name):
        #ser = self.driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/nav/ul/div[2]/div[3]/div[16]/div[2]/div').click()
        #ser = self.driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/nav/ul/div[2]/div[3]/div[16]/div[2]/div/div/svg/foreignObject/div').click()
        
        # por el momento entra a este pero despues va a a estar asi
        self.driver.get(URL_S + url_name)
        time.sleep(5)


    def start(self):
        self.driver.get(URL)
        self.login()

        time.sleep(5)
        self.server_list()
        #self.server_list()\
        #self.entry_server(url_name)
        #self.send_message("wenisima lam")
        #self.detect_chat_message()

    # Mo esta del todo solucionado este problema
    # sacado de githubinvestigar como se logro la deteccion de textarea a traves de xpath
    def send_message(self,message):
        
        time.sleep(10)
        print("envio de mensaje")
        msg_xpath = '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div/div'
        #input_message = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//textarea[@placeholder='Enviar mensaje a #general']"))).send_keys(message)
        
        self.driver.find_element_by_xpath(msg_xpath).send_keys(message)
        self.driver.find_element_by_xpath(msg_xpath).send_keys(Keys.ENTER)
    

    # sacar el texto de esto y procesar
    def detect_chat_message(self):
        xpath_msg = '//*[@id="message-content-892104240607146035"]'
        chat = []
        # tenemos por el momento de 50 chat por el momento despues tene,os que optimizar esto
        set_msg = self.driver.find_elements_by_class_name('messageListItem-1-jvGY')

        print(len(set_msg))
        for i in set_msg:
            chat.append(i.text)
        # ahroa que obtenemos los datos tenemos que procesar los datos


    '''
    def choose(self):
        """Choose where to send messages"""
        self.driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/nav/ul/div[2]/div[3]/div[2]/div[2]').click()
        self.driver.find_element_by_xpath('//*[@id="channels"]/div/div[4]').click()
    '''

    # TODO: 1) En horas definidmos la funcion que va a detectar las notififcacikones del discord
    # Ademas de la lista de Servers
    # y la lista de personas de cada Server
    # la detedcion de las notificaciones de los servidoress
    def notification(self):
        pass
    

    #   La lista de amigos debe tener el nombre de la personas
    def list_friend(self):
        pass
    

    # una funcion que va a recorrer todos los servidores y los guarda (Funcion no usada)
    def server_list(self):
        #server_list = self.driver.find_elements_by_class_name('listItem-GuPuDH')
        #server_list = self.driver.find_elements_by_class_name('wrapper-1BJsBx')
        # capturar la informacion a traves de todos los for
        #print(len(server_list))
        
        time.sleep(10)
        print("preguntando al servidor")
        res = requests.get(URL)
        print(res.text)
        bs = BeautifulSoup(res.content,'html.parser')
        data = bs.find_all('div',class_='listItem-GuPuDH')
        print(len(data))
        print("paso por aqui")
        for i in data:
            print("entro")
            print(data.href)
    

    def login(self):
        time.sleep(2)
        user = self.driver.find_element_by_name("email")
        user.send_keys(self.email)
        
        pass_user = self.driver.find_element_by_name("password")
        pass_user.send_keys(self.password)
        pass_user.send_keys(Keys.RETURN)
        time.sleep(3)

    '''
    # Esta funcion no va a estar definida aun hasta que el bot tome ;a desision de las cosas
    def logout(self):
        pass
    '''




