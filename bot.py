from selenium import webdriver
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
load_dotenv()
import os


browser = webdriver.Chrome()
browser.get('https://www.instagram.com/')
time.sleep(2)

########################## essa variavel pode mudar com tempo 
campo_login = '//*[@id="loginForm"]/div/div[1]/div/label/input'
campo_senha = '//*[@id="loginForm"]/div/div[2]/div/label/input'
notificacao_class = '_a9_1'
bolinha_class = 'xzolkzo'   
msg_class = '_ab6-'
contato_cliente = 'xuxw1ft'
msgs_cliente = 'x126k92a'
inputcampo = 'x14wi4xw'


login = browser.find_element(By.XPATH,campo_login)
login.click()
login.send_keys(os.environ["USER_INSTAGRAM"])
time.sleep(2)
senha = browser.find_element(By.XPATH,campo_senha)
senha.click()
senha.send_keys(os.environ["SENHA_INSTAGRAM"])
time.sleep(2)
senha.send_keys(Keys.ENTER)
time.sleep(5)

######## entrando na area de chat

browser.get("https://www.instagram.com/direct/inbox/")
time.sleep(5)
notificacao = browser.find_element(By.CLASS_NAME,notificacao_class)
time.sleep(1)
notificacao.click()
time.sleep(5)


##############
### criar fnc do bot
#####################


def bot():
    try:
        ##### clicar na bolinha azul(notificao de nova mensagem)
        bolinha = browser.find_element(By.CLASS_NAME,bolinha_class)
        bolinha = browser.find_elements(By.CLASS_NAME,bolinha_class)
        clica_bolinha = bolinha[-1]
        acao_bolinha = webdriver.common.action_chains.ActionChains(browser)
        acao_bolinha.move_to_element_with_offset(clica_bolinha,0,-20)
        acao_bolinha.click()
        acao_bolinha.perform()
        print("Clicou na bolinha")
        time.sleep(3)

        #### nome/contato do cliente

        contato = browser.find_elements(By.CLASS_NAME,contato_cliente)
        contato = contato[6]
        contato2 = contato.text

        print(contato2)
        print("peguei contato cliente")

        ########### Pegar mensagem do cliente
        todas_as_msg = browser.find_elements(By.CLASS_NAME,msgs_cliente);
        todas_as_msg_texto = [e.text for e in todas_as_msg]
        msg_ultima = todas_as_msg_texto[-1]
        print(msg_ultima)
        time.sleep(2)
        print("Finalizou parte de pegar ultima mensagem")
        ##########################


        ###################### Responder mensagem
        textarea = browser.find_element(By.CLASS_NAME,inputcampo)
        textarea.send_keys("Olá eu sou CoisinhaBot",Keys.ENTER)
        time.sleep(3)
        print("mensagem respondida")
        ################################
        
        ### voltar pra mensagem  
        msg_padrao = browser.find_elements(By.CLASS_NAME,msg_class)
        msg_padrao = msg_padrao[4]
        time.sleep(2)
        msg_padrao.click()
    except:
        print('aguarde')
        time.sleep(3)
while True :
    bot()