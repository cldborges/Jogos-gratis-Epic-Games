from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

from funcoes import login_with_epic

url = 'https://store.epicgames.com/pt-BR/free-games'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

#login_with_epic(driver)

#time.sleep(15)

WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'css-1myhtyb')))

jogos_gratis = driver.find_element(By.CLASS_NAME, 'css-1myhtyb')
jogos_gratis_da_semana = jogos_gratis.find_elements(By.CLASS_NAME, 'css-5auk98')
print(len(jogos_gratis_da_semana))

#pegar links
links = []
for jogo_gratis in jogos_gratis_da_semana:
    jogo_gratis_semana = None
    try:
        jogo_gratis_semana = jogo_gratis.find_element(By.CLASS_NAME, 'css-11xvn05') #verifica se tem a DIV "GRÁTIS" no jogo
        link = jogo_gratis.find_element(By.CSS_SELECTOR, 'a').get_attribute("href")
        links.append(link)
        print(links)
    except:
        pass

for link in links:
    driver.get(link)
    try:
        WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'css-187rod9'))
            )
    except:
        print('Não funcionou aqui')
        driver.quit()
    #print(driver.find_element(By.CLASS_NAME, 'css-187rod9').text)
    driver.find_element(By.CLASS_NAME, 'css-187rod9').click()
    try:
        WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="purchase-app"]/div/div/div/div[2]/div[2]/button'))
            )
    except:
        print('Não funcionou aqui')
        driver.quit()
    driver.find_element(By.XPATH, '//*[@id="purchase-app"]/div/div/div/div[2]/div[2]/button').click()
    time.sleep(15)
    
print(links)