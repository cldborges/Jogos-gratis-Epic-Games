import time
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def cadastrar_credenciais(usuario='', senha=''):
    if usuario =='':
        usuario = input('Qual o usuário?')
    if senha == '':
        senha = input('Qual a senha?')
    with open('conf.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(f'{usuario}\n{senha}')
    print('Usuário e senha atualizados!')


def ler_credenciais():
    with open('conf.txt', 'r', encoding='utf-8') as arquivo:
        usuario, senha = arquivo.readlines()
    return usuario, senha


def salvar_cookies(driver):
    time.sleep(90)
    pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
    print('Cookies Salvos!')


def login_with_epic(driver):
    driver.get('https://www.epicgames.com/site/login')
    #WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-cOFTSb')))
    #WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-cOFTSb')))
    #driver.find_element(By.CLASS_NAME, 'sc-cOFTSb').click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'login-with-epic')))
    # WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID, 'login-with-epic')))
    driver.find_element(By.ID, 'login-with-epic').click()
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID, 'email')))
    #driver.find_element(By.CLASS_NAME, 'sc-cOFTSb').click()
    usuario, senha = ler_credenciais()
    driver.find_element(By.ID, 'email').send_keys(usuario)
    driver.find_element(By.ID, 'password').send_keys(senha)
    time.sleep(2)
    driver.find_element(By.ID, 'sign-in').click()


def get_chrome_version():
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager(path = r"C:\Temp\Sessoes\chromedriver").install()))
    # driver.get('www.google.com.br')
    version = driver.capabilities["browserVersion"].split('.')[0]
    driver.quit()
    print(f'Versão do chrome: {version}')
    return version
