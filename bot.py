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


campo_login = '//*[@id="loginForm"]/div/div[1]/div/label/input'
campo_senha = '//*[@id="loginForm"]/div/div[2]/div/label/input'
notificacao_class = '_a9_1'

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


# /html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]
# /html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]
######## entrando na area de chat

browser.get("https://www.instagram.com/direct/inbox/")
time.sleep(5)
notificacao = browser.find_element(By.CLASS_NAME,notificacao_class)
time.sleep(1)
notificacao.click()
time.sleep(30)