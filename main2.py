from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pickle
from funcoes import *
import time

url = 'https://store.epicgames.com/pt-BR/free-games'

try:
    usuario, senha = ler_credenciais()
except:
    cadastrar_credenciais()
    usuario, senha = ler_credenciais()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

time.sleep(90)



jogos_gratis = driver.find_element(By.CLASS_NAME, 'css-1myhtyb')
jogos_gratis_da_semana = jogos_gratis.find_elements(By.CLASS_NAME, 'css-5auk98')
print(len(jogos_gratis_da_semana))